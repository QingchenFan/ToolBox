import nibabel as nib
import numpy as np
import pandas as pd

# TODO: 真实代码
path = './Gordon333_FreesurferSubcortical.32k_fs_LR.dlabel.nii'
Gordondataimage = nib.load(path)
print(Gordondataimage)
Gordondata = Gordondataimage.get_fdata()
weightpath = './GeneralSum.csv'
weightdata = pd.read_csv(weightpath)
for i in range(1, 353):
    index = np.where(Gordondata == i)
    Gordondata[index[0], index[1]] = weightdata['sum'][i-1]

# nib.Cifti2Image(Gordondata,  nifti_header=Gordondataimage.nifti_header, file_map=Gordondataimage.file_map).to_filename('./gordon.dscalar.nii')
# exit()
scalar_axis=nib.cifti2.cifti2_axes.ScalarAxis(['val'])
brain_model_axis=Gordondataimage.header.get_axis(1)
print(brain_model_axis)
val_head=nib.cifti2.Cifti2Header.from_axes((scalar_axis, brain_model_axis))
nib.Cifti2Image(Gordondata, val_head, Gordondataimage.nifti_header, Gordondataimage.extra, Gordondataimage.file_map).to_filename('./gordonweight2.dscalar.nii')
