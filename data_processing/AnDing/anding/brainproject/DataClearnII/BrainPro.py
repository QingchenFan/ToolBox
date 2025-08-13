import os
import glob
from shutil import copy

path = '/home/zhouyuan/Fan/20250409175237/data_796/02*'

file = os.listdir(path)

for i in file:
    subID = i.split('/')[1]
    print(i)
    print(subID)
    #sMRI
    T1image = glob.glob(path + i + '/*t1*.nii.gz')
    T1json = glob.glob(path + i + '/*t1_sag*.json')

    Tnewpath = '/Volumes/qingchen/AnDing/BIDS/MDD/'+ i +'/anat'
    if not os.path.exists(Tnewpath):
        os.makedirs(Tnewpath)

    copy(T1image[0], Tnewpath+'/'+ i +'_T1w.nii.gz')
    copy(T1json[0], Tnewpath + '/' + i + '_T1w.json')
    #BOLD
    fnewpath = '/Volumes/qingchen/AnDing/BIDS/HC/' + i + '/func'

    if not os.path.exists(fnewpath):
        os.makedirs(fnewpath)

    Boldimage = glob.glob(path + i +'/*bold_resting*.nii.gz')
    Boldjson = glob.glob(path + i + '/*bold_resting*.json')

    copy(Boldimage[0], fnewpath+'/'+i+'_task-rest_bold.nii.gz')
    copy(Boldjson[0], fnewpath + '/' + i + '_task-rest_bold.json')

    #Fieldmap







