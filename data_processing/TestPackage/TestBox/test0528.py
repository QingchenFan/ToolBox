import nibabel as nib

import scipy.io as scio

a = nib.load('/Users/qingchen/Desktop/abcd_template_matching_avg_number_of_networks_thresh2.0.dlabel.nii')
data = a.get_fdata()

print(data)
scio.savemat('/Users/qingchen/Desktop/avg_number2.mat',{'avg_number2':data})