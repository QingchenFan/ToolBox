import glob
import os.path
from shutil import copy

funImgpath = glob.glob('/Users/qingchen/Documents/code/Data/anding_service/youngHC/FunImg/*')

for i in funImgpath:
    id = i[-5:]
    funimage = glob.glob(i + '/*nii')
    funjson = glob.glob(i + '/*json')

    tp = '/Users/qingchen/Documents/code/Data/anding_service/BIDS/youngHC/'+ 'sub-'+ id
    if not os.path.exists(tp):
        os.mkdir(tp)

    funcpath = tp + '/func'
    if not os.path.exists(funcpath):
        os.mkdir(funcpath)

    copy(funimage[0],funcpath + '/sub-'+ id + '_task-rest_bold.nii.gz')
    copy(funjson[0], funcpath + '/sub-' + id + '_task-rest_bold.json')

T1Imgpath = glob.glob('/Users/qingchen/Documents/code/Data/anding_service/youngHC/T1Img/*')

for j in T1Imgpath:
    id = j[-5:]
    T1image = glob.glob(j + '/*nii')
    T1json = glob.glob(j + '/*json')

    tp = '/Users/qingchen/Documents/code/Data/anding_service/BIDS/youngHC/'+ 'sub-'+ id
    if not os.path.exists(tp):
        os.mkdir(tp)

    anatpath = tp + '/anat'
    if not os.path.exists(anatpath):
        os.mkdir(anatpath)

    copy(T1image[0],anatpath + '/sub-'+ id + '_T1w.nii.gz')
    copy(T1json[0], anatpath + '/sub-' + id + '_T1w.json')
