import nibabel as nib

from nilearn.image import resample_to_img

sourcedatapath = './Sub_0001_WIP_3DT1W_TFE_sSAG_CS3_20211218183239_301_Crop_1_n4_mni_seg_post_inverse.nii.gz'
targetdata = './c_sub_0001_pcereb.nii'
sourcedata = nib.load(sourcedatapath)
print(sourcedata)
data = sourcedata.get_data()
data[data == 20] =0
data[(data < 20) & (data>0) ] =1
nib.Nifti1Image(data, sourcedata.affine, sourcedata.header).to_filename(
    './cerbmask.nii.gz')
maskpath = './cerbmask.nii.gz'
outdata = resample_to_img(source_img=maskpath, target_img=targetdata, interpolation='nearest')
nib.Nifti1Image(outdata.get_data(), outdata.affine, outdata.header).to_filename(
    './cerbmask2.nii.gz')
