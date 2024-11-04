from nilearn.maskers import NiftiSpheresMasker
import nibabel as nib
from nilearn.maskers import NiftiMasker
import pandas as pd
import glob
import numpy as np


votexdata = '/Users/qingchen/Documents/code/Data/roi_fc/sub-0062_task-rest_space-fsLR_den-91k_desc-denoisedSmoothed_bold.dtseries.nii'
voxeldata = '/Users/qingchen/Documents/code/Data/roi_fc/sub-0062_task-rest_space-MNI152NLin6Asym_res-2_desc-denoisedSmoothed_bold.nii.gz'
masker = '/Users/qingchen/Documents/code/Data/roi_fc/amygdala_mask_2/ROI_Amygdala_CM_R_MNI.nii.gz'
a = nib.load(masker).get_fdata()


amgydala_masker = NiftiMasker(
    mask_img=masker,
    #standardize="zscore_sample",
    #standardize_confounds="zscore_sample",
    t_r=None,
    memory_level=1,
    verbose=0,
)
brain_time_series = amgydala_masker.fit_transform(voxeldata)

amgydala_time_series_mean = brain_time_series.mean(axis=1)

