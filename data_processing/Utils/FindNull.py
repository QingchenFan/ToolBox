import pandas as pd

HCData = pd.read_csv('/Volumes/Images_QC/INT/INT_BN246_HC135BP_allMDD/Results/INTvalue_HC.csv')
MDDData = pd.read_csv('/Volumes/Images_QC/INT/INT_BN246_HC135BP_allMDD/Results/INTvalue_MDD.csv')
# 检查空值
nan_rows = MDDData.isnull().any(axis=1)
print(nan_rows)
# 获取包含空值的行的索引
nan_indices = MDDData[nan_rows].index

# 打印包含空值的行的索引位置
print("索引位置包含空值的行：")
print(nan_indices)