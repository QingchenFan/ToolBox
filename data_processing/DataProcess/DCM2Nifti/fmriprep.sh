




docker run --rm -v E:/Public_Data/Twin_fMRI_2012_fmriprep/derivatives/tmp_wd:/wd
-v E:/Public_Data/Twin_fMRI_2012_bids/:/input -v E:/Public_Data/Twin_fMRI_2012_fmriprep/derivatives:/out
-v D:/fantest/:/freesurfer_license nipreps/fmriprep:23.0.2 /input /out participant -w /wd
--output-spaces T1w MNI152NLin6Asym:res-2 MNI152NLin2009cAsym:res-2
--fs-license-file /freesurfer_license/license.txt
--cifti 91k
--skip-bids-validation