import glob
import os
from shutil import copy

datapath = '/Users/qingchen/Desktop/HC/*'    # TODO
data = glob.glob(datapath)
for i in data:

    subid = i.split('/')[-1].replace('_','')

    newpath = '/Users/qingchen/Desktop/BIDS/V01/HC/'+'sub-'+subid     # TODO
    if not os.path.exists(newpath):
         os.mkdir(newpath)

    funpath = newpath + '/func'
    t1wpath = newpath + '/anat'
    fieldmappath = newpath + '/fmap'

    if not os.path.exists(funpath):
         os.mkdir(funpath)
    if not os.path.exists(t1wpath):
         os.mkdir(t1wpath)
    if not os.path.exists(fieldmappath):
         os.mkdir(fieldmappath)

    T1w = glob.glob(i + '/*t1*.nii')
    T1wjson = glob.glob(i + '/*t1*.json')

    fun = glob.glob(i + '/*bold_resting*.nii')
    funjson = glob.glob(i + '/*bold_resting*.json')

    fmpath = sorted(glob.glob(i + '/*bold_field_mapping*.json'))
    print(fmpath)
    for inx, p in enumerate(fmpath):
        if 'ph' not in p:
            inx = inx + 1
           # n = p.split('/')[-1][:-4]
            ph = p[:-5]
            fm = ph + '.nii'

            copy(p, fieldmappath + '/sub-' + subid + '_acq-v1_magnitude' + str(inx) + '.json')
            copy(fm, fieldmappath + '/sub-' + subid + '_acq-v1_magnitude' + str(inx) + '.nii')
        else:
            #n = p.split('/')[-1][:-5]
            ph = p[:-5]
            fm = ph + '.nii'
            copy(p, fieldmappath + '/sub-' + subid + '_phasediff.json')
            copy(fm, fieldmappath + '/sub-' + subid + '_phasediff.nii')

    if len(fun) != 0:
        copy(fun[0],funpath+'/sub-'+subid+'_task-rest_acq-ap_run-1_bold.nii')
        copy(funjson[0], funpath + '/sub-' + subid + '_task-rest_acq-ap_run-1_bold.json')
    else:
        print('No funcAP：',i)

    if len(T1w) != 0 :
        copy(T1w[0],t1wpath+'/sub-'+subid+'_T1w.nii')
        copy(T1wjson[0], t1wpath + '/sub-' + subid + '_T1w.json')
    else:
        print('No T1w：', i)