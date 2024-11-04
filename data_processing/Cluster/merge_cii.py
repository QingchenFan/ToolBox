import glob
import os
import nibabel as nib

data = glob.glob('/Users/qingchen/Documents/code/Data/test_dtseries/*.dscalar.nii')
cmd = 'wb_shortcuts -cifti-concatenate /Users/qingchen/Documents/code/Data/test_dtseries/merged.dscalar.nii'
for i in data :
     cmd = cmd +' '+i
print(cmd)
#os.system(cmd)
dp = '/Users/qingchen/Documents/code/Data/test_dtseries/merged_new.dscalar.nii'
a = nib.load(dp)
data = a.get_fdata()

print(data.shape)
exit()

import pandas as pd
import scipy.io as sio

# 读取 CSV 文件为 pandas DataFrame
dataframe = pd.read_csv('/Users/qingchen/Documents/code/Data/test_dtseries/designmatrix.csv',header=None)
print(dataframe)
# 将 DataFrame 转换为字典
data_dict = dataframe.to_numpy()
print(data_dict.shape)
# 保存为 MATLAB .mat 文件
sio.savemat('ddm.mat', {'matrix': data_dict})