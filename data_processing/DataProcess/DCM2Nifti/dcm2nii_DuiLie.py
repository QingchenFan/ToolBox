import os
import glob
inpath = '/Volumes/QCI/DuiLie_MDD87_143_DICOM/*'
foldername = glob.glob(inpath)

for i in foldername:
    subID = i.split('/')[-1][:8] + 'V01'
    print(subID)

    outpath = '/Volumes/QCI/DuiLie_MDD87_143_nii/'+ i
    print('outpath-', outpath)
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    else:
        continue
    cmd = 'dcm2niix'+' -z y -o '+outpath+' '+ i
    print('cmd-', cmd)
    os.system(cmd)
    print('=========================done==================================')
