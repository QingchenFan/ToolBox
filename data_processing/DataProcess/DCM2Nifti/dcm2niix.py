import os
from tqdm import tqdm
import scipy.io

# intpath = '/Users/qingchen/Documents/Datafc/ChenJieRawData/'
# outpath = '/Users/qingchen/Documents/Datafc/c_nii/'
#
# foldername = os.listdir(intpath)
# for i in foldername:
#     datapath = intpath + i
#     print('datapath-', datapath)
#
#     out_pathnew = outpath + 'sub-' + i[-4:]
#     print('out_path-', out_pathnew)
#
#     if not os.path.exists(out_pathnew):
#         os.makedirs(out_pathnew)
#
#     cmd = 'dcm2niix' +' -z y -f %p_%t_%s -o '+out_pathnew +' '+ datapath
#     print('cmd-', cmd)
#
#     os.system(cmd)
inpath = '/Volumes/SeagateBackupPlusDrive/TWIN_IPCAS2015005/'
foldername = os.listdir(inpath)
for i in tqdm(foldername):
    datapath = inpath + i + '/scans/'
    print('datapath-', datapath)
    outpath = '/Volumes/SeagateBackupPlusDrive/Public_Data/out/'+ i
    print('outpath-', outpath)
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    else:
        continue
    cmd = 'dcm2niix'+' -z y -o '+outpath+' '+ datapath
    print('cmd-', cmd)
    os.system(cmd)
    print('=========================done==================================')

