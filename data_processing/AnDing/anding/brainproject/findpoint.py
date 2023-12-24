import glob
import nibabel as nib

path = '/Users/qingchen/Documents/Data/brianproject/facemapping1/FunRaw/*'

sub = sorted(glob.glob(path))

for i in sub:
    funpath = glob.glob(i + '/*.nii.gz')
    data = nib.load(funpath[0]).get_fdata()
    print(i)
    print(data.shape[3:4][0])
    if 100 != data.shape[3:4][0]:
         print(i)



