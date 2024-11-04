import nibabel as nib
from scipy.io import savemat

# a = nib.load('/Users/qingchen/Documents/code/INT/intrinsic-timescales-main/dataTest/sub-MDD127_task-rest_acq-pa_run-1_space-fsLR_den-91k_desc-denoisedSmoothed_bold.dtseries.nii')
#
# res = a.get_fdata()

#savemat('./sub-MDD127.mat', {'data': res})

b = nib.load('/Volumes/QCI/GL/HC_fmriprep_out/sub-HC001/anat/sub-HC001_space-MNI152NLin6Asym_res-2_desc-brain_mask.nii.gz')
res = b.get_fdata()
print(res.shape)