import nibabel as nib
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
from scipy.io import savemat
from nilearn.image import resample_to_img

# -- Resample --
# sourcedata = './sub-MDD001_task-rest_space-MNI152NLin6Asym_desc-denoisedSmoothed_bold.nii.gz'
# targetdata = './Schaefer2018_400Parcels_7Networks_order_FSLMNI152_2mm.nii.gz'
# outdata = resample_to_img(source_img=sourcedata, target_img=targetdata)
# nib.Nifti1Image(outdata.get_data(), outdata.affine, outdata.header).to_filename('./sub-MDD001_task-rest_space-MNI152NLin6Asym_desc-denoisedSmoothed_bold_re.nii.gz')

template = './Schaefer2018_400Parcels_7Networks_order_FSLMNI152_2mm.nii.gz'
shcaData = nib.load(template)
templateData = shcaData.get_fdata()


templateData = np.reshape(templateData, (1, 91 * 109 * 91), order='F')


boldpath = './sub-MDD001_task-rest_space-MNI152NLin6Asym_res-2_desc-denoisedSmoothed_bold.nii.gz'
bolddata = nib.load(boldpath).get_fdata()
savemat('./bolddata.mat', {'data': bolddata})
print(bolddata.shape)
bolddata = np.reshape(bolddata, (158, 91 * 109 * 91), order='F')
print(bolddata)

roilist = []
for r in range(1, 401):
    index = np.where(templateData == r)


    roi = bolddata[:, index[1]]  # 将第r个脑区中的voxel 数据（时间序列）提取

    totalvoxel = roi.shape[1]    # 统计体素个数

    sum = np.sum(roi, axis=1)
    roiBoldsum = sum / totalvoxel
    print('roiBoldsum.shape-', roiBoldsum.shape)

    roilist.append(roiBoldsum)
    print('roilist-len', len(roilist))
roiMatrix = np.array(roilist)
savemat('./roiMatrix.mat', {'data': roiMatrix})
resFC = np.corrcoef(roiMatrix)
print('--resFC--', resFC.shape)
z_res = np.arctanh(resFC)

savemat('./Schaefer400_7FC.mat', {'data': resFC})
savemat('./fisherzSchaefer400_7FC.mat', {'data': z_res})