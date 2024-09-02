import nibabel as nib
import numpy as np
from scipy import io
"""
    Map the functional connectivity (FC) onto the brain and visualize it using Workbench.
"""

labelpath = '/Users/qingchen/Documents/code/Data/FC/Schaefer2018_400Parcels_17Networks_order.dscalar.nii'
labeldata = nib.load(labelpath)

data = io.loadmat('/Users/qingchen/Documents/code/Data/FC/amgydala_allvertex.mat')['data']

#data = np.nan_to_num(data)

scalar_axis=nib.cifti2.cifti2_axes.ScalarAxis(['val'])
brain_model_axis=labeldata.header.get_axis(1)

val_head=nib.cifti2.Cifti2Header.from_axes((scalar_axis, brain_model_axis))
nib.Cifti2Image(data, val_head, labeldata.nifti_header, labeldata.extra, labeldata.file_map).to_filename('./fcvalue2.dscalar.nii')
exit()
# TODO: 未运行成功，需调试
#------------dlabel-----------------#
dlabelpath = '/Users/qingchen/Documents/code/Data/FC/Schaefer2018_400Parcels_17Networks_order.dlabel.nii'
dlabeldata = nib.load(labelpath)


data = io.loadmat('/Users/qingchen/Documents/code/Data/FC/amgydala_allvertex.mat')['data']

print(dir(nib.cifti2.cifti2_axes.LabelAxis))
scalar_axis=nib.cifti2.cifti2_axes.LabelAxis(['label'])
brain_model_axis=dlabeldata.header.get_axis(1)
print(brain_model_axis)
val_head=nib.cifti2.Cifti2Header.from_axes((scalar_axis, brain_model_axis))
nib.Cifti2Image(data, val_head, dlabeldata.nifti_header, labeldata.extra, labeldata.file_map).to_filename('./fcvalue.dlabel.nii')
