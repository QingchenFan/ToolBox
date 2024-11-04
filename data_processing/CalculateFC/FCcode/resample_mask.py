import nibabel as nib
import glob
from nilearn.image import resample_to_img

sourcemask = '/Users/qingchen/Documents/code/Data/roi_fc/amygdala_mask/ROI_Amygdala_CM_L_MNI.nii'
tar = '/Users/qingchen/Documents/Data/template/MNITemplate-master/inst/extdata/MNI152_T1_2mm_Brain_Mask.nii.gz'

outdata = resample_to_img(source_img=sourcemask, target_img=tar, interpolation='continuous')
nib.Nifti1Image(outdata.get_fdata(), outdata.affine, outdata.header).to_filename('/Users/qingchen/Documents/code/Data/roi_fc/amygdala_mask_2/ROI_Amygdala_CM_L_MNI.nii.gz')

