import nibabel as nib
from scipy.io import savemat
import numpy as np
t = nib.load('./AAL.nii.gz')
#print(data)
data = t.get_fdata()
savemat('./aaldata.mat', {'data': data})
index = np.where(data == 2501)

data[data != 2501] = 0
data[data == 2501] = 1


nib.Nifti1Image(data, t.affine, t.header).to_filename(
    'mask.nii.gz')


res = nib.load('./mask.nii.gz').get_fdata()
index = np.where(data == 1)
print(index)