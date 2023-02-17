from shutil import copy
import os
import glob
import json

BIDSpath = '/home/cuizaixu_lab/fanqingchen/DATA/data/HCPD/HCPD_BIDS/'
FuncPath = '/home/cuizaixu_lab/fanqingchen/DATA/data/HCPD/rsfMRI_20210514'

FuncName = os.listdir(FuncPath)   # 获取FunImgName路径下所有文件的文件名
if not os.path.exists(BIDSpath):
    os.mkdir(BIDSpath)
    for i in FuncName:
        tem = i[0:10]  # Take the three-digit number of the file name
        new_name = 'sub-' + tem
        print(i + '--' + new_name)  # Calibration
        if not os.path.exists(BIDSpath + new_name):
            os.mkdir(BIDSpath + new_name)  # Create a file for each subject
            os.mkdir(BIDSpath + new_name + '/' + 'anat')
            os.mkdir(BIDSpath + new_name + '/' + 'func')

funcfile = glob.glob('/home/cuizaixu_lab/fanqingchen/DATA/data/HCPD/rsfMRI_20210514/*/MNINonLinear/Results/rfMRI_REST1_AP/*')
for i in funcfile:
    fname = i[62:73]
    funcName = 'sub-'+fname
    funcaimpath = BIDSpath+funcName+'/func/'
    copy(i, funcaimpath+funcName+'_'+'task-rest'+'_bold.nii.gz')
    jsonStruc = {
        "RepetitionTime": 2,
        "SkullStripped": "false",
        "TaskName": "rest"
    }
    box = json.dumps(jsonStruc, indent=1)
    with open(funcaimpath+funcName+'_'+'task-rest'+ '_bold.json', 'w', newline='\n') as f:
        f.write(box)

#-------------------------------------------------------------------------------------------------------------------------
T1wPath = '/home/cuizaixu_lab/fanqingchen/DATA/data/HCPD/sMRI_unprocessed_20210514'
T1wName = os.listdir(T1wPath)

for i in T1wName:
    if i not in FuncName:
        continue
    tname = i[0:10]
    t1wname = 'sub-'+tname
    t1aimpath = BIDSpath + t1wname + '/anat/'

    t1wfile = glob.glob('/home/cuizaixu_lab/fanqingchen/DATA/data/HCPD/sMRI_unprocessed_20210514/'+i+'/unprocessed/T1w_MPR_vNav_4e_e1e2_mean/*.nii.gz')

    copy(t1wfile[0], t1aimpath+t1wname+'T1w.nii')
    jsonStruc = {'SkullStripped': 'false',
                 'Project': 'IPCASTest'}
    box = json.dumps(jsonStruc, indent=1)
    with open(t1aimpath + t1wname + '_T1w.json', 'w', newline='\n') as f:
        f.write(box)

