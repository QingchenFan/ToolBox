import glob
import os
import numpy as np
import nibabel as nib
from nilearn.maskers import NiftiMasker
from scipy.io import savemat
from nilearn.image.image import mean_img
def volume_from_cifti(data, axis):
    assert isinstance(axis, nib.cifti2.BrainModelAxis)
    data = data.T[axis.volume_mask]                          # Assume brainmodels axis is last, move it to front
    volmask = axis.volume_mask                               # Which indices on this axis are for voxels?
    vox_indices = tuple(axis.voxel[axis.volume_mask].T)      # ([x0, x1, ...], [y0, ...], [z0, ...])
    vol_data = np.zeros(axis.volume_shape + data.shape[1:],  # Volume + any extra dimensions
                        dtype=data.dtype)
    vol_data[vox_indices] = data                             # "Fancy indexing"
    return nib.Nifti1Image(vol_data, axis.affine)
def surf_data_from_cifti(data, axis, surf_name):
    assert isinstance(axis, nib.cifti2.BrainModelAxis)
    for name, data_indices, model in axis.iter_structures():  # Iterates over volumetric and surface structures
        if name == surf_name:                                 # Just looking for a surface
            data = data.T[data_indices]                       # Assume brainmodels axis is last, move it to front
            vtx_indices = model.vertex                        # Generally 1-N, except medial wall vertices
            surf_data = np.zeros((vtx_indices.max() + 1,) + data.shape[1:], dtype=data.dtype)
            surf_data[vtx_indices] = data
            return surf_data
    raise ValueError(f"No structure named {surf_name}")


p = '/Volumes/QCI/wangyun/Data/*'
# TODO
masker = '/Volumes/QCI/wangyun/mask/NAc_subregions/new_rRH_rsFC_shell.nii'  # new_rLH_rsFC_core.nii /new_rLH_rsFC_shell.nii /new_rRH_rsFC_core.nii /new_rRH_rsFC_shell.nii
#mask = '/Users/qingchen/Documents/code/Data/roi_fc/amygdala_mask/amygdala_l.nii'
box = glob.glob(p)
print(box)
for i in box :
    print(i)
    subId = i.split('/')[-1].split('_')[0]

    cifti = nib.load(i)
    cifti_data = cifti.get_fdata()
    cifti_hdr = cifti.header

    axes = [cifti_hdr.get_axis(n) for n in range(cifti.ndim)]
    a = volume_from_cifti(cifti_data, axes[1])
    NAc_masker = NiftiMasker(
        mask_img=masker,
        # standardize="zscore_sample",
        # standardize_confounds="zscore_sample",
        t_r=None,
        memory_level=1,
        verbose=0,
    )
    NAc_time_series = NAc_masker.fit_transform(a)
    print('amgydala_time_series:', NAc_time_series.shape)

    NAc_time_series_mean = NAc_time_series.mean(axis=1)

    a_left = surf_data_from_cifti(cifti_data, axes[1], 'CIFTI_STRUCTURE_CORTEX_LEFT')
    a_right = surf_data_from_cifti(cifti_data, axes[1], 'CIFTI_STRUCTURE_CORTEX_RIGHT')
    CIFTI_STRUCTURE_CORTEX_LEFT_RIGHT = np.concatenate((a_left, a_right), axis=0)
    print('--CIFTI_STRUCTURE_CORTEX_LEFT_RIGHT--', CIFTI_STRUCTURE_CORTEX_LEFT_RIGHT.shape)
    print('--amgydala_time_series_mean--', NAc_time_series_mean.shape)

    res = []
    for j in range(0, CIFTI_STRUCTURE_CORTEX_LEFT_RIGHT.shape[0]):
        corr = np.corrcoef(NAc_time_series_mean, CIFTI_STRUCTURE_CORTEX_LEFT_RIGHT[j:j + 1, :])

        res.append(corr[0, 1])

    data_corr = np.array(res)
    data_corr = np.arctanh(data_corr)

    # TODO
    savemat('/Volumes/QCI/wangyun/NAc_rRH_rsFC_shell_z/'+subId+'_NAc_rRH_rsFC_shell.mat', {'data': data_corr})

