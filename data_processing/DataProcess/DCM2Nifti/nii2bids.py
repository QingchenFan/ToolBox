from shutil import copy
import os

import json

StruPath = '/Users/fan/Documents/ZhouLab/data/Twin_fmri_2013/5_Structure_nii/'
FunPath = '/Users/fan/Documents/ZhouLab/data/Twin_fmri_2013/1_Rest_nii/'
targetpath = '/Users/fan/Documents/ZhouLab/data/Twin_fmri_2013/Twin_fmri_2013_bids/'



# foldername = os.listdir(StruPath)
# for i in foldername:
#     T1 = StruPath + i +'/'+i+'_T1w.nii.gz'
#     T1_json = StruPath + i +'/'+i+'_T1w.json'
#
#     bold = FunPath + i + '/' + i+'_task-rest_bold.nii.gz'
#     bold_json = FunPath + i + '/' + i +'_task-rest_bold.json'
#
#     targetpathfunc = '/Users/fan/Documents/ZhouLab/data/Twin_fmri_2013/Twin_fmri_2013_bids/'+i+'/func'
#
#     targetpathanat = '/Users/fan/Documents/ZhouLab/data/Twin_fmri_2013/Twin_fmri_2013_bids/'+i+'/anat'
#     if not os.path.exists(targetpathfunc):
#         os.makedirs(targetpathfunc)
#     if not os.path.exists(targetpathanat):
#         os.makedirs(targetpathanat)
#     copy(T1, targetpathanat)
#     copy(T1_json, targetpathanat)
#     copy(bold, targetpathfunc)
#     copy(bold_json, targetpathfunc)

import glob
filepath = '/Users/qingchen/Documents/Data/c_nii/'
subid = os.listdir(filepath)

for i in subid:
   T1w = glob.glob(filepath + i +'/t1_*.nii.gz')

   T1w_json = glob.glob(filepath + i +'/t1_*.json')
   T1w_targetpath = '/Users/qingchen/Documents/Datafc/Twins_2021_bids/'+i+'/anat/'
   if not os.path.exists(T1w_targetpath):
      os.makedirs(T1w_targetpath)
   if not T1w or not T1w_json:
      print('--no T1w--', i)
      continue
   copy(T1w[0], T1w_targetpath+i+'_T1w.nii.gz')
   copy(T1w_json[0], T1w_targetpath + i + '_T1w.json')

   fun = glob.glob(filepath + i +'/K19*.nii.gz')

   fun_json = glob.glob(filepath + i +'/K19*.json')
   funcpath = '/Users/qingchen/Documents/Datafc/Twins_2021_bids/'+i+'/func/'
   if not os.path.exists(funcpath):
      os.makedirs(funcpath)
   if not fun or not fun_json:
      print('--no bold--', i)
      continue
   copy(fun[0], funcpath+i+'_task-rest_bold.nii.gz')
   copy(fun_json[0], funcpath + i + '_task-rest_bold.json')