import os.path
from shutil import copy
import glob
import pandas as pd

data = glob.glob("/Volumes/ZLabData/BrainProject/brainproject_II/XCPD/MDD_xcpd_HX/xcp_d/sub-*V01/func/sub-*V01_task-rest_space-fsLR_den-91k_reho.dscalar.nii")

for i in data:
    subID = i.split("/")[-3]
    filename = i.split("/")[-1]
    print(subID)
    print(filename)
    newpath = "/Volumes/QC/Data/To_LMH/MDD_HX/"+filename
    copy(i, newpath)
