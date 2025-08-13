import os
import glob
path = "/Volumes/QCII/Data135/Data135_BIDS/V1/HC/*/anat/*.nii"

file = glob.glob(path)

for i in file:
    a = "scp "+i+" root@211.87.253.101:/home/kkwang/xicang/Data/Data135/"

    os.system(a)
    exit()
