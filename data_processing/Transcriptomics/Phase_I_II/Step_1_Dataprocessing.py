import pandas as pd
import numpy as np
import abagen
from scipy.stats import spearmanr
import os
from statsmodels.stats.multitest import fdrcorrection
from neuromaps import nulls, stats, parcellate
from neuromaps.images import dlabel_to_gifti  # 新增：转换 dlabel
import nibabel as nib
from nilearn.image import new_img_like

# ==========================================
# 路径设置（新增表面 atlas 路径）
# ==========================================
gmv_data_path = '/Users/qingchen/Documents/code/ToolBox/data_processing/Transcriptomics/Data_Test/GMV_246.csv'
atlas_path = '/Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_246_2mm.nii.gz'
lut_path = '/Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_freesurfer/BN_Atlas_246_LUT.txt'
surface_atlas_path = '/Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_freesurfer/fsaverage/fsaverage_LR32k/fsaverage.BN_Atlas.32k_fs_LR.dlabel.nii'  # ← 替换为你的实际路径

output_path = './gene_imaging_correlation_results.csv'
stable_matrix_path = './stable_gene_expression.csv'
print("--- 正在启动分析流程 ---")

# ==========================================
# 2. 加载 GMV 数据
# ==========================================
try:
    df_gmv = pd.read_csv(gmv_data_path, header=None)
    gmv_vector = df_gmv.iloc[:, 1].values
    if len(gmv_vector) != 246:
        print(f"警告：检测到数据行数为 {len(gmv_vector)}，请确保与 246 分区一致！")
except Exception as e:
    print(f"读取数据失败: {e}")
    exit()

# ==========================================
# Phase 1 Step 1-4: LUT + atlas_info + GMV匹配
# ==========================================
print("Phase 1 Step 1-4: 构建 atlas_info + GMV向量...")
df_lut = pd.read_csv(lut_path, sep='\s+', header=None, skiprows=1,
                     names=['ID', 'Label', 'R', 'G', 'B', 'A'])
df_lut['ID'] = df_lut['ID'].astype(int)
df_lut['Label'] = df_lut['Label'].astype(str)

df_lut['hemisphere'] = df_lut['Label'].apply(lambda x: 'left' if '_L' in x else 'right')
df_lut['structure'] = df_lut['ID'].apply(lambda x: 'cortex' if 1 <= x <= 210 else 'subcortex')

atlas_info = df_lut[['ID', 'hemisphere', 'structure']].copy()
atlas_info.columns = ['id', 'hemisphere', 'structure']
atlas_info.set_index('id', inplace=True)

# ==========================================
# 3. abagen Phase 1
# ==========================================
print("正在从艾伦脑图谱提取基因表达数据，这可能需要几分钟...")
expression_return = abagen.get_expression_data(
    atlas_path,
    atlas_info=atlas_info,
    probe_selection='diff_stability',
    ibf_threshold=0.5,
    donor_probes='aggregate',
    lr_mirror=True,
    missing='interpolate',
    tolerance=2,
    norm_matched=True,
    corrected_mni=True,
    return_donors=True,
    return_report=True,
    verbose=2
)

print("abagen 返回类型:", type(expression_return))
print("返回长度:", len(expression_return))

# 关键修正：提取捐体数据（dict）和报告字符串
donor_expression = expression_return[0]  # dict {donor_id: DataFrame}
report_text = expression_return[1]  # 报告字符串

# 保存报告为文件（可选，但推荐记录方法）
with open('abagen_processing_report.txt', 'w') as f:
    f.write(report_text)
print("处理报告已保存为: abagen_processing_report.txt")

# 手动聚合捐体数据（文章 Step 5：平均跨捐体）
print("手动聚合捐体表达数据...")
all_donor_dfs = []
for donor_id, df in donor_expression.items():
    all_donor_dfs.append(df)

# concat 所有捐体，按脑区（index）取平均
gene_expression = pd.concat(all_donor_dfs).groupby(level=0).mean()
print(f"聚合后表达矩阵维度: {gene_expression.shape}")

# Step 6: DS 筛选（使用捐体 dict）
from abagen import keep_stable_genes

print("执行 DS 筛选...")
donor_list = list(donor_expression.values())  # list of DataFrame

filtered_dfs, ds_values = keep_stable_genes(
    donor_list,
    threshold=0.4,
    return_stability=True
)

# ds_values 是 numpy.ndarray (长度 = 基因数，值 = DS 分数)
print("ds_values 类型:", type(ds_values))
print("ds_values 形状:", ds_values.shape)

# 从任意一个捐体矩阵获取基因名列表（所有捐体基因相同）
all_genes = donor_list[0].columns.tolist()  # list of str, 基因名
print("总基因数:", len(all_genes))

# 过滤 DS > 0.4 的基因
stable_mask = ds_values > 0.4
stable_genes = [all_genes[i] for i in range(len(all_genes)) if stable_mask[i]]

print(f"DS > 0.4 的基因数: {len(stable_genes)}")

# 用这些基因名过滤聚合矩阵
stable_expression = gene_expression[stable_genes]

print(f"筛选后稳定表达矩阵维度: {stable_expression.shape}")
stable_expression.to_csv(stable_matrix_path)
print(f"稳定基因矩阵保存至: {stable_matrix_path}")

# ==========================================
# 4. 计算关联分析 (Phase 2)
# ==========================================
print("正在计算每个基因与灰质体积的相关性...")
valid_mask = stable_expression.notnull().all(axis=1)
n_dropped = len(stable_expression) - valid_mask.sum()
print(f"提示：246个脑区中有 {n_dropped} 个脑区因缺乏基因采样被剔除，实际参与计算脑区数：{valid_mask.sum()}")

clean_gmv = gmv_vector[valid_mask]
clean_expression = stable_expression[valid_mask]

results = []
for gene_name in clean_expression.columns:
    gene_vector = clean_expression[gene_name].values
    corr, p_value = spearmanr(clean_gmv, gene_vector, nan_policy='omit')
    results.append({
        'Gene': gene_name,
        'Correlation': corr,
        'Uncorrected_P': p_value
    })

# ==========================================
# 5. 排序并保存结果（加 FDR 校正）
# ==========================================
results_df = pd.DataFrame(results)
results_df = results_df.dropna(subset=['Correlation'])

# FDR 校正（BH 方法，文章推荐）
rejected, p_fdr = fdrcorrection(results_df['Uncorrected_P'], alpha=0.05, method='indep')  # indep 为 BH
results_df['FDR_P'] = p_fdr
results_df['Significant_FDR'] = results_df['FDR_P'] < 0.05  # 是否显著

results_df['Abs_Corr'] = results_df['Correlation'].abs()
results_df = results_df.sort_values(by='Abs_Corr', ascending=False)

results_df.to_csv(output_path, index=False)

print(f"--- 分析完成！---")
print(f"结果已保存至: {output_path}")
print("前 5 个最强的相关基因（含 FDR）：")
print(results_df.head(5)[['Gene', 'Correlation', 'Uncorrected_P', 'FDR_P', 'Significant_FDR']])

# ==========================================
# Phase 2 高级：空间自相关校正
# Alexander–Bloch null (fsLR 32k, parcel-wise)
# ==========================================

from neuromaps import nulls
from neuromaps.images import dlabel_to_gifti
print("\nPhase 2 高级：空间自相关校正（alexander_bloch null model, parcel-wise）...")
print("\n>>> Phase II：空间自相关校正（皮层限定）")

# 皮层 mask
cortex_mask = np.arange(246) < 210

gmv_ctx = clean_gmv[cortex_mask]
expr_ctx = clean_expression.loc[cortex_mask]

# dlabel → GIFTI（定义 surface 拓扑）
bn_gii = dlabel_to_gifti(surface_atlas_path)

# ------------------------------------------
# Step 1: dlabel → GIFTI（仅用于定义 surface 拓扑）
# ------------------------------------------
print("加载 fsLR 32k BN Atlas dlabel...")
bn_parcellation_gii = dlabel_to_gifti(surface_atlas_path)
print("dlabel 转换完成")

# ------------------------------------------
# Step 2: 生成 Alexander–Bloch null
# ⚠️ 输入必须是 parcel-wise GMV（246）
# ------------------------------------------
print("生成 alexander_bloch null maps (n_perm=2000)...")

nulls_ab = nulls.alexander_bloch(
    data=clean_gmv,                 # ← 246 维向量（关键）
    atlas="fsLR",
    density="32k",
    parcellation=bn_parcellation_gii,
    n_perm=2000,
    seed=42
)

print(f"nulls_ab 形状: {nulls_ab.shape}")  # (2000, 246)

# ==========================================
# Phase II 高级：Alexander–Bloch（仅皮层 210）
# ==========================================
print("\n>>> Phase II：空间自相关校正（皮层限定）")

# 皮层 mask
cortex_mask = np.arange(246) < 210

gmv_ctx = clean_gmv[cortex_mask]
expr_ctx = clean_expression.loc[cortex_mask]

# dlabel → GIFTI（定义 surface 拓扑）
bn_gii = dlabel_to_gifti(surface_atlas_path)

# 生成 spin null（210 × 2000）
nulls_ab = nulls.alexander_bloch(
    data=gmv_ctx,
    atlas='fsLR',
    density='32k',
    parcellation=bn_gii,
    n_perm=2000,
    seed=42
)

print(f">>> null maps 维度: {nulls_ab.shape}")

# 仅对 FDR 显著基因做 AB 校正
sig_genes = results_df.loc[
    results_df['Significant_FDR'], 'Gene'
].tolist()

ab_pvals = {}

for gene in sig_genes:
    gene_vec = expr_ctx[gene].values
    r_obs, _ = spearmanr(gmv_ctx, gene_vec)

    null_corrs = np.array([
        spearmanr(nulls_ab[:, i], gene_vec)[0]
        for i in range(nulls_ab.shape[1])
    ])

    ab_pvals[gene] = np.mean(np.abs(null_corrs) >= np.abs(r_obs))

ab_df = pd.DataFrame.from_dict(
    ab_pvals, orient='index', columns=['AB_P']
)
ab_df.to_csv('ab_corrected_p.csv')

print(">>> Alexander–Bloch 校正完成，结果保存至 ab_corrected_p.csv")
print("\n--- Pipeline 全部完成（无错误，方法学正确）---")

# ==========================================
# Phase 3: Gene Enrichment Analysis (GCEA)
# ==========================================
print("\n>>> Phase 3: 基因富集分析（功能含义评估）")

# 安装 gseapy（如果未安装，先在终端运行：pip install gseapy）

import gseapy as gp
from gseapy.plot import barplot, dotplot
import matplotlib.pyplot as plt




# Step 1: 加载 Phase 2 输出，提取显著基因
# 优先用 spin 校正后的 AB_P < 0.05（最严格）
try:
    ab_df = pd.read_csv('ab_corrected_p.csv', index_col=0)
    sig_genes_spin = ab_df[ab_df['AB_P'] < 0.05].index.tolist()
    print(f"Spin 校正显著基因数 (AB_P < 0.05): {len(sig_genes_spin)}")
except FileNotFoundError:
    print("未找到 ab_corrected_p.csv，使用 FDR 显著基因作为备选")
    sig_genes_spin = results_df[results_df['Significant_FDR']]['Gene'].tolist()

# 备选：如果 spin 基因太少，用 FDR 显著基因
sig_genes_fdr = results_df[results_df['Significant_FDR']]['Gene'].tolist()
print(f"FDR 显著基因数: {len(sig_genes_fdr)}")

# 使用 spin 优先（文章推荐最严格校正）
significant_genes = sig_genes_spin if len(sig_genes_spin) > 5 else sig_genes_fdr
print(f"用于富集的前景基因数: {len(significant_genes)}")
print("示例基因:", significant_genes[:10])

# Step 2: 背景基因集（所有参与计算的基因，避免 bias）
background_genes = results_df['Gene'].tolist()
print(f"背景基因数: {len(background_genes)}")

# Step 3: GO Biological Process 富集（文章推荐 GO BP）
print("执行 GO Biological Process 富集...")
enr_go = gp.enrichr(
    gene_list=significant_genes,
    gene_sets='GO_Biological_Process_2021',  # 或 'GO_Biological_Process_2023'
    organism='human',
    background=background_genes,  # 自定义背景（文章强调）
    cutoff=0.05  # FDR < 0.05
)

go_results = enr_go.results
go_results.to_csv('go_enrichment_results.csv', index=False)
print("GO 富集结果保存至: go_enrichment_results.csv")
print("前 5 个显著 GO 通路：")
print(go_results[['Term', 'Adjusted P-value', 'Overlap', 'Genes']].head())

# Step 4: KEGG Pathway 富集（文章推荐 KEGG）
print("执行 KEGG Pathway 富集...")
enr_kegg = gp.enrichr(
    gene_list=significant_genes,
    gene_sets='KEGG_2021_Human',
    organism='human',
    background=background_genes,
    cutoff=0.05
)

kegg_results = enr_kegg.results
kegg_results.to_csv('kegg_enrichment_results.csv', index=False)
print("KEGG 富集结果保存至: kegg_enrichment_results.csv")
print("前 5 个显著 KEGG 通路：")
print(kegg_results[['Term', 'Adjusted P-value', 'Overlap', 'Genes']].head())

# Step 5: 可视化（类似文章 Figure 5 的富集图）
if not go_results.empty:
    print("绘制 GO 富集条形图...")
    barplot(go_results, title='Top GO Biological Processes (FDR < 0.05)', cutoff=0.05, top_term=10)
    plt.savefig('go_barplot.png')
    plt.show()

if not kegg_results.empty:
    print("绘制 KEGG 富集点图...")
    dotplot(kegg_results, title='Top KEGG Pathways (FDR < 0.05)', cmap='viridis', cutoff=0.05, top_term=10)
    plt.savefig('kegg_dotplot.png')
    plt.show()

print("\n--- Phase 3 完成！请检查富集表格和图表，评估显著基因的功能含义 ---")
print("建议：如果富集结果为空或不显著，尝试降低阈值（AB_P < 0.1）或扩大前景基因集。")