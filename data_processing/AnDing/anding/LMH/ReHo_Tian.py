import glob
import pandas as pd
import os

# 1. 设置文件路径模式
# 注意：确保这里的路径与你的实际路径一致
base_path = "/Volumes/QCII/duilie_processed/duilie_HC1_67_MDD_XCPD_Volume/xcpd_out/xcp_d/"
search_pattern = os.path.join(base_path, "sub-MDD*/func/sub-*_task-rest_acq-ap_run-1_space-MNI152NLin6Asym_atlas-4S456Parcels_reho.tsv")
# 获取所有主文件列表
files_4s = glob.glob(search_pattern)
print(files_4s)


all_subjects_data = []

# 2. 循环处理每个被试
for file_path_4s in files_4s:
    try:
        subID = file_path_4s.split("/")[-3]

        # --- 构建 Tian 图谱文件的路径 ---
        file_path_tian = file_path_4s.replace("atlas-4S456Parcels", "atlas-Tian")

        # 检查 Tian 文件是否存在
        if not os.path.exists(file_path_tian):
            print(f"警告: 找不到被试 {subID} 的 Tian 文件，跳过。路径: {file_path_tian}")
            continue

        # --- 读取并处理数据 ---

        # 1. 读取 4S456Parcels 文件
        # Pandas 会自动识别 'n/a' 为 NaN (缺失值)
        df_4s = pd.read_csv(file_path_4s, sep='\t')

        # 截取前 400 列 (Schaefer 400)
        df_4s_cortical = df_4s.iloc[:, :400]

        # 2. 读取 Tian 文件
        df_tian = pd.read_csv(file_path_tian, sep='\t')

        # 3. 横向拼接
        combined_row = pd.concat([df_4s_cortical.reset_index(drop=True),
                                  df_tian.reset_index(drop=True)], axis=1)

        # 4. 插入 subID 到第一列
        combined_row.insert(0, 'subID', subID)

        # 添加到列表
        all_subjects_data.append(combined_row)

    except Exception as e:
        print(f"处理被试 {subID} 时出错: {e}")

# 3. 合并所有被试并保存
if all_subjects_data:
    final_df = pd.concat(all_subjects_data, axis=0, ignore_index=True)

    # 打印结果预览
    print("-" * 30)
    print("处理完成！")
    print(f"总被试数: {len(final_df)}")
    print(f"总列数: {final_df.shape[1]} (1 subID + 400 Cortical + {final_df.shape[1] - 401} Subcortical)")

    # 检查是否有 NaN 值 (在内存中预览)
    if final_df.isnull().values.any():
        print("注意: 数据中包含 'n/a' (NaN) 值，将在保存时保留。")

    # 保存结果
    output_file = "./Queue_MDD_ReHo_Schaefer400_Tian.csv"

    # 【关键修改】：添加 na_rep='n/a' 参数
    # 这会强制将表格中的空值(NaN)在保存的文件里写成 "n/a"
    final_df.to_csv(output_file, index=False, na_rep='n/a')

    print(f"结果已保存至: {output_file} (空值已填充为 'n/a')")
else:
    print("未提取到任何数据，请检查路径是否正确。")