#!/bin/bash
for id in 20 21 22
do 
site_id=site${id}
ses_id=ses-baselineYear1Arm1
rawMRI_dir=/home/cuizaixu_lab/xulongzhou/DATA/ABCD/ABCD_BIDS_raw_data/SIEMENS/$site_id

ls $rawMRI_dir | grep sub-N > $rawMRI_dir/batch_run_subject_id.txt

for subj_id in `ls $rawMRI_dir | grep sub-N`
do

echo ""
echo "Running fmriprep on participant: $subj_id"
echo ""

sbatch -p lab_fat_c fMRIprep_anatonly.sh $site_id $subj_id $ses_id

done

done
