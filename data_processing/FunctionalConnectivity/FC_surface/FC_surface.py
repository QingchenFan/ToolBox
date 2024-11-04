import glob
import os
import numpy as np
import nibabel as nib
from nilearn.maskers import NiftiMasker
from scipy.io import savemat
from nilearn import plotting
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

def loadData(datapath):
    cifti = nib.load(datapath)
    cifti_data = cifti.get_fdata()
    cifti_hdr = cifti.header
    axes = [cifti_hdr.get_axis(i) for i in range(cifti.ndim)]
    return cifti,cifti_data, cifti_hdr, axes

def plot_correlation_matrix(correlation_matrix,labels):
    plotting.plot_matrix(
        correlation_matrix,
        figure=(10, 8),
        labels=labels,
        vmax=0.8,
        vmin=-0.8,
        #title="Confounds",
        reorder=True,
    )
    plotting.show()
datapath = '/Users/qingchen/Documents/code/Data/FC/sub-06202_task-rest_space-fsLR_den-91k_desc-denoisedSmoothed_bold.dtseries.nii'

cifti, cifti_data, cifti_hdr, axes = loadData(datapath)
axes = [cifti_hdr.get_axis(i) for i in range(cifti.ndim)]

Subcortical_Data = volume_from_cifti(cifti_data, axes[1])

a_left = surf_data_from_cifti(cifti_data, axes[1], 'CIFTI_STRUCTURE_CORTEX_LEFT')
a_right = surf_data_from_cifti(cifti_data, axes[1], 'CIFTI_STRUCTURE_CORTEX_RIGHT')
cortex_data = np.concatenate((a_left, a_right), axis=0)

template = '/Users/qingchen/Documents/code/Data/FC/Schaefer2018_400Parcels_7Networks_order.dlabel.nii'
label = nib.load(template).get_fdata()

roilist = []
for i in range(1,401):
    index = np.where(label == i)
    roi = cortex_data[index[1],: ]
    roilist.append(np.mean(roi, axis=0))


roiMatrix = np.array(roilist)
print(roiMatrix.shape)
resFC = np.corrcoef(roiMatrix)

savemat('./FC.mat',{'data':resFC})
print(resFC.shape)

# 画图
# from nilearn import datasets
# schaefer_400 = datasets.fetch_atlas_schaefer_2018(n_rois=400, resolution_mm=2)  # 加载 schaefer template (可设置参数选择合适的模板)，可以选择nilearn自带template，也可以自己加载所需要的template
# atlas_filename = schaefer_400.maps                                              # atlas_filename  模板数据的路径 string
# labels = schaefer_400.labels
#
# plot_correlation_matrix(resFC,labels)