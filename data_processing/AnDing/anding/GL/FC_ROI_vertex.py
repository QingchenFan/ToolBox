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


p = '/Volumes/QC/Dataprocess/hcout_xcpd/xcp_d/sub-*'
masker = '/Users/qingchen/Documents/code/Data/roi_fc/amygdala_mask_2/ROI_Amygdala_SF_R_MNI.nii.gz'
#mask = '/Users/qingchen/Documents/code/Data/roi_fc/amygdala_mask/amygdala_l.nii'
box = glob.glob(p)

for i in box :
    if not os.path.isdir(i):
        continue
    print(i)
    subId = i[-9:]  #  HC  -9:0  MDD -10:0

    datapath = i + '/func/sub*-denoisedSmoothed_bold.dtseries.nii'
    data = glob.glob(datapath)

    cifti = nib.load(data[0])
    cifti_data = cifti.get_fdata()
    cifti_hdr = cifti.header

    axes = [cifti_hdr.get_axis(i) for i in range(cifti.ndim)]
    a = volume_from_cifti(cifti_data, axes[1])

    amgydala_masker = NiftiMasker(
        mask_img=masker,
        # standardize="zscore_sample",
        # standardize_confounds="zscore_sample",
        t_r=None,
        memory_level=1,
        verbose=0,
    )
    amgydala_time_series = amgydala_masker.fit_transform(a)
    print('amgydala_time_series:',amgydala_time_series.shape)

    amgydala_time_series_mean = amgydala_time_series.mean(axis=1)


    CIFTI_STRUCTURE_CORTEX_LEFT_RIGHT = cifti_data[:,0:59412]
    print('--a--',CIFTI_STRUCTURE_CORTEX_LEFT_RIGHT.shape)
    print('--b--',amgydala_time_series_mean.shape)
    res = []
    for j in range(0,CIFTI_STRUCTURE_CORTEX_LEFT_RIGHT.shape[1]):
        corr= np.corrcoef(amgydala_time_series_mean,CIFTI_STRUCTURE_CORTEX_LEFT_RIGHT[:,j:j+1].T)

        res.append(corr[0,1])

    data_corr = np.array(res)
    savemat('/Volumes/QC/HC_Amygdala_SF_R_FC/'+subId+'_AMGYDALA_SF_R_FC.mat', {'data': data_corr})
    #savemat('/Volumes/QC/HC_Amygdala_L_FC/'+subId+'_AMGYDALA_L_FC.mat', {'data': data_corr})
    exit()





