from nilearn.maskers import NiftiSpheresMasker
import nibabel as nib
from nilearn.maskers import NiftiMasker
import pandas as pd
import glob
import numpy as np
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
print(brain_time_series.shape)
amgydala_time_series_mean = brain_time_series.mean(axis=1)


maskerdata = nib.load(masker).get_fdata()
votexdata_m = votexdata.get_fdata()

res = maskerdata * votexdata_m

print(res.shape)
