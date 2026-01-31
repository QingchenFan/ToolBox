import os.path

import pandas as pd
from shutil import copy
path = "/Volumes/QC/Data/To_LMH/BN_Precise.csv"

data = pd.read_csv(path)

subID = data['subID'].tolist()

for i in subID:
    print(i)
    map = "/Volumes/ZLabData/BrainProject/brainproject_I/xcpd_out_PD/xcp_d/"+i+"/func/"+i+"_task-rest_acq-ap_run-1_space-MNI152NLin6Asym_res-2_reho.nii.gz"
    if not os.path.isfile(map):
        print(' -----no-----', i)
        continue
    filename = i+"_task-rest_acq-ap_run-1_space-MNI152NLin6Asym_res-2_reho.nii.gz"
    newpath = "/Volumes/QC/Data/To_LMH/BN_Precise/"+filename

    copy(map, newpath)


