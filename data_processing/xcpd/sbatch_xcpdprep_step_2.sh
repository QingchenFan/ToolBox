#!/bin/bash
#SBATCH --job-name=motionreg
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu 8G
#SBATCH -p lab_fat_c
#SBATCH --qos=lab_fat
#SBATCH -o /GPFS/cuizaixu_lab_permanent/xulongzhou/ABCD/FCcode/slurm_out/job.%j.out
#SBATCH -e /GPFS/cuizaixu_lab_permanent/xulongzhou/ABCD/FCcode/slurm_error/job.%j.error.txt

# set the environment
source activate xcp_d
module load afni/20.3.01
# subject list
xcpdDir=$1
subjID=$2
sesID=$3
taskID=$4
runID=$5
spaceID=$6

# run xcpd pre-process
python ABCDxcpd.py --dir $xcpdDir --ID $subjID --ses $sesID --task $taskID --run $runID --space $spaceID  
