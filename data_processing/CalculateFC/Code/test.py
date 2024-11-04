import nibabel as nib
from scipy.io import savemat
import numpy as np
# a = nib.load('./sub-06202_task-rest_space-fsLR_atlas-Schaefer417_den-91k_measure-pearsoncorrelation_conmat.pconn.nii').get_fdata()
from nilearn import surface
from nilearn import datasets


dataset = '/Users/qingchen/Documents/code/Data/roi_fc/sub-0062_task-rest_space-fsLR_den-91k_desc-denoisedSmoothed_bold.dtseries.nii'
cifti = nib.load(dataset)
cifti_data = cifti.get_fdata()
cifti_hdr = cifti.header
# axes = [cii.header.get_axis(i) for i in range(cii.ndim)]
# print(cii.header.get_axis(1))
# print(list(axes[1].iter_structures()))
def volume_from_cifti(data, axis):
    assert isinstance(axis, nib.cifti2.BrainModelAxis)
    data = data.T[axis.volume_mask]                          # Assume brainmodels axis is last, move it to front
    volmask = axis.volume_mask                               # Which indices on this axis are for voxels?
    vox_indices = tuple(axis.voxel[axis.volume_mask].T)      # ([x0, x1, ...], [y0, ...], [z0, ...])
    vol_data = np.zeros(axis.volume_shape + data.shape[1:],  # Volume + any extra dimensions
                        dtype=data.dtype)
    vol_data[vox_indices] = data                             # "Fancy indexing"
    return nib.Nifti1Image(vol_data, axis.affine).to_filename('./subcor.nii.gz')             # Add affine for spatial interpretation

axes = [cifti_hdr.get_axis(i) for i in range(cifti.ndim)]
a = volume_from_cifti(cifti_data, axes[1])

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

a_left = surf_data_from_cifti(cifti_data, axes[1], 'CIFTI_STRUCTURE_CORTEX_LEFT')
a_right = surf_data_from_cifti(cifti_data, axes[1], 'CIFTI_STRUCTURE_CORTEX_RIGHT')




