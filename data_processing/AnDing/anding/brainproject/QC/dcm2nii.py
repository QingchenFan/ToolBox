import os
from tqdm import tqdm
import glob
import scipy.io
path = '/home/zhouyuan/dicom/*/*CBPD_bold_FM_*'

data = glob.glob(path)

for i in tqdm(data):

    subId = i.split('/')[-2]
    outpath = '/home/zhouyuan/fan/QC/'+ subId
    print('outpath-', outpath)
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    else:
        continue
    cmd = 'dcm2niix'+' -z y -o '+outpath+' '+ i
    print('cmd-', cmd)
    os.system(cmd)
    print('=========================done==================================')
    exit()
