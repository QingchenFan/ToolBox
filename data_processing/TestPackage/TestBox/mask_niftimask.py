import plotly.io
from nilearn.image import smooth_img
from nilearn.maskers import NiftiSpheresMasker
import nibabel as nib
from nilearn.maskers import NiftiMasker
import pandas as pd
import glob
import numpy as np
from nilearn import image
from nilearn import datasets
''''
    测试niftimask函数，想验证一下
'''

def volume_from_cifti(data, axis):
    assert isinstance(axis, nib.cifti2.BrainModelAxis)
    data = data.T[axis.volume_mask]                          # Assume brainmodels axis is last, move it to front
    volmask = axis.volume_mask                               # Which indices on this axis are for voxels?
    vox_indices = tuple(axis.voxel[axis.volume_mask].T)      # ([x0, x1, ...], [y0, ...], [z0, ...])
    vol_data = np.zeros(axis.volume_shape + data.shape[1:],  # Volume + any extra dimensions
                        dtype=data.dtype)
    vol_data[vox_indices] = data                             # "Fancy indexing"
    return nib.Nifti1Image(vol_data, axis.affine)


datapath = '/Users/qingchen/Documents/code/Data/roi_fc/sub-MDD003_task-rest_space-fsLR_den-91k_desc-denoisedSmoothed_bold.dtseries.nii'
masker = '/Users/qingchen/Documents/code/Data/roi_fc/amygdala_mask_2/ROI_Amygdala_CM_R_MNI.nii.gz'


cifti = nib.load(datapath)
cifti_data = cifti.get_fdata()
cifti_hdr = cifti.header

axes = [cifti_hdr.get_axis(i) for i in range(cifti.ndim)]
votexdata = volume_from_cifti(cifti_data, axes[1])


amgydala_masker = NiftiMasker(
    mask_img=masker,
    #standardize="zscore_sample",
    #standardize_confounds="zscore_sample",
    t_r=None,
    memory_level=1,
    verbose=0,
)
brain_time_series = amgydala_masker.fit_transform(votexdata)
mask_img = amgydala_masker.mask_img_

from nilearn import datasets


voxeldata = '/Users/qingchen/Documents/code/Data/roi_fc/sub-0062_task-rest_space-MNI152NLin6Asym_res-2_desc-denoisedSmoothed_bold.nii.gz'



from nilearn.image.image import mean_img
from nilearn.plotting import plot_roi
from nilearn import plotting
# calculate mean image for the background
mean_func_img = mean_img(voxeldata)
print(mean_func_img.shape)
plot_roi(mask_img, mean_func_img, display_mode="y", cut_coords=4, title="Mask")
print(brain_time_series.shape)
amgydala_time_series_mean = brain_time_series.mean(axis=1)
plotting.show()
#
# maskerdata = nib.load(masker).get_fdata()
# votexdata_m = votexdata.get_fdata()
# BOLDdata = smooth_img(votexdata, fwhm=0)  # 91x109x91x478 1*1*1
# print('Bolddatashape-', BOLDdata.shape)
#
# reslist = []
# for j in range(0, BOLDdata.shape[3]):
#     res = maskerdata * image.index_img(BOLDdata, j).get_fdata()
#     reslist.append(res)
# r = np.array(reslist).transpose(1, 2, 3, 0)
# print(r.shape)
#
