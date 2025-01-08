import os
import glob
from shutil import copy

path = '/Volumes/qingchen/Images_QC/Datafc/HC/'

file = os.listdir(path)

for i in file:
    # T1image = glob.glob(path + i + '/*t1*.nii.gz')
    # T1json = glob.glob(path + i + '/*t1_sag*.json')
    #
    # Tnewpath = '/Volumes/qingchen/AnDing/BIDS/MDD/'+ i +'/anat'
    # if not os.path.exists(Tnewpath):
    #     os.makedirs(Tnewpath)
    #
    # copy(T1image[0], Tnewpath+'/'+ i +'_T1w.nii.gz')
    # copy(T1json[0], Tnewpath + '/' + i + '_T1w.json')
    #
    fnewpath = '/Volumes/qingchen/AnDing/BIDS/HC/' + i + '/func'
    #
    # if not os.path.exists(fnewpath):
    #     os.makedirs(fnewpath)
    #
    # Boldimage = glob.glob(path + i +'/*bold_resting*.nii.gz')
    # Boldjson = glob.glob(path + i + '/*bold_resting*.json')
    #
    # copy(Boldimage[0], fnewpath+'/'+i+'_task-rest_bold.nii.gz')
    # copy(Boldjson[0], fnewpath + '/' + i + '_task-rest_bold.json')
    #

    #
    # if not os.path.exists(fnewpath):
    #     os.makedirs(fnewpath)
    #
    # FMap = glob.glob(path + i +'/*face_matching_ap*.nii.gz')
    # print('-FMap-', FMap)
    # FMapjson = glob.glob(path + i + '/*face_matching_ap*.json')
    #
    # copy(FMap[0], fnewpath+'/'+i+'_task-facematching_run-1_acp-ap_bold.nii.gz')
    # copy(FMapjson[0], fnewpath + '/' + i + '_task-facematching_run-1_acp-ap_bold.json')
    #
    # FMpa = glob.glob(path + i + '/*face_matching_pa*.nii.gz')
    # print('-FMpa-', FMpa)
    # FMpajson = glob.glob(path + i + '/*face_matching_pa*.json')
    #
    # copy(FMpa[0], fnewpath + '/' + i + '_task-facematching_run-2_acp-pa_bold.nii.gz')
    # copy(FMpajson[0], fnewpath + '/' + i + '_task-facematching_run-2_acp-pa_bold.json')
    #
    # UG = glob.glob(path + i + '/*ultimate_game*.nii.gz')
    # print('-UG-', UG)
    # UGjson = glob.glob(path + i + '/*ultimate_game*.json')
    #
    # copy(UG[0], fnewpath + '/' + i + '_task-ultimategame_bold.nii.gz')
    # copy(UGjson[0], fnewpath + '/' + i + '_task-ultimategame_bold.json')
    #
    #
    longr1 = glob.glob(path + i + '/*bold_longresting1*.nii.gz')
    print(len(longr1))
    if len(longr1) == 0:
        continue
    print(i)
    longrjson1 = glob.glob(path + i + '/*bold_longresting1*.json')

    copy(longr1[0], fnewpath + '/' + i + '_task-longresting_run-1_bold.nii.gz')
    copy(longrjson1[0], fnewpath + '/' + i + '_task-longresting_run-1_bold.json')

    longr2 = glob.glob(path + i + '/*bold_longresting2*.nii.gz')
    longrjson2 = glob.glob(path + i + '/*bold_longresting2*.json')

    copy(longr2[0], fnewpath + '/' + i + '_task-longresting_run-2_bold.nii.gz')
    copy(longrjson2[0], fnewpath + '/' + i + '_task-longresting_run-2_bold.json')




