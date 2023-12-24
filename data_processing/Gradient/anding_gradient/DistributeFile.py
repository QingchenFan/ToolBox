import glob
import os.path

import scipy.io as scio
from scipy.io import savemat

path = '/Volumes/qingchen/anding/gradient/all_gradient_pca.mat'
alldata = scio.loadmat(path)
fcpath = '/Volumes/qingchen/anding/gradient/hc_v2/ROISignals_SurfLHSurfRHVolu_FunSurfWCF/*.mat'
filename = glob.glob(fcpath)
hcv2_data = alldata['data'][0:75, :]

for i , j in zip(hcv2_data, filename):
    id = j[-13:-4]

    savemat('/Volumes/qingchen/anding/gradient/PCA/hc_v2/gradients_aligned/'+id+'_gradient.mat', {'data': i})

#
# #path = '/Volumes/qingchen/anding/gradient/all_gradient_global.mat'
# alldata = scio.loadmat(path)
# fcpath = '/Volumes/qingchen/anding/gradient/hc001_50_v01/ROISignals_SurfLHSurfRHVolu_FunSurfWglobalCF/*.mat'
# filename = glob.glob(fcpath)
# hcv2_data = alldata['data'][75:125, :]
#
# for i , j in zip(hcv2_data, filename):
#     id = j[-13:-4]
#     savemat('/Volumes/qingchen/anding/gradient/PCA/hc001_50_v01/gradients_aligned/'+id+'_gradient.mat', {'data': i})
#
#
# #path = '/Volumes/qingchen/anding/gradient/all_gradient_global.mat'
# alldata = scio.loadmat(path)
# fcpath = '/Volumes/qingchen/anding/gradient/hc051_114_v01/ROISignals_SurfLHSurfRHVolu_FunSurfWglobalCF/*.mat'
# filename = glob.glob(fcpath)
# hcv2_data = alldata['data'][125:189, :]
#
# for i , j in zip(hcv2_data, filename):
#     id = j[-13:-4]
#     savemat('/Volumes/qingchen/anding/gradient/PCA/hc051_114_v01/gradients_aligned/'+id+'_gradient.mat', {'data': i})


# #path = '/Volumes/qingchen/anding/gradient/all_gradient_global.mat'
# alldata = scio.loadmat(path)
# fcpath = '/Volumes/qingchen/anding/gradient/MDDv1/ROISignals_SurfLHSurfRHVolu_FunSurfWglobalCF/*.mat'
# filename = glob.glob(fcpath)
# hcv2_data = alldata['data'][189:326, :]
# for i , j in zip(hcv2_data, filename):
#     id = j[-14:-4]
#     savemat('/Volumes/qingchen/anding/gradient/PCA/MDDv1/gradients_aligned_global/'+id+'_gradient.mat', {'data': i})
#
#
# #path = '/Volumes/qingchen/anding/gradient/all_gradient_global.mat'
# alldata = scio.loadmat(path)
# fcpath = '/Volumes/qingchen/anding/gradient/MDDv2/ROISignals_SurfLHSurfRHVolu_FunSurfWglobalCF/*.mat'
# filename = glob.glob(fcpath)
# hcv2_data = alldata['data'][326:389, :]
# for i , j in zip(hcv2_data, filename):
#     id = j[-14:-4]
#     savemat('/Volumes/qingchen/anding/gradient/PCA/MDDv2/gradients_aligned_global/'+id+'_gradient.mat', {'data': i})

