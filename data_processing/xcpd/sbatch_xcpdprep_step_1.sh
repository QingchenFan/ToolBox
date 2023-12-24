#!/bin/bash
#SBATCH --job-name=motionreg
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu 4G
#SBATCH --qos=lab_fat
#SBATCH -p lab_fat_c
#SBATCH -o /GPFS/cuizaixu_lab_permanent/xulongzhou/ABCD/FCcode/slurm_out/job.%j.out
#SBATCH -e /GPFS/cuizaixu_lab_permanent/xulongzhou/ABCD/FCcode/slurm_error/job.%j.error.txt

# set the environment
source activate xcp_d
# subject list
siteID=$1
runID=$2
# run xcpd pre-process
python ABCDdcan2fMRIprep.py --site $siteID --run $runID  