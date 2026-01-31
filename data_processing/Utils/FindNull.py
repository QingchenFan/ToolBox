# import pandas as pd
#
# MDDData= pd.read_csv('/Volumes/QC/INT/INT_BN246_HC135BP_BP135MDD/Results/INTvalue_HC.csv')
# #MDDData = pd.read_csv('/Volumes/QC/INT/INT_BN246_HC135BP_BP135MDD/Results/INTvalue_MDD.csv')
# # 检查空值
# nan_rows = MDDData.isnull().any(axis=1)
# print(nan_rows)
# # 获取包含空值的行的索引
# nan_indices = MDDData[nan_rows].index
#
# # 打印包含空值的行的索引位置
# print("索引位置包含空值的行：")
# print(nan_indices)

import os
import glob
file = '/Volumes/ZLabData/BrainProject/brainprojectII/fmriprep/HC_DZ/sourcedata/freesurfer/sub-*/surf/lh.pial'

data = glob.glob(file)

for i in data:

    subID = i.split('/')[-3]
    # 检查文件是否存在
    if os.path.exists(i):
        # 获取文件大小（单位：字节）
        file_size_bytes = os.path.getsize(i)

        # 转换为更易读的单位（如 KB、MB）
        file_size_kb = file_size_bytes / 1024  # 千字节
        file_size_mb = file_size_kb / 1024     # 兆字节
        if file_size_kb == 0:
            print(subID)

    else:
        print(f"文件不存在：{i}")
