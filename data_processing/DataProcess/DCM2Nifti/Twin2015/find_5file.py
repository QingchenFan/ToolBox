import os
import glob
path = '/Volumes/qingchen/out/'

filename = os.listdir(path)

for i in filename:

    path_5 = path + i
    file_1 = glob.glob(path_5 + '/5_*.nii.gz')
    file_2 = glob.glob(path_5 + '/scans_*_5.nii.gz')


    if not file_1 and not file_2:
        print('========='+i+'=======')
