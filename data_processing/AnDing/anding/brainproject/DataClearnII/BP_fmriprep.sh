#!/bin/bash
#SBATCH --job-name=Zhou
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu 2G
#SBATCH -p verylong.q
#SBATCH -o /home/zhouyuan/Fan/Log/job.%j.out
#SBATCH -e /home/zhouyuan/Fan/Log/job.%j.error.txt


#!/bin/bash
#User inputs:
bids_root_dir=/home/zhouyuan/Fan/BrainProjectII/DZ/
bids_root_dir_output_wd4singularity=/home/zhouyuan/Fan/DZ_temp

mkdir $bids_root_dir_output_wd4singularity
subj=$1
nthreads=40

mkdir $bids_root_dir/derivatives
mkdir $bids_root_dir_output_wd4singularity/derivatives
#Run fmriprep
echo ""
echo "Running fmriprep on participant: sub-$subj"
echo ""
#Make fmriprep directory and participant directory in derivatives folder
if [ ! -d $bids_root_dir/derivatives/fmriprep ]; then
    mkdir $bids_root_dir/derivatives/fmriprep
fi

if [ ! -d $bids_root_dir/derivatives/fmriprep/sub-${subj} ]; then
    mkdir $bids_root_dir/derivatives/fmriprep/sub-${subj}
fi
if [ ! -d $bids_root_dir_output_wd4singularity/derivatives/fmriprep ]; then
    mkdir $bids_root_dir_output_wd4singularity/derivatives/fmriprep
fi

if [ ! -d $bids_root_dir_output_wd4singularity/derivatives/fmriprep/sub-${subj} ]; then
    mkdir $bids_root_dir_output_wd4singularity/derivatives/fmriprep/sub-${subj}
fi

#Run fmriprep
docker run --rm -v $bids_root_dir_output_wd4singularity/derivatives/fmriprep/sub-${subj}:/wd \
-v $bids_root_dir:/input \
-v $bids_root_dir/derivatives/fmriprep/sub-${subj}:/out \
-v /home/zhouyuan/Fan/freesurfer_license \
nipreps/fmriprep:23.1.4 \
/input /out participant --participant_label ${subj} -w /wd --output-spaces T1w MNI152NLin6Asym:res-2 MNI152NLin2009cAsym:res-2 --fs-license-file \
/freesurfer_license/license.txt \
--cifti 91k --skip-bids-validation


