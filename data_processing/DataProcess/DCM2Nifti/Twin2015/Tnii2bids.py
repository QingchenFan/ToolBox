import os
import glob
from shutil import copy

from tqdm import tqdm

path = '/Volumes/qingchen/out/'
filename = os.listdir(path)

for i in filename:
   print('================>', i)
   index = i.find('sub')

   subID = i[index+3:]

   a = subID.replace('_', '')
   outpath = '/Volumes/qingchen/Twin_2015_bids/'
   newfile = outpath + 'sub-' + a

   if not os.path.exists(newfile):
      os.makedirs(newfile)
      os.makedirs(newfile + '/func')
      os.makedirs(newfile + '/anat')

   sourcepath = path + i

   # T1wimagepath = sourcepath + '/scans_*_3.nii.gz'
   # T1wjsonpath = sourcepath + '/scans_*_3.json'
   # T1wimage = glob.glob(T1wimagepath)
   # T1wjson = glob.glob(T1wjsonpath)
   #
   # T1wimagepathII = sourcepath + '/3_*.nii.gz'
   # T1wjsonpathII = sourcepath + '/3_*.json'
   # T1wimageII = glob.glob(T1wimagepathII)
   # T1wjsonII = glob.glob(T1wjsonpathII)
   # if not T1wimage and not T1wimageII:
   #    print('================异常数据-无结构像：', i)
   #    continue
   #
   # if T1wimage:
   #
   #    copy(T1wimage[0], newfile + '/anat/sub-' + a + '_T1w.nii.gz')
   #    copy(T1wjson[0], newfile + '/anat/sub-' + a + '_T1w.json')
   # elif T1wimageII:
   #
   #    copy(T1wimageII[0], newfile + '/anat/sub-' + a + '_T1w.nii.gz')
   #    copy(T1wjsonII[0], newfile + '/anat/sub-' + a + '_T1w.json')

   funimagepath = sourcepath + '/scans_*_5.nii.gz'
   funjsonpath = sourcepath + '/scans_*_5.json'
   funimage = glob.glob(funimagepath)
   funjson = glob.glob(funjsonpath)

   funimagepathII = sourcepath + '/5_*.nii.gz'
   funjsonpathII = sourcepath + '/5_*.json'
   funimageII = glob.glob(funimagepathII)
   funjsonII = glob.glob(funjsonpathII)
   if not funimage and not funimageII:
      print('================异常数据-无功能像：', i)
      continue

   if funimage:

      copy(funimage[0], newfile + '/func/sub-' + a + '_task-rest_bold.nii.gz')
      copy(funjson[0], newfile + '/func/sub-' + a + '_task-rest_bold.json')
   elif funimageII:

      copy(funimageII[0], newfile + '/func/sub-' + a + '_task-rest_bold.nii.gz')
      copy(funjsonII[0], newfile + '/func/sub-' + a + '_task-rest_bold.json')
