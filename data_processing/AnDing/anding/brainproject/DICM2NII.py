import glob
import os

from tqdm import tqdm

inpath = '/Volumes/qingchen/AnDing/DICOM/BD/*'
foldername = glob.glob(inpath)

for i in tqdm(foldername):
    a = i.split('/')[6][0:8]
    b = i.split('/')[6][9:12]

    if b in ['V01']:
        id = 'sub-'+ a + 'V01'
    else:
        id = 'sub-' + a + 'V03'
    outpath = '/Volumes/qingchen/AnDing/Datafc/BD/'+ id
    print('outpath-', outpath)
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    cmd = 'dcm2niix'+' -z y -o '+outpath+' '+ i
    print('cmd-', cmd)
    os.system(cmd)
    print('=========================done==================================')
