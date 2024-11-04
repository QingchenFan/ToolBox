import nibabel as nib
import numpy as np

# 读取cifti文件
from scipy.io import savemat

cifti_file = './sub-MDD001_task-rest_space-fsLR_den-91k_desc-denoisedSmoothed_bold.dtseries.nii'
cifti_img = nib.load(cifti_file).get_fdata()
cifti_img = cifti_img[:, 0:64984]
print('cifti_img-', cifti_img.shape)
# 获取数据数组和标签数组
cifti_label_path = './Schaefer2018_400Parcels_7Networks_order.dlabel.nii'
cifti_label = nib.load(cifti_label_path).get_fdata()
print(cifti_label.shape)

# 获取ROI标签列表
roilist = []
for r in range(1, 401):
    index = np.where(cifti_label == r)
    roi = cifti_img[:, index[1]]  # ROI内所有的voxel
    totalvoxel = roi.shape[1]
    sum = np.sum(roi, axis=1)

    roiBoldsum = sum / totalvoxel

    roilist.append(roiBoldsum)
roiMatrix = np.array(roilist)
resFC = np.corrcoef(roiMatrix)
savemat('./roiMatrix0504.mat', {'data': resFC})
