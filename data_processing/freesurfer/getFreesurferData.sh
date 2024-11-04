#!/bin/bash
export FREESURFER_HOME=/Applications/freesurfer/7.4.1
export SUBJECTS_DIR=$FREESURFER_HOME/subjects
source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh

export SUBJECTS_DIR='/Volumes/QCI/GL/data135_out_fmriprep/sourcedata/freesurfer'
newpath=/Users/qingchen/Desktop/testfreesurfer/

mkdir $newpath

for subj in $(ls ${SUBJECTS_DIR});
do
  if [ ! -d $newpath/${subj} ]; then
      mkdir $newpath/${subj}
  fi
  echo "${subj}";
  aparcstats2table --hemi lh \
  --meas thickness \
  --parc aparc.DKTatlas \
  --tablefile $newpath/${subj}/lh_thickness.txt  \
  --subjects ${subj}/

  asegstats2table --meas volume \
  --tablefile $newpath/${subj}/subcortical_volume.txt \
  --subjects ${subj}/
done