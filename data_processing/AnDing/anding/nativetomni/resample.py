from nilearn.datasets import (
    load_mni152_template,
    load_sample_motor_activation_image,
)
import nibabel as nib
#template = load_mni152_template(resolution=1)
template = './MNI152_T1_1mm_brain.nii.gz'
sourcedata = './MDD002/MDD002_t1_mprage_sag_p2_iso_20210520203739_3.nii'

from nilearn.image import resample_to_img

resampled_stat_img = resample_to_img(sourcedata, template)
nib.Nifti1Image(resampled_stat_img.get_fdata(), resampled_stat_img.affine, resampled_stat_img.header).to_filename('./MDD02_t1_2.nii')
exit()
