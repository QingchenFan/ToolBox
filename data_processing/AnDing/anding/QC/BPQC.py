import glob
import pandas as pd

# 设置文件路径
path = "/Users/qingchen/Documents/Dailywork/Lab/AnDing/BrainProjectQC_UG_GM/QC_CSV/*/*UG*.csv"
data_files = glob.glob(path)

if data_files:
    first_file = data_files[0]
    first_df = pd.read_csv(first_file)
    # 初始化结果DataFrame，使用第一个文件的列名作为列
    res_df = pd.DataFrame(columns=first_df['Key'])
    print(res_df)

# 初始化一个空的列表用于存储每个文件的DataFrame
all_data = []

# 遍历所有文件
for file in data_files:
    # 获取 subID (即文件夹的名称，倒数第二个路径部分)
    subID = file.split('/')[-2]
    print(f"Processing: {subID}")

    # 读取CSV文件
    df = pd.read_csv(file)
    print(df)
    # 读取文件的第二行 (iloc[1])，并转换为Series
    data_row = df.iloc[:,1]
    print(data_row)
    # 将 subID 插入到该行的最前面
    data_row = pd.Series([subID], index=['subID'])._append(data_row)

    # 将处理好的行数据添加到all_data列表中
    all_data.append(data_row)


# 将所有行数据转换为一个DataFrame
res_df = pd.DataFrame(all_data)

# 保存结果到CSV文件

res_df.to_csv('./UG.csv', index=False)


