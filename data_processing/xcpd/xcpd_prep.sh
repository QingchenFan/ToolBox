#!/bin/bash
##### dcan 2 fMRIprep
#for siteID in `ls /GPFS/cuizaixu_lab_permanent/xulongzhou/ABCD/ABCD_fMRIprep_anatonly/SIEMENS | grep site`
#do
#runID=run-1
#sbatch sbatch_xcpdprep_step_1.sh $siteID $runID
#runID=run-2
#sbatch sbatch_xcpdprep_step_1.sh $siteID $runID
#done

#### xcpd pre-processing
ABCD=/GPFS/cuizaixu_lab_permanent/xulongzhou/ABCD
SIEMENS=/GPFS/cuizaixu_lab_permanent/xulongzhou/ABCD/ABCD_xcpd/SIEMENS
ls $SIEMENS | grep site > $ABCD/site_list.txt
for siteID in `ls $SIEMENS | grep site`
do
xcpdDir=$SIEMENS/$siteID
ls $xcpdDir | grep sub > $ABCD/${siteID}SubjectList.txt

    for subjID in `ls $xcpdDir | grep sub`
    do
    sesID=ses-baselineYear1Arm1
    taskID=task-rest
    spaceID=space-MNI152NLin6Asym_res-2
    runID=run-1
    sbatch sbatch_xcpdprep_step_2.sh $xcpdDir $subjID $sesID $taskID $runID $spaceID
    runID=run-2
    sbatch sbatch_xcpdprep_step_2.sh $xcpdDir $subjID $sesID $taskID $runID $spaceID
    done
done
