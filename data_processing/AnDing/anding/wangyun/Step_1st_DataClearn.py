import glob
from shutil import copy
import pandas as pd

labelpath = '/Users/qingchen/Documents/Dailywork/Lab/AnDing/wangyun_nucleusaccumben/MDD46HC58.csv'

subID = pd.read_csv(labelpath)['subID']
for i in subID:
    print('id>>>>',i)
    nsubID = 'sub-' + i
    if 'HC' in nsubID:
        dpath = '/Volumes/QCII/Data135_processed/xcpd_out_globalsignal_hc/xcp_d/'+nsubID+'/func/*ap_run-1_space-fsLR_den-91k_desc-denoisedSmoothed_bold.dtseries.nii'
    else:
        dpath = '/Volumes/QCII/Data135_processed/xcpd_out_globalsignal_mdd/xcp_d/'+nsubID+'/func/*ap_run-1_space-fsLR_den-91k_desc-denoisedSmoothed_bold.dtseries.nii'

    fdata = glob.glob(dpath)
    if len(fdata) == 0:
        print('No data>>>>>>>',i)
        continue
    dataName = fdata[0].split('/')[-1]
    tarpath = '/Volumes/QCI/wangyun/Data/'+dataName

    copy(fdata[0],tarpath)
