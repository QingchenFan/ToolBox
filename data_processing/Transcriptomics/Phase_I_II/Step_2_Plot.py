import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 加载数据文件（假设这些文件在当前目录）
stable_expr = pd.read_csv('stable_gene_expression.csv')
results_df = pd.read_csv('gene_imaging_correlation_results.csv')
full_results = pd.read_csv('full_results_with_spin.csv')
ab_p = pd.read_csv('ab_corrected_p.csv')

# 图 1: 稳定基因表达热图 (Top 20 Correlated Genes)
top_genes = results_df.sort_values('Abs_Corr', ascending=False)['Gene'].head(20).tolist()
expr_top = stable_expr[top_genes]  # 提取 top 20 基因的表达矩阵
plt.figure(figsize=(12, 8))
sns.heatmap(expr_top, cmap='viridis', annot=False)
plt.title('Heatmap of Stable Gene Expression for Top 20 Correlated Genes')
plt.xlabel('Genes')
plt.ylabel('Brain Regions (Label)')
plt.xticks(rotation=90)
plt.show()

# 图 2: Top 基因表达分布直方图 (e.g., STPG1)
gene = 'STPG1'  # Top gene from results
expr_values = stable_expr[gene]
plt.figure(figsize=(8, 6))
sns.histplot(expr_values, kde=True, bins=20)
plt.title(f'Distribution of {gene} Expression Across Brain Regions')
plt.xlabel('Expression Value')
plt.ylabel('Frequency')
plt.show()

# 图 3: 显著 vs 非显著基因表达水平箱线图
significant_genes = results_df[results_df['Significant_FDR']]['Gene'].tolist()
non_sig_genes = results_df[~results_df['Significant_FDR']]['Gene'].tolist()

sig_expr = stable_expr[significant_genes].melt()['value']
non_sig_expr = stable_expr[non_sig_genes].melt()['value']

data = pd.concat([pd.DataFrame({'Expression': sig_expr, 'Type': 'Significant'}),
                  pd.DataFrame({'Expression': non_sig_expr, 'Type': 'Non-Significant'})])

plt.figure(figsize=(8, 6))
sns.boxplot(x='Type', y='Expression', data=data)
plt.title('Boxplot: Expression Levels of Significant vs Non-Significant Genes')
plt.ylabel('Expression Value')
plt.show()

# 图 4: 火山图 (Volcano Plot of Gene Correlations with GMV)
plt.figure(figsize=(10, 8))
sns.scatterplot(x='Correlation', y=-np.log10(results_df['Uncorrected_P'] + 1e-10),
                hue=results_df['Significant_FDR'], data=results_df, palette={True: 'red', False: 'gray'})
plt.title('Volcano Plot: Gene Correlations vs -log10(P)')
plt.xlabel('Spearman Correlation')
plt.ylabel('-log10(Uncorrected P)')
plt.axhline(-np.log10(0.05), color='blue', linestyle='--', label='P=0.05')
plt.legend()
plt.show()

# 图 5: Top 20 基因绝对相关条形图
top20 = results_df.sort_values('Abs_Corr', ascending=False).head(20)
plt.figure(figsize=(10, 8))
sns.barplot(x='Abs_Corr', y='Gene', data=top20, color='skyblue')
plt.title('Bar Plot of Top 20 Genes by Absolute Correlation')
plt.xlabel('Absolute Correlation')
plt.ylabel('Genes')
plt.show()

# 图 6: FDR_P vs AB_P 散点图 (只针对显著基因)
sig_full = full_results[full_results['Significant_FDR']]
plt.figure(figsize=(8, 6))
sns.scatterplot(x=-np.log10(sig_full['FDR_P'] + 1e-10), y=-np.log10(sig_full['AB_P'] + 1e-10), data=sig_full)
plt.title('Scatter Plot: -log10(FDR_P) vs -log10(AB_P)')
plt.xlabel('-log10(FDR P)')
plt.ylabel('-log10(Spin-Corrected AB P)')
plt.axline((0, 0), slope=1, color='red', linestyle='--', label='Equality Line')
plt.legend()
plt.show()

# 图 7: Spearman 相关系数分布直方图
plt.figure(figsize=(8, 6))
sns.histplot(results_df['Correlation'], kde=True, bins=50)
plt.title('Histogram of All Gene Correlations with GMV')
plt.xlabel('Spearman Correlation')
plt.ylabel('Frequency')
plt.show()