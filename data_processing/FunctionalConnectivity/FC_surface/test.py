import glob
import os
import numpy as np
import nibabel as nib
from nilearn.maskers import NiftiMasker
from scipy.io import savemat
from nilearn import plotting

# path = '/Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_freesurfer/fsaverage/fsaverage_LR32k/fsaverage.R.BN_Atlas.32k_fs_LR.label.gii'
# a = nib.load(path)
# dataa = a.darrays[0].data
# print(dataa.shape)
# savemat('r.mat', {'dataR': dataa})
#
# path = '/Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_freesurfer/fsaverage/fsaverage_LR32k/fsaverage.L.BN_Atlas.32k_fs_LR.label.gii'
# b = nib.load(path)
# datab = b.darrays[0].data
# print(datab.shape)
# savemat('l.mat', {'dataL': datab})

# niipath = '/Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_246_2mm.nii.gz'
# c = nib.load(niipath)
# datac = c.get_fdata()
# datac = datac.flatten()
# print(datac.shape)
# np.savetxt('matrix.txt', datac)
# savemat('bn.mat', {'datac': datac})

# def subc_timeseries(data,atlaspath):
#
#     atlasData = nib.load(atlaspath).get_fdata()
#
#     atlasData = np.reshape(atlasData, (1, 91 * 109 * 91), order='F')
#
#     data = np.reshape(data, (data.shape[3], 91 * 109 * 91), order='F')
#
#     roilist = []
#     for r in range(211, 247):
#         index = np.where(atlasData == r)
#         roi = data[:, index[1]]  # 将第r个脑区中的voxel 数据（时间序列）提取
#
#         # 统计体素个数
#         totalvoxel = roi.shape[1] if roi.shape[1] > 0 else 1
#
#         sum = np.sum(roi, axis=1)
#
#         roiBoldsum = sum / totalvoxel
#
#         roilist.append(roiBoldsum)
#
#     subctimeseries = np.array(roilist)
#     print('subctimeseries.shape-', subctimeseries.shape)
#     subcFC = np.corrcoef(subctimeseries)
#     return subcFC,subctimeseries
#
# atlaspath = '/Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_246_2mm.nii.gz'
# dpath = '/Users/qingchen/Desktop/sub-HC001_task-rest_acq-ap_run-1_space-MNI152NLin6Asym_res-2_desc-denoisedSmoothed_bold.nii.gz'
# data = nib.load(dpath).get_fdata()
# subcFC , subctimeseries = subc_timeseries(data,atlaspath)
# savemat('./subcFC2.mat', {'data2': subcFC})
# savemat('./subctimeseries2.mat', {'data2': subctimeseries})
np.random.seed(0)
a = np.random.randint(0,10,size=(3, 2, 4))
b = np.random.randint(0,10,size=(3, 2, 4, 2))
c = b.transpose(3, 0, 1, 2)
print(a)
print(b)
print(c)
aa = np.reshape(a,(1, 3 * 2 * 4), order='F')
bb = np.reshape(b,(2, 3 * 2 * 4), order='F')
cc = np.reshape(c,(2, 3 * 2 * 4), order='F')
print(aa)
print(bb)
print(cc)