import nibabel as nib

maskpath = '/Users/qingchen/Documents/Dailywork/Lab/AnDing/seedFC/ZY/rAmygdala_BNA.nii'
masklabeldata = nib.load(maskpath)
NAcmask = masklabeldata.get_fdata()
NAcmask[NAcmask < 0] = 0
NAcmask[NAcmask > 0] = 1.0
nib.Nifti1Image(NAcmask, masklabeldata.affine, masklabeldata.header).to_filename('/Users/qingchen/Documents/Dailywork/Lab/AnDing/seedFC/ZY/NewrAmygdala_BNA.nii')
print('NAc mask done!')