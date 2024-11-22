import glob
import nibabel as nib

data = glob.glob('/Volumes/QCI/ZY/zy_seedFC_all_data135/*.nii.gz')
a = []
for i in data:
    # img = nib.load(i).get_fdata()
    # print(img.shape)
    # exit()
    a.append(i)
print(len(a))