#!/bin/bash
#SBATCH --job-name=abcd_anat
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu 4000
#SBATCH -o /GPFS/cuizaixu_lab_permanent/xulongzhou/ABCD/ABCD_fMRIprep_anatonly/sbatch_out/job.%j.out.txt
#SBATCH -e /GPFS/cuizaixu_lab_permanent/xulongzhou/ABCD/ABCD_fMRIprep_anatonly/sbatch_error/job.%j.error.txt

module load singularity/3.7.0

# User inputs
site=$1
subj=$2
ses_id=$3
MM_id=SIEMENS
rawMRI_dir=/home/cuizaixu_lab/xulongzhou/DATA/ABCD/ABCD_BIDS_raw_data/$MM_id/$site
output_dir=/GPFS/cuizaixu_lab_permanent/xulongzhou/ABCD
nthreads=4
fs_lincense=/GPFS/cuizaixu_lab_permanent/xulongzhou/IEEG_DSI_connectome/code/freesurfer

# Run fmriprep
echo ""
echo "Running fmriprep on participant: $subj"
echo ""

#Make fmriprep directory and participant directory in derivatives folder
mkdir $output_dir
mkdir $output_dir/ABCD_fMRIprep_anatonly
mkdir $output_dir/ABCD_fMRIprep_anatonly/$MM_id
mkdir $output_dir/ABCD_fMRIprep_anatonly/$MM_id/$site
mkdir $output_dir/ABCD_fMRIprep_anatonly/anat_w

# Run fmriprep
export SINGULARITYENV_TEMPLATEFLOW_HOME=/home/cuizaixu_lab/xulongzhou/.cache/templateflow/
singularity run --cleanenv \
	-B $output_dir/ABCD_fMRIprep_anatonly/$MM_id/$site:/output \
	-B $output_dir/ABCD_fMRIprep_anatonly/anat_w:/wk \
	-B $rawMRI_dir:/input \
	-B $fs_lincense:/fs \
	/home/cuizaixu_lab/xulongzhou/.singularity/fMRIprep-22.0.0rc2.sif \
	/input \
	/output \
	participant \
	--participant_label ${subj} \
	-w /wk \
	--n_cpus $nthreads \
	--mem-mb 32000 \
	--fs-license-file /fs/license.txt \
	--output-spaces T1w MNI152NLin6Asym:res-2 MNI152NLin2009cAsym:res-2 \
	--fs-no-reconall \
	--anat-only \
	--notrack \
	--skip-bids-validation \
	--debug all
	--clearn-workdir
