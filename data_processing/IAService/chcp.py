import os.path
from shutil import copytree
import glob

file = glob.glob('/n07dat01/OpenData/CHCP/*')
a = ['/n07dat01/OpenData/CHCP/CHCP_STIM','/n07dat01/OpenData/CHCP/CHCP_subjects_information.xlsx','/n07dat01/OpenData/CHCP/CHCP_task_EVs.docx']
for i in file:

    if i in a:
        continue
    subid = i[-4:]
    if os.path.exists('/n01dat01/kkwang/CHCP_rfmri_t1w/' + subid):
        continue
    rest1_ap = i + '/rfMRI_REST1_AP'
    rest1_pa = i + '/rfMRI_REST1_PA'

    rest2_ap = i + '/rfMRI_REST2_AP'
    rest2_pa = i + '/rfMRI_REST2_PA'

    t1w = i + '/T1w_MPR1'

    tp = '/n01dat01/kkwang/CHCP_rfmri_t1w/'+subid
    if os.path.exists(rest1_ap):
        copytree(rest1_ap, tp + '/rfMRI_REST1_AP')
    if os.path.exists(rest1_pa):
        copytree(rest1_pa, tp + '/rfMRI_REST1_PA')
    if os.path.exists(rest2_ap):
        copytree(rest2_ap, tp + '/rfMRI_REST2_AP')
    if os.path.exists(rest2_pa):
        copytree(rest2_pa, tp + '/rfMRI_REST2_PA')
    if os.path.exists(t1w):
        copytree(t1w, tp + '/T1w_MPR1')


