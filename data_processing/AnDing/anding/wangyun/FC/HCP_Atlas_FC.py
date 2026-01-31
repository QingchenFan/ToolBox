import glob
import pandas as pd
import os

# ==========================================
# 1. 设置文件路径（请根据实际情况修改）
# ==========================================
tsv_path = "/Volumes/ZLabData/BrainProject/brainproject_II/XCPD/MDD_xcpd_HX/xcp_d/sub-*V01/func/sub-*_task-rest_space-fsLR_atlas-Glasser_measure-pearsoncorrelation_conmat.tsv"
databox = glob.glob(tsv_path)
target_regions = [
    'Right_7Am', 'Left_7Am',
    'Right_7Pm', 'Left_7Pm',
    'Right_5mv', 'Left_5mv',
    'Right_PCV',  'Left_PCV',
    'Right_23c',  'Left_23c',
    'Right_31a',  'Left_31a',
    'Right_31pd', 'Left_31pd',
    'Right_7m',   'Left_7m',
    'Right_23d',  'Left_23d',
    'Right_31pv', 'Left_31pv',
    'Right_d23ab','Left_d23ab',
    'Right_v23ab','Left_v23ab',
    'Right_RSC',  'Left_RSC',
    'Right_33pr', 'Left_33pr',
    'Right_POS2', 'Left_POS2'
]

for i in databox:
    subID = i.split('/')[-3]
    output_csv = "/Volumes/QC/Data/To_WY/MDD/"+subID+"_regions_correlation.csv"

    df = pd.read_csv(i, sep='\t', index_col=0)  # 第一列是行名（脑区名）
    if df.isna().any().any() or (df == 'n/a').any().any():
        print("\n⚠️ 警告：数据中存在 n/a 或 NaN 值！")
        print("以下脑区行中包含 n/a：")
        na_rows = df.index[df.apply(lambda row: row.astype(str).str.contains('n/a').any(), axis=1)]
        for row in na_rows:
            print(f"  - {row}")
        print("n/a - subID：", subID)

    found_regions = [r for r in target_regions if r in df.index]
    missing_regions = [r for r in target_regions if r not in df.index]

    selected_df = df.loc[found_regions].copy()
    columns_to_fill = ['Right_H', 'Left_H']

    for col in columns_to_fill:
        if col in selected_df.columns:
            selected_df[col] = 'n/a'
            print(f"  已将列 {col} 全部填充为 'n/a'")

    print('数据维度：', selected_df.shape)

    selected_df.to_csv(output_csv, encoding='utf-8-sig')  # utf-8-sig 防止中文乱码（Windows Excel）





