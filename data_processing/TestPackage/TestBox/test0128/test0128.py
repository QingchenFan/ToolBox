import nibabel as nib

path = '/Users/qingchen/Documents/code/Data/FC/Schaefer2018_400Parcels_17Networks_order.dlabel.nii'

data = nib.load(path).get_fdata()

print(data)