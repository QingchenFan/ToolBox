import nibabel as nib

maskpath = '/Volumes/QCI/wangyun/mask/NAc_subregions/rLH_rsFC_core.nii'
masklabeldata = nib.load(maskpath)
NAcmask = masklabeldata.get_fdata()
NAcmask[NAcmask < 0] = 0
NAcmask[NAcmask > 0] = 1.0
nib.Nifti1Image(NAcmask, masklabeldata.affine, masklabeldata.header).to_filename('/Volumes/QCI/wangyun/mask/NAc_subregions/new2_rLH_rsFC_core.nii')
print('NAc mask done!')