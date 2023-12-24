import glob
import os
import nibabel as nib
path = '/Volumes/SeagateBackupPlusDrive/Public_Data/Twin_fMRI_2015_bids/*'
filename = glob.glob(path)
for i in filename:
    subID = i[-8:]
    #print('------',subID,'------')
    funcpath = i + '/func/' + subID + '_task-rest_bold.nii.gz'
    T1path = i + '/anat/' + subID + '_T1w.nii.gz'
    if not os.path.exists(T1path) :
        print(subID + ' : no T1w')
    if not os.path.exists(funcpath) :
        print(subID + ' : no Func')


    data = nib.load(funcpath)

    if data.shape[3] != 240 :
        print(subID + ' : no 240 ', 'time : ', data.shape[3] )


