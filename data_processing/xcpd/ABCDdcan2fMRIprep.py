import os
import sys
import glob
import numpy as np
import pandas as pd
import nibabel as nib
import argparse

########################### function
def writejson(data, outfile):
    import json
    with open(outfile, 'w') as f:
        json.dump(data, f)
    return outfile

########################### argparse system
parser = argparse.ArgumentParser(description='dcan 2 fMRIprep')
parser.add_argument('--site', '-s', help='the ID of site', required=True)
parser.add_argument('--run', '-r', help='the ID of site', required=True)
args = parser.parse_args()
site_id = args.site
run_id = args.run
print('site: %s' %(site_id))

################################### main (1):prepare the input data for xcpd
# the directory of site
ABCD_funcdir = '/GPFS/cuizaixu_lab_permanent/Public_Data/ABCD/ABCC/rawdata/rsfMRI/SIEMENS/' + site_id
ABCD_anatdir = '/GPFS/cuizaixu_lab_permanent/xulongzhou/ABCD/ABCD_fMRIprep_anatonly/SIEMENS/' + site_id
ABCD_xcpddir = '/GPFS/cuizaixu_lab_permanent/xulongzhou/ABCD/ABCD_xcpd/SIEMENS/' + site_id
# the directory of subject
subj_list = os.listdir(ABCD_anatdir)
for sub_id in subj_list:
    ses_id = 'ses-baselineYear1Arm1'
    task_id = 'task-rest'
    space_id = 'space-MNI152NLin6Asym_res-2'
    file_title = sub_id + '_' + ses_id + '_' + task_id + '_' + run_id + '_' + space_id
    print('subject: %s' %(file_title))
        
        
    #####set the work path
    rawfunc_dir = ABCD_funcdir + '/'+ sub_id + '/' + ses_id + '/' + 'func' # the folder of fMRI data from minimal preprocess 
    fMRIprep_anat_dir = ABCD_anatdir + '/'+ sub_id + '/' + ses_id + '/' + 'anat' # the folder of preprocessed T1 MRI data
    newfunc_dir = ABCD_xcpddir + '/'+ sub_id + '/' + ses_id + '/' + 'func' # the folder of preprocessed fMRI data after xcpd
    if not os.path.exists(fMRIprep_anat_dir):
        print('missing anat file, skip this subject: %s' %(sub_id))
        continue
    if not os.path.exists(rawfunc_dir):
        print('missing raw fMRI file, skip this subject: %s' %(sub_id))
        continue
    raw_fMRI_path = rawfunc_dir + '/' + sub_id + '_' + ses_id + '_' + task_id + '_' + run_id + '_space-MNI_bold.nii.gz' # raw fMRI file
    if not os.path.exists(raw_fMRI_path):
        print('missing raw fMRI file, skip this subject: %s' %(sub_id))
        continue
    raw_motion_path = rawfunc_dir + '/' + sub_id + '_' + ses_id + '_' + task_id + '_'+ run_id +'_desc-filtered_motion.tsv' # motion file of ABCD dcan style
    if not os.path.exists(raw_motion_path):
        print('missing raw motion file, skip this subject: %s' %(sub_id))
        continue
    fMRIprep_mask_path = glob.glob(fMRIprep_anat_dir + '/' + sub_id + '_' + ses_id + '*' + 'space-MNI152NLin6Asym_res-2_desc-brain_mask.nii.gz') # mask file
    if not os.path.exists(fMRIprep_mask_path[0]):
        print('missing fMRiprep mask file, skip this subject: %s' %(sub_id))
        continue
        
    ######convert the dcan to fMRIprep
    # bold image file
    print('raw fMRI: %s' %(raw_fMRI_path))
    fMRIimg = nib.load(raw_fMRI_path) #load the fMRI data
    TR = nib.load(raw_fMRI_path).header.get_zooms()[-1]  # repetition time
    fMRIdimension = fMRIimg.shape
    if fMRIdimension[3] != 383:
        print("miss volume frame, skip this subject: %s" %(sub_id))
        continue
    if not os.path.exists(newfunc_dir):
        os.makedirs(newfunc_dir) # make the directary for saving new data
    mri_newname = newfunc_dir + '/' + sub_id + '_' + ses_id + '_' + task_id + '_' + run_id + '_' + space_id + '_desc-preproc_bold.nii.gz'
    nib.save(fMRIimg, mri_newname) # rename the fMRI data
        
    # bold json file
    taskname = "REST"
    jsontis = {"RepetitionTime": np.float(TR), "TaskName": taskname}
    boldjson = newfunc_dir + '/' + sub_id + '_' + ses_id + '_' + task_id + '_' + run_id + '_' + space_id + '_desc-preproc_bold.json'
    writejson(jsontis, boldjson)
        
    # mask file
    MaskImage = nib.load(fMRIprep_mask_path[0])
    mask_newdir = newfunc_dir + '/' + sub_id + '_' + ses_id + '_' + task_id + '_' + run_id + '_' + space_id + '_desc-brain_mask.nii.gz'
    nib.save(MaskImage, mask_newdir)
        
    #####convert the ABCD motion file to fMRIprep confounds file 
    print('raw motion: %s' %(raw_motion_path))
    # confounds tsv file
    mvreg = pd.read_csv(raw_motion_path, delimiter="\t")
    mvreg = mvreg.iloc[:, 0:6]
    mvreg.columns = ['trans_x', 'trans_y', 'trans_z', 'rot_x', 'rot_y', 'rot_z']
    mvreg['rot_x'] = mvreg['rot_x'] * np.pi / 180 # convert rot to rad
    mvreg['rot_y'] = mvreg['rot_y'] * np.pi / 180
    mvreg['rot_z'] = mvreg['rot_z'] * np.pi / 180
    confreg = newfunc_dir + '/' + sub_id + '_' + ses_id + '_' + task_id + '_' + run_id + '_desc-confounds_timeseries.tsv'
    regressors = pd.concat([mvreg], axis=1)
    regressors.to_csv(confreg, sep='\t', index=False)# save confounds
    print('confounds tsv: %s' %(confreg))
        
    # confounds json file
    confregj = newfunc_dir + '/' + sub_id + '_' + ses_id + '_' + task_id + '_' + run_id + '_desc-confounds_timeseries.json'
    json2 = {
            "grayordinates": "91k",
            "space": "HCP grayordinates",
            "surface": "fsLR",
            "surface_density": "32k",
            "volume": "MNI152NLin6Asym"
            }
    writejson(json2, confregj)# write json
    print('confounds json: %s' %(confregj))
        
        
    
