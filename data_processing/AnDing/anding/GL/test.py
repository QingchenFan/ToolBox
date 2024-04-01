import nibabel as nib
import numpy as np
import pandas as pd
from scipy.io import savemat,loadmat

import pandas as pd

# labelpath = '/Users/qingchen/Documents/code/Data/FC/Schaefer2018_400Parcels_7Networks_order.dlabel.nii'
# label = nib.load(labelpath).get_fdata()
#
# data = loadmat('./amgydala_allvertex.mat')['data']
#
#
# roilist = []
# dic = {}
# for i in range(1,4):
#
#     index = np.where(label == i)
#
#     roi = data[:,index[1]]
#
#     dic[i] = roi[0,:]
#
# df = pd.DataFrame.from_dict(dic, orient='index').transpose()

# import pandas as pd
# import pandas as pd
#
# my_dict = {'a': [1, 2, 3, 4], 'f': [6, 2, 8, 9], 'e': [1, 1, 1, 1]}
#
# df = pd.DataFrame.from_dict(my_dict, orient='index')
# df.index.name = 'subject'
#
#
# my_dict2 = {'a': 1, 'b': 6, 'd': 9,'e': 100}
#
# df2 = pd.DataFrame.from_dict(my_dict2, orient='index')
# df2.index.name = 'subject'
# merged_df = pd.merge(df, df2, on='subject', how='inner')
# print(merged_df)
# concatenated_df = pd.concat([df, df2], axis=1, join='inner')
# print(concatenated_df)
# if not concatenated_df.empty:
#     concatenated_df.to_csv('./text.csv',)

# data = loadmat('./sub-HC008_AMGYDALA_CM_L_FC.mat')['data']
# nan_indices = np.argwhere(np.isnan(data))
#
# print(nan_indices[:,1])
# a = nan_indices[:,1]
# print(len(a))
#
#
# labelpath = '/Users/qingchen/Documents/code/Data/FC/Schaefer2018_400Parcels_17Networks_order.dlabel.nii'
# label = nib.load(labelpath).get_fdata()
# # print(label.shape)
# b = np.argwhere(label == 0)
# res = b[:,1]
# print(res)
# print(len(res))
#
# for i,j in enumerate(a,res):
#     print(i,'--',j)
import pandas as pd
path = '/Users/qingchen/Desktop/results_CM_R_list.csv'
pd.set_option('display.max_rows', None)  # 设置为None以显示所有行
pd.set_option('display.max_columns', None)
a = pd.read_csv(path)
list = []
list.append(a.iloc[1,:])
