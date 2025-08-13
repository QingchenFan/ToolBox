import pandas as pd

MDDData= pd.read_csv('/Volumes/QC/INT/INT_BN246_HC135BP_BP135MDD/Results/INTvalue_HC.csv')
#MDDData = pd.read_csv('/Volumes/QC/INT/INT_BN246_HC135BP_BP135MDD/Results/INTvalue_MDD.csv')
# 检查空值
nan_rows = MDDData.isnull().any(axis=1)
print(nan_rows)
# 获取包含空值的行的索引
nan_indices = MDDData[nan_rows].index

# 打印包含空值的行的索引位置
print("索引位置包含空值的行：")
print(nan_indices)