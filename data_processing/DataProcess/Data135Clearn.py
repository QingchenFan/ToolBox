import glob
import os
from shutil import copytree, copy

path = '/Volumes/QCII/Data135_processed/xcpd_out_mdd/xcp_d/*/func/sub*denoisedSmoothed_bold.dtseries.nii'

box = glob.glob(path)


for i in box:
    print(i)
    subid = i.split('/')[6]
    print(subid)
    name = i.split('/')[8]
    print(name)
    tp = '/Volumes/QCI/NormativeModel/Data135/MDD/' + subid

    if not os.path.exists(tp):
        os.mkdir(tp)

    copy(i, tp + '/' + name)