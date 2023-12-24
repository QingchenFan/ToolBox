import nibabel as nib
import scipy.io as scio
import numpy as np
# imagedata = nib.load('./FCMap_sub-47021.nii').get_fdata()
# print(imagedata.shape)
#
# matdata = scio.loadmat('./roiMatrix_test.mat')['data']
# print(matdata.shape)
#
# imagedata = np.reshape(imagedata, (1, 64 * 64 * 33))
# print(imagedata.shape)
#
# meanroi_img = np.transpose(imagedata)
# Corr = np.corrcoef(imagedata, matdata)
# print(Corr)
# Corr = Corr[0, 1]
# print(Corr)

# a = np.array([2, 1, 7, 5])
# b = np.array([1, 3, 5, 6])
#
# res = np.corrcoef(a,b)
# print(res)
# print(res[0,1])

a = np.random.randint(low=1, high=10, size=(3, 4, 2, 3))

print(a)

b = np.array(a).transpose( 3, 0, 1, 2,)

print(b.shape)
print(b)