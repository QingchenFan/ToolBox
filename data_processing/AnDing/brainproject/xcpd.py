import glob
import os

path = '/home/zhouyuan/fan/Data/brainproject_processed/fmriprep_out_HC'
subID= glob.glob(path)

for subid in subID:
    print(subid)
    cmd = 'docker run --rm -v /home/zhouyuan/fan/Data/brainproject_processed/temp_hc:/wd -v /home/zhouyuan/fan/Data/brainproject_processed/fmriprep_out_HC/'+subid+':/data -v /home/zhouyuan/fan/Data/brainproject_processed/xcpd_out_HC:/out -v /home/zhouyuan/fan/freesurferlicense:/freesurfer_license pennlinc/xcp_d:0.6.0 /data /out participant -w /wd  -p 36P --despike --lower-bpf 0.01 --upper-bpf 0.1 --smoothing 6 --cifti'

    os.system(cmd)
