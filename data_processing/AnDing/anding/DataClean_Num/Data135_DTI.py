import os
import glob
from shutil import copy
#Data 135 #
# path = '/Volumes/QCII/Data135/SourceData/Data_135/nifti/V3/MDD*_3'
#
# file = glob.glob(path)
#
# box = []
# for i in file:
#     DTI = glob.glob(i + '/*DTI_AP*.nii')
#     if len(DTI) == 0:
#         continue
#     box.append(DTI[0])
# print(len(box))
#-----------------------
#Queue #
path = '/Volumes/QCII/duilie/duilie_2024512/nifti/V28/YDMDD*'

file = glob.glob(path)

box = []
for i in file:
    DTI = glob.glob(i + '/*DTI_AP*.nii*')
    if len(DTI) == 0:
        continue
    box.append(DTI[0])
print(len(box))