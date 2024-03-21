import glob
import os.path
from shutil import copy

path = glob.glob('/home/zhouyuan/Documents/Datafc/20231014150026/nifti/V1/*')
path = glob.glob('/Volumes/QC/Data_13_5/SourceData/Data_135/nifti/V1/*')

for i in path:
    print('i--',i)
    if 'HC' in i :
        subid = i[-7:-2]
        funcAPpath = glob.glob(i+'/*Functional*AP*.nii')
        funcPApath = glob.glob(i+'/*Functional*PA*.nii')
        funcAPJSONpath = glob.glob(i+'/*Functional*AP*.json')
        funcPAJSONpath = glob.glob(i+'/*Functional*PA*.json')
        T1wpath = glob.glob(i+'/*t1*.nii')
        T1wJSONpath = glob.glob(i + '/*t1*.json')

        newpath = '/home/zhouyuan/Documents/Datafc/BrainProject_bids/'+'sub-'+subid
        newpath = '/Volumes/QC/Data_13_5/Data135_BIDS/V1/HC/'+'sub-'+subid
        if not os.path.exists(newpath):
            os.mkdir(newpath)

        funpath = newpath + '/func'
        t1wpath = newpath + '/anat'

        if not os.path.exists(funpath):
            os.mkdir(funpath)
        if not os.path.exists(t1wpath):
            os.mkdir(t1wpath)
        if len(funcAPpath) != 0:
            copy(funcAPpath[0],funpath+'/sub-'+subid+'_task-rest_acq-ap_run-1_bold.nii')
            copy(funcAPJSONpath[0], funpath + '/sub-' + subid + '_task-rest_acq-ap_run-1_bold.json')
        else:
            print('No funcAP：',i)

        if len(funcPApath) != 0:
            copy(funcPApath[0], funpath + '/sub-' + subid + '_task-rest_acq-pa_run-1_bold.nii')
            copy(funcPAJSONpath[0], funpath + '/sub-' + subid + '_task-rest_acq-pa_run-1_bold.json')
        else:
            print('No funcPA：',i)

        if len(T1wpath) != 0 :
            copy(T1wpath[0],t1wpath+'/sub-'+subid+'_T1w.nii')
            copy(T1wJSONpath[0], t1wpath + '/sub-' + subid + '_T1w.json')
        else:
            print('No T1w：', i)



    if 'MDD' in i:
        subid = i[-8:-2]
        funcAPpath = glob.glob(i+'/*Functional*AP*.nii')
        funcPApath = glob.glob(i+'/*Functional*PA*.nii')
        funcAPJSONpath = glob.glob(i+'/*Functional*AP*.json')
        funcPAJSONpath = glob.glob(i+'/*Functional*PA*.json')
        T1wpath = glob.glob(i+'/*t1*.nii')
        T1wJSONpath = glob.glob(i + '/*t1*.json')

        newpath = '/home/zhouyuan/Documents/Datafc/BrainProject_bids/'+'sub-'+subid
        newpath = '/Volumes/QC/Data_13_5/Data135_BIDS/V1/MDD/'+'sub-'+subid

        if not os.path.exists(newpath):
            os.mkdir(newpath)

        funpath = newpath + '/func'
        t1wpath = newpath + '/anat'

        if not os.path.exists(funpath):
            os.mkdir(funpath)
        if not os.path.exists(t1wpath):
            os.mkdir(t1wpath)

        if len(funcAPpath) != 0:
            copy(funcAPpath[0], funpath + '/sub-' + subid + '_task-rest_acq-ap_run-1_bold.nii')
            copy(funcAPJSONpath[0], funpath + '/sub-' + subid + '_task-rest_acq-ap_run-1_bold.json')
        else:
            print('No funcAP：', i)

        if len(funcPApath) != 0:
            copy(funcPApath[0], funpath + '/sub-' + subid + '_task-rest_acq-pa_run-1_bold.nii')
            copy(funcPAJSONpath[0], funpath + '/sub-' + subid + '_task-rest_acq-pa_run-1_bold.json')
        else:
            print('No funcPA：', i)

        if len(T1wpath) != 0:
            copy(T1wpath[0], t1wpath + '/sub-' + subid + '_T1w.nii')
            copy(T1wJSONpath[0], t1wpath + '/sub-' + subid + '_T1w.json')
        else:
            print('No T1w：', i)