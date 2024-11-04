#!/bin/bash
#SBATCH --job-name=abcd
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu 8000
#SBATCH -p lab_fat_c
#SBATCH -o /GPFS/cuizaixu_lab_permanent/xulongzhou/ABCD/xcp_sbatch_out/job.%j.out
#SBATCH -e /GPFS/cuizaixu_lab_permanent/xulongzhou/ABCD/xcp_sbatch_error/job.%j.error.txt

module pruge
module load singularity

#User inputs:
site=$1
subj=$2
xcpd_output=/GPFS/cuizaixu_lab_permanent/xulongzhou/ABCD/xcp_output/$site
xcpd_work=/GPFS/cuizaixu_lab_permanent/xulongzhou/ABCD/xcp_work/$site
xcpd_input=/GPFS/cuizaixu_lab_permanent/Public_Data/ABCD/ABCC/rawdata/rsfMRI/SIEMENS/$site

#Run xcpd
echo ""
echo "Running xcpd on participant: $subj"
echo ""

#Make fmriprep directory and participant directory in derivatives folder
if [ ! -d $xcpd_output ]; then
    mkdir $xcpd_output
fi

if [ ! -d $xcpd_output/${subj} ]; then
    mkdir $xcpd_output/${subj}
fi

if [ ! -d $xcpd_work ]; then
    mkdir $xcpd_work
fi

if [ ! -d $xcpd_work/${subj} ]; then
    mkdir $xcpd_work/${subj}
fi

# run xcp_d
#export SINGULARITYENV_TEMPLATEFLOW_HOME=/GPFS/cuizaixu_lab_permanent/xulongzhou/.cache/templateflow
unset PYTHONPATH;
singularity run --cleanenv \
	-B $xcpd_input/${subj}:/xcpd_input \
	-B $xcpd_output/${subj}:/xcpd_output \
    	-B $xcpd_work/${subj}:/xcpd_work \
    	-B /home/cuizaixu_lab/wuguowei/.cache:/home/xcp_abcd/.cache \
	/home/cuizaixu_lab/xulongzhou/DATA/apps/singularity/xcpd.latest.sif \
	/xcpd_input \
    	/xcpd_output \
    	-w /xcpd_work \
    	--participant_label ${subj} \
    	-p 24P \
    	--lower-bpf 0.01 \
    	--upper-bpf 0.2
