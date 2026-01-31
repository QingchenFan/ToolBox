import glob
import pandas as pd
import os

# 1. 设置文件路径模式
base_path = "/Volumes/QCII/duilie_processed/duilie_HC1_67_MDD_XCPD_Volume/xcpd_out/xcp_d/"
# 建议使用 recursive=True 如果目录结构较深，但在目前的固定层级下不需要
search_pattern = os.path.join(base_path,"sub-MDD*/func/sub-*_task-rest_acq-ap_run-1_space-MNI152NLin6Asym_atlas-4S456Parcels_reho.tsv")

# 获取所有主文件列表
files_4s = glob.glob(search_pattern)

# 对文件列表进行排序，保证处理顺序（可选）
files_4s.sort()

print(f"找到 {len(files_4s)} 个文件，准备开始处理...")

all_subjects_data = []

# 2. 循环处理每个被试
for file_path_4s in files_4s:

        # 提取 subID
        subID = file_path_4s.split("/")[-3]

        # --- 读取并处理数据 ---
        # 1. 读取 4S456Parcels 文件
        df_4s = pd.read_csv(file_path_4s, sep='\t')

        # 2. 插入 subID 到第一列
        # insert(插入位置, 列名, 值)
        df_4s.insert(0, 'subID', subID)

        # 3. 添加到列表
        all_subjects_data.append(df_4s)

# 3. 合并所有被试数据并保存

    # 将列表中的 DataFrame 上下拼接 (axis=0)
final_df = pd.concat(all_subjects_data, axis=0, ignore_index=True)

    # 设置输出文件名
output_csv_path = "./Queue_MDD_reho_4S456Parcels.csv"

    # 保存为 CSV
    # index=False 表示不保存 pandas 自动生成的 0,1,2... 索引列
final_df.to_csv(output_csv_path, index=False, na_rep='n/a')


print("处理完成！")
print(f"共包含 {len(final_df)} 个被试。")
print(f"结果已保存至: {output_csv_path}")

