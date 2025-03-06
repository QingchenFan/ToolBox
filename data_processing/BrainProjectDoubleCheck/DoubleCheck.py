import pandas as pd

pd.set_option('display.max_rows', None)  # 显示所有行
pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.width', None)  # 自动调整显示宽度
pd.set_option('display.max_colwidth', None)  # 显示完整的列内容

def compare_tables(file_path1, file_path2):
    # 读取第一个 Excel 文件
    df1 = pd.read_excel(file_path1)

    # 读取第二个 Excel 文件
    df2 = pd.read_excel(file_path2)

    AD_num = df1['subID'].shape
    QC_num = df2['subID'].shape
    print(f"anding 被试： {AD_num[0]} 个样本")
    print(f"qc 被试： {QC_num[0]} 个样本")
    # 要对比的列（除了 subID 列）
    AD_columns = [col for col in df1.columns if col != 'subID']
    QC_columns = [col for col in df2.columns if col != 'subID']
    all_list = list(set(AD_columns+QC_columns))
    columns_to_compare = [elem for elem in AD_columns if elem in QC_columns]
    diff_elements = [elem for elem in all_list if elem not in columns_to_compare]

    print('检查量表：', columns_to_compare)
    print('未检测量表：', diff_elements)
    print('全部量表：', all_list)
    for column in columns_to_compare:
        # 基于 subID 列合并两个数据框
        merged_df = pd.merge(df1[['subID', column]], df2[['subID', column]], on='subID', suffixes=('_anding', '_qc'))

        # 查找不一致的数据
        inconsistent_data = []
        for index, row in merged_df.iterrows():

            subID = row['subID']
            # 对比两列数据是否一致
            if row[column + '_anding'] != row[column + '_qc']:
                inconsistent_row = {
                   'subID': subID,
                   f'{column}_anding': row[column + '_anding'],
                   f'{column}_qc': row[column + '_qc']
                }
                inconsistent_data.append(inconsistent_row)

        if inconsistent_data:
            result_df = pd.DataFrame(inconsistent_data)
            print(f"{column} 列不一致的数据：")
            print(result_df)
        else:
            print(f"{column} 列的数据全部一致")

# 调用函数，传入两个 Excel 文件的路径
AD_path = '/Users/qingchen/Documents/Data/zhouLabData/brainproject/DoubleCheck/AD_PD_24w.xlsx'
QC_path = '/Users/qingchen/Documents/Data/zhouLabData/brainproject/DoubleCheck/QC_PD_24w.xlsx'
compare_tables(AD_path, QC_path)