
import pandas as pd

# 加载数据
df_first = pd.read_csv('/Users/qingchen/Documents/Data/zhouLabData/brainproject/临床数据/II/HC_FirstData.csv')
df_all = pd.read_csv('/Users/qingchen/Documents/Data/zhouLabData/brainproject/临床数据/II/HC_AllData.csv',encoding='UTF-8-SIG')

# 获取 FirstData.csv 中 subID 列的值
ids_to_remove = df_first['subID'].tolist()

# 从 AllDat.csv 中剔除这些被试
df_filtered = df_all[~df_all['subID'].isin(ids_to_remove)]

# 将结果保存为新的 CSV 文件
csv_path = '/Users/qingchen/Documents/Data/zhouLabData/brainproject/临床数据/II/New_HCData.csv'
df_filtered.to_csv(csv_path, index=False, encoding='UTF-8-SIG')