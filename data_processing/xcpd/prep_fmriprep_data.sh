#!/bin/bash


for id in 02 03 05 07 08 09 11 12 14 15 16 17 20 21 22
do

# site id
site_id=site${id}
MM_id=SIEMENS
ses_id=ses-baselineYear1Arm1

# aim folder
ABCD_fmri=/home/cuizaixu_lab/xulongzhou/DATA/ABCD/ABCD_fmri_mini
mkdir $ABCD_fmri
mkdir $ABCD_fmri/$MM_id
mkdir $ABCD_fmri/$MM_id/$site_id

# source folder
dMRI_s=/GPFS/cuizaixu_lab_permanent/Public_Data/ABCD/ABCC/rawdata/dMRI/$MM_id/$site_id
rsfMRI_s=/GPFS/cuizaixu_lab_permanent/Public_Data/ABCD/ABCC/rawdata/rsfMRI/$MM_id/$site_id
sMRI_s=/GPFS/cuizaixu_lab_permanent/Public_Data/ABCD/ABCC/rawdata/sMRI

# list the subject in fMRI
for subj in `ls $rsfMRI_s | grep sub*`
do

echo "******"
echo "run the subject: $subj"
echo "******"

# from the sMRI soruce cp file
if [ -d "$sMRI_s/$subj/$ses_id/anat" ]; then
	mkdir $ABCD_fmri/$MM_id/$site_id/$subj
	mkdir $ABCD_fmri/$MM_id/$site_id/$subj/$ses_id
	cp -arf $rsfMRI_s/$subj/$ses_id/func $ABCD_fmri/$MM_id/$site_id/$subj/$ses_id
fi

# cp file from the dMRI source
if [ -d "$dMRI_s/$subj/$ses_id/anat" ]; then
	mkdir $ABCD_fmri/$MM_id/$site_id/$subj
	mkdir $ABCD_fmri/$MM_id/$site_id/$subj/$ses_id
        cp -arf $rsfMRI_s/$subj/$ses_id/func $ABCD_fmri/$MM_id/$site_id/$subj/$ses_id
fi

done

done
