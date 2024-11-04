import glob
import os
from shutil import copy

path = '/Volumes/QCII/CHCP_BIDS/*'

sub = glob.glob(path)

for i in sub:
    id = i[-8:]
    print('-------------->',id)
    tp = '/Volumes/QCII/CHCP_BIDS_fMRI_sMRI/' + id + '/anat'
    if not os.path.exists(tp):
        os.mkdir(tp)
    func = glob.glob(i+'/anat/*_T1w*')
    for j in func:
        copy(j,tp)


