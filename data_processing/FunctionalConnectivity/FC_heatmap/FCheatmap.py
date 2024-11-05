import nibabel as nib
import seaborn as sns
import scipy.io as sio
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
from scipy.io import savemat
from string import ascii_letters
def find_martrix_min_value(data_matrix):
    '''
    功能：找到矩阵最小值
    '''
    new_data = []
    for i in range(len(data_matrix)):
        new_data.append(min(data_matrix[i]))
    print('data_matrix min:', min(new_data))


def find_martrix_max_value(data_matrix):
    '''
    功能：找到矩阵最大值
    '''
    new_data = []
    for i in range(len(data_matrix)):
        new_data.append(max(data_matrix[i]))
    print('data_matrix max:', max(new_data))

# data = nib.load('./sub-MDD001_task-rest_space-fsLR_atlas-Schaefer417_den-91k_measure-pearsoncorrelation_conmat.pconn.nii')
#
# fcdata = data.get_data()
#
# savemat('./schaefer400FC.mat', {'data': fcdata})
#
#
#
# find_martrix_min_value(fcdata)
# find_martrix_max_value(fcdata)
#
# #z_res = stats.zscore(fcdata, axis=None, ddof=1)
# z_res = np.arctanh(fcdata)
# savemat('./fisher_r-z_schaefer400FC.mat', {'data': z_res})
#
# #
# find_martrix_min_value(z_res)
# find_martrix_max_value(z_res)

matdata = sio.loadmat('/Volumes/QCI/NormativeModel/Data135/HC/BN246_FC/sub-HC001_FC.mat')
data = matdata['data']

find_martrix_max_value(data)

# Compute the correlation matrix
mask = np.triu(np.ones_like(data, dtype=bool))
resdata = pd.DataFrame(data)
cx = sns.heatmap(data,
                 xticklabels=False, yticklabels=False, cmap='Blues', annot=False,
                 #mask=mask
                #cbar_kws ={'format': '%.1f','ticks': [-1.0, 0.0, 1.0]}
                )    # xticklabels/yticklabels x轴的titel  "Spectral"
cx.tick_params(labelsize=100, left=False, bottom=False)  # 控制去掉小刻度线
cbar_3 = cx.collections[0].colorbar
cbar_3.ax.tick_params(labelsize=12, left=False, right=False)

plt.show()
