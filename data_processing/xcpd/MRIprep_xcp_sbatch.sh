#!/bin/bash
site=site02;
for subj in `ls /GPFS/cuizaixu_lab_permanent/Public_Data/ABCD/ABCC/rawdata/rsfMRI/SIEMENS/$site`
do

echo ""
echo "Running xcpd on participant: $subj"
echo ""

rawdata=/GPFS/cuizaixu_lab_permanent/Public_Data/ABCD/ABCC/rawdata
ABCDfmri=/GPFS/cuizaixu_lab_permanent/xulongzhou/ABCD/fMRI_mini

mkdir $ABCDfmri
mkdir $ABCDfmri/$site
mkdir $ABCDfmri/$site/$subj
mkdir $ABCDfmri/$site/$subj/ses-baselineYear1Arm1

cp -arf $rawdata/sMRI/$subj/ses-baselineYear1Arm1/* $ABCDfmri/$site/$subj/ses-baselineYear1Arm1
cp -arf $rawdata/rsfMRI/SIEMENS/$site/$subj/ses-baselineYear1Arm1/* $ABCDfmri/$site/ses-baselineYear1Arm1
done
