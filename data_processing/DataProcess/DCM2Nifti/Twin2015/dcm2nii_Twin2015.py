import glob
import os
from tqdm import tqdm


inpath = '/Volumes/SeagateBackupPlusDrive/TWIN_IPCAS2015005/'
foldername = os.listdir(inpath)
for i in tqdm(foldername):
    outpath = '/Volumes/qingchen/out_new/' + i
    print('outpath-', outpath)
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    else:
        continue

    # T1path = inpath + i + '/scans/3'
    # print('datapath-', T1path)
    # if not os.path.exists(T1path):
    #     print('no exists path-', T1path)
    #     print('this-', i, 'no 3')
    #     continue
    # cmd = 'dcm2niix'+' -z y -o '+outpath+' '+ T1path
    # print('cmd-', cmd)
    # os.system(cmd)
    #
    # T1path_300 = inpath + i + '/scans/300'
    # print('datapath-', T1path_300)
    # if not os.path.exists(T1path_300):
    #     print('no exists path-', T1path_300)
    #     print('this-', i, 'no 300')
    #     continue
    # cmd = 'dcm2niix' + ' -z y -o ' + outpath + ' ' + T1path_300
    # print('cmd-', cmd)
    # os.system(cmd)
    print('===========================5================================')
    funpath_5 = inpath + i + '/scans/5'
    if not os.path.exists(funpath_5):
        print('#######################'+i+ '--5' )
        continue
    #dcm2niix -f "%f_%p_%t_%s" -p y -z y -o "/Users/qingchen/Desktop" "/Volumes/SeagateBackupPlusDrive/TWIN_IPCAS2015005/IPCAS2015005_sub001/scans/1/DICOM"
    #cmd = 'dcm2niix -f' + ' "%f_%p_%t_%s" -p y -z y -o ' +'\"' +outpath + '\" ' +'\"' + funpath_5+'\"'
    cmd = 'dcm2niix -f' + ' "%f_%p_%t_%s" -p y -z y -o ' +'\"' +outpath + '\" ' +'\"' + funpath_5+'\"'

    print(cmd)

    os.system(cmd)
    print('=========================5-done==================================')
    exit()
    print('===========================6================================')
    funpath_6 = inpath + i + '/scans/6'
    if not os.path.exists(funpath_6):
        print('#######################' + i + '--6')
        continue
    #dcm2niix -f "%f_%p_%t_%s" -p y -z y -o "/Users/qingchen/Desktop" "/Volumes/SeagateBackupPlusDrive/TWIN_IPCAS2015005/IPCAS2015005_sub001/scans/1/DICOM"
    cmd = 'dcm2niix -f' + ' %f_%p_%t_%s -p y -z y ' + outpath + ' ' + funpath_6
    os.system(cmd)
    print('=========================6-done==================================')


    print('===========================7================================')
    funpath_7 = inpath + i + '/scans/7'
    if not os.path.exists(funpath_7):
        print('#######################' + i + '--7')
        continue
    cmd = 'dcm2niix -f' + ' %f_%p_%t_%s -p y -z y ' + outpath + ' ' + funpath_7
    os.system(cmd)
    print('=========================7-done==================================')


    print('=============================8==============================')
    funpath_8 = inpath + i + '/scans/8'

    if not os.path.exists(funpath_8):
        print('#######################' + i + '--8')
        continue
    cmd = 'dcm2niix -f' + ' %f_%p_%t_%s -p y -z y ' + outpath + ' ' + funpath_8

    os.system(cmd)

    print('=========================8-done==================================')


    print('===========================3================================')
    funpath_3 = inpath + i + '/scans/3'
    if not os.path.exists(funpath_3):
        print('#######################' + i + '--3')
        continue

    cmd = 'dcm2niix -f' + ' %f_%p_%t_%s -p y -z y ' + outpath + ' ' + funpath_3

    os.system(cmd)
    print('=========================3-done==================================')

    exit()