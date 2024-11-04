import os
import sys
import glob
import numpy as np
import pandas as pd
import nibabel as nib
import argparse
from xcp_d.interfaces import (regress, 
                              FilteringData,
                              CensorScrub, 
                              interpolate)
from nipype.interfaces import afni

########################### function
def writejson(data, outfile):
    import json
    with open(outfile, 'w') as f:
        json.dump(data, f)
    return outfile

########################### argparse system
parser = argparse.ArgumentParser(description='Test for argparse')
parser.add_argument('--dir', '-d', help='the directory of BIDS+fMRIprep style', required=True)
parser.add_argument('--ID', '-i', help='the subject ID', required=True)
parser.add_argument('--ses', '-s', help='the session name', required=True)
parser.add_argument('--task', '-t', help='the task name', required=True)
parser.add_argument('--run', '-r', help='the run name', required=True)
parser.add_argument('--space', '-c', help='the space name and resolution', required=True)
args = parser.parse_args()
xcpd_dir = args.dir
sub_id = args.ID
ses_id = args.ses
task_id = args.task
run_id = args.run
space_id = args.space
print('directory: %s' %(xcpd_dir))
print("subject ID: %s" %(sub_id))
print('session: %s' %(ses_id))
print('task: %s' %(task_id))
print('run: %s' %(run_id))
print('space: %s' %(space_id))

########################## main ######################################
####### raw data
func_dir = xcpd_dir + '/' + sub_id + '/' + ses_id + '/' + 'func' # the folder of preprocessed fMRI data after xcpd
os.chdir(func_dir)
fMRIprep_fMRI = glob.glob('./*' + task_id + '*' + run_id + '*' + space_id + '*_desc-preproc_bold.nii.gz')
mask = glob.glob('./*' + task_id + '*' + run_id + '*' + space_id + '*brain_mask.nii.gz')
confoundjson = glob.glob('./*' + task_id + '*' + run_id + '*confounds_timeseries.json')
confoundtsv = glob.glob('./*' + task_id + '*' + run_id + '*confounds_timeseries.tsv')
if len(fMRIprep_fMRI) == 0:
    print("skip this subjects: %s" %(sub_id))
    sys.exit()
if len(mask) == 0:
    print("skip this subjects: %s" %(sub_id))
    sys.exit()
if len(confoundjson) == 0:
    print("skip this subjects: %s" %(sub_id))
    sys.exit()
if len(confoundtsv) == 0:
    print("skip this subjects: %s" %(sub_id))
    sys.exit()
TR = nib.load(fMRIprep_fMRI[0]).header.get_zooms()[-1]  # repetition time
print('fMRI: %s' %(fMRIprep_fMRI[0]))
print("confound tsv: %s" %(confoundtsv[0]))
print('confound json: %s' %(confoundjson[0]))
print('TR = %s' %(TR))

###### despike using nipype
despike_out_file = sub_id + '_' + ses_id + '_' + task_id + '_' + run_id + '_' + space_id + '_desc-preproc_bold_despike.nii.gz'
#despike = afni.Despike()
#despike.inputs.in_file = fMRIprep_fMRI[0]
#despike.inputs.out_file = despike_out_file # despike.cmdline '3dDespike -prefix functional_despike functional.nii'
#despike.run()
#print('despike output: %s' %(despike_out_file))

###### bandpass using nipype
#out_file = sub_id + '_' + ses_id + '_' + task_id + '_' + run_id + '_' + space_id + '_desc-preproc_bold_bandpass_despike.nii.gz'
#bandpass = afni.Bandpass()
#bandpass.inputs.in_file = fMRIdatafile[0]
#bandpass.inputs.out_file = out_file
#bandpass.inputs.highpass = 0.01
#bandpass.inputs.lowpass = 0.2
#bandpass.inputs.despike = True # bandpass.cmdline '3dBandpass -prefix functional_bp 0.005000 0.100000 functional.nii'
#bandpass.run()  # doctest: +SKIP

###### censor scrubbing
scrub = CensorScrub()
scrub.inputs.in_file = despike_out_file
scrub.inputs.fd_thresh = 0.3
scrub.inputs.fmriprep_confounds_file = confoundtsv[0]
scrub.inputs.head_radius = 50.
scrub.inputs.motion_filter_type = 'none'
scrub.inputs.motion_filter_order = 4 # default
scrub.inputs.TR = TR
scrub.inputs.low_freq = 100.
scrub.inputs.high_freq = 101.
scrub.run()
print('CensorScrud fMRI output: %s' %(scrub._results['bold_censored']))
print('CensorScrud tmask output: %s' %(scrub._results['tmask']))
print('CensorScrud FD output: %s' %(scrub._results['fd_timeseries']))
print('CensorScrud confounds output: %s' %(scrub._results['fmriprep_confounds_censored']))

###### regression using xcpd
reg = regress()
reg.inputs.in_file = scrub._results['bold_censored']
reg.inputs.original_file = fMRIprep_fMRI[0]
reg.inputs.confounds = scrub._results['fmriprep_confounds_censored']
reg.inputs.mask = mask[0]
reg.inputs.TR = TR
reg.run()
print('confounds matrix: %s' %(reg._results['confound_matrix']))
print('residualized fMRI: %s' %(reg._results['res_file']))

###### interpolate using xcpd
interpolatewf = interpolate()
interpolatewf.inputs.in_file = reg._results['res_file']
interpolatewf.inputs.bold_file = despike_out_file
interpolatewf.inputs.TR = TR
interpolatewf.inputs.tmask = scrub._results['tmask']
interpolatewf.inputs.mask_file = mask[0]
interpolatewf.run()
print('interpolated fMRI: %s' %(interpolatewf._results['bold_interpolated']))

###### filtering using xcpd
filt = FilteringData()
filt.inputs.in_file = interpolatewf._results['bold_interpolated']
filt.inputs.mask = mask[0]
filt.inputs.tr = TR
filt.inputs.lowpass = 0.2
filt.inputs.highpass = 0.01
filt.inputs.filter_order = 2
filt.inputs.bandpass_filter = True
filt.run()
print('filtering fMRI: %s' %(filt._results['filt_file']))

###### censor scrubbing after filtering
scrub = CensorScrub()
scrub.inputs.in_file = filt._results['filt_file']
scrub.inputs.fd_thresh = 0.2
scrub.inputs.fmriprep_confounds_file = confoundtsv[0]
scrub.inputs.head_radius = 50.0
scrub.inputs.motion_filter_type = 'none'
scrub.inputs.motion_filter_order = 4 # default
scrub.inputs.TR = TR
scrub.inputs.low_freq = 100
scrub.inputs.high_freq = 101
scrub.run()
print('CensorScrud fMRI output: %s' %(scrub._results['bold_censored']))
print('CensorScrud tmask output: %s' %(scrub._results['tmask']))
print('CensorScrud FD output: %s' %(scrub._results['fd_timeseries']))
print('CensorScrud confounds output: %s' %(scrub._results['fmriprep_confounds_censored']))
