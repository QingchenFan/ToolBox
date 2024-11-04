import os
import glob
from shutil import copytree, copy

def copy_folder(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)
    for item in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, item)):
            copy(os.path.join(source_folder, item), destination_folder)
        else:
            copy_folder(os.path.join(source_folder, item), os.path.join(destination_folder, item))

funcpath = '/Volumes/MyBook/HCP_func/*'
strcpath = '/Volumes/MyBook/HCP_stru/'
fp = glob.glob(funcpath)

for i in fp:
    subid = i[-6:]
    print('----------',subid, ':star---------')

    if os.path.exists('/Volumes/MyBook/HCP_func/' + subid + '/release-notes/Structural_preproc.txt'):
        continue

    substr = ['MNINonLinear', 'release-notes', 'T1w']
    for j in substr:
        strcfile = strcpath + subid + '/' + j
        if not os.path.exists(strcfile):
            print('no --', strcfile)


        tarpath = i + '/' + j + '/'

        copy_folder(strcfile,tarpath)

    print('----------', subid, ':Done---------')







