import glob
import os

path = '/home/zhouyuan/fan/Datafc/BrainProject_fmriprep/V1_1/derivatives/*'

filename = glob.glob(path)

for i in filename:
     subid = i[-9:]
     outpath = 'E:/Public_Data/Twin_fMRI_2013_xcpd/xcp_d_new/'+subid
     if os.path.exists(outpath):
         continue

     cmd = ' docker run --rm -v E:/Public_Data/Twin_2013_temp_xcpd:/wd -v E:/Public_Data/Twin_fMRI_2013_fmriprep/derivatives/fmriprep/'+subid+'/fmriprep:/data -v E:/Public_Data/Twin_fMRI_2013_xcpd:/out -v D:/fantest/:/freesurfer_license pennlinc/xcp_d:latest /data /out participant -w /wd  -p 36P --despike --lower-bpf 0.01 --upper-bpf 0.1 --smoothing 6'

     os.system(cmd)

