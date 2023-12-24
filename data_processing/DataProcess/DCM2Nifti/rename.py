import os

path = '/home/cuizaixu_lab/zhaoshaoling/DATA_C/fqc_test/Twin_fMRI_2013_bids/'

filename = os.listdir(path)

for i in filename:
    antpath = path + i + '/anat/'
    anatfile = os.listdir(antpath)
    for j in anatfile:
        print('j-',j)
        newanat = i + '_T1w.nii.gz'
        newjson = i+ '_T1w.json'
        print('newanat-', newanat)
        print(j[-4:])
        if j[-4:] == 'json':
            os.rename(antpath+j, antpath+newjson)
        if j[-2:] == 'gz':
            os.rename(antpath+j, antpath+newanat)
    funcpath = path + i + '/func/'
    funcfile = os.listdir(funcpath)
    for p in funcfile:
        newfunc = i + '_task-rest_bold.nii.gz'
        newfjson = i + '_task-rest_bold.json'
        if p[-4:] == 'json':
            os.rename(funcpath+p, funcpath+newfjson)
        if p[-2:] == 'gz':
            os.rename(funcpath+p, funcpath+newfunc)
    exit()
