import glob
import os

from shutil import copy
path = '/Volumes/qingchen/QC/BIDS/BDHCMDD/*'
sub = glob.glob(path)

for i in sub:
    print(i[-15:])
    fm1json = glob.glob(i + '/func/*facematching_run-1*ap*.json')
    fm1 = glob.glob(i + '/func/*facematching_run-1*ap*.nii.gz')
    newpathfun = '/Users/qingchen/Documents/Datafc/brianproject/facemapping1/FunRaw/'+ i[-15:] +'/'
    if not os.path.exists(newpathfun):
        os.mkdir(newpathfun)
    copy(fm1[0],newpathfun)
    copy(fm1json[0], newpathfun)

    T1json = glob.glob(i + '/anat/*.json')
    T1 = glob.glob(i + '/anat/*.nii.gz')
    newpathT1 = '/Users/qingchen/Documents/Datafc/brianproject/facemapping1/T1Raw/' + i[-15:] + '/'
    if not os.path.exists(newpathT1):
        os.mkdir(newpathT1)
    copy(T1[0], newpathT1)
    copy(T1json[0], newpathT1)
    # '------------------------------------------'
    #
    # fm2json = glob.glob(i + '/func/*facematching_run-2*pa*.json')
    # fm2 = glob.glob(i + '/func/*facematching_run-2*pa*.nii.gz')
    # newpathfun2 = '/Users/qingchen/Documents/Datafc/brianproject/facemapping2/FunRaw/'+ i[-15:] +'/'
    # if not os.path.exists(newpathfun2):
    #     os.mkdir(newpathfun2)
    # copy(fm2[0],newpathfun2)
    # copy(fm2json[0], newpathfun2)
    #
    # T1json2 = glob.glob(i + '/anat/*.json')
    # T12 = glob.glob(i + '/anat/*.nii.gz')
    # newpathT1w2 = '/Users/qingchen/Documents/Datafc/brianproject/facemapping2/T1Raw/' + i[-15:] + '/'
    # if not os.path.exists(newpathT1w2):
    #     os.mkdir(newpathT1w2)
    # copy(T12[0], newpathT1w2)
    # copy(T1json2[0], newpathT1w2)
    # '------------------------------------------'
    #
    # ugjson = glob.glob(i + '/func/*ultimategame*.json')
    # ug = glob.glob(i + '/func/*ultimategame*.nii.gz')
    # newpathugfun = '/Users/qingchen/Documents/Datafc/brianproject/UG/FunRaw/' + i[-15:] + '/'
    # if not os.path.exists(newpathugfun):
    #     os.mkdir(newpathugfun)
    # copy(ug[0], newpathugfun)
    # copy(ugjson[0], newpathugfun)
    #
    # T1ugjson = glob.glob(i + '/anat/*.json')
    # T1ug = glob.glob(i + '/anat/*.nii.gz')
    # newpathugT1 = '/Users/qingchen/Documents/Datafc/brianproject/UG/T1Raw/' + i[-15:] + '/'
    # if not os.path.exists(newpathugT1):
    #     os.mkdir(newpathugT1)
    # copy(T1ug[0], newpathugT1)
    # copy(T1ugjson[0], newpathugT1)
    # '------------------------------------------'
    # long1json = glob.glob(i + '/func/*longresting_run-1*.json')
    # long1 = glob.glob(i + '/func/*longresting_run-1*.nii.gz')
    # if len(long1) == 0 :
    #     continue
    # newpathlong1fun = '/Users/qingchen/Documents/Datafc/brianproject/long1/FunRaw/' + i[-15:] + '/'
    # if not os.path.exists(newpathlong1fun):
    #     os.mkdir(newpathlong1fun)
    # copy(long1[0], newpathlong1fun)
    # copy(long1json[0], newpathlong1fun)
    #
    # T1long1json = glob.glob(i + '/anat/*.json')
    # T1long1 = glob.glob(i + '/anat/*.nii.gz')
    # newpathlong1T1 = '/Users/qingchen/Documents/Datafc/brianproject/long1/T1Raw/' + i[-15:] + '/'
    # if not os.path.exists(newpathlong1T1):
    #     os.mkdir(newpathlong1T1)
    # copy(T1long1json[0], newpathlong1T1)
    # copy(T1long1[0], newpathlong1T1)
    # '------------------------------------------'
    # long2json = glob.glob(i + '/func/*longresting_run-2*.json')
    # long2 = glob.glob(i + '/func/*longresting_run-2*.nii.gz')
    # if len(long2) == 0:
    #     continue
    # newpathlong2fun = '/Users/qingchen/Documents/Datafc/brianproject/long2/FunRaw/' + i[-15:] + '/'
    # if not os.path.exists(newpathlong2fun):
    #     os.mkdir(newpathlong2fun)
    # copy(long2[0], newpathlong2fun)
    # copy(long2json[0], newpathlong2fun)
    #
    # T1long2json = glob.glob(i + '/anat/*.json')
    # T1long2 = glob.glob(i + '/anat/*.nii.gz')
    # newpathlong2T1 = '/Users/qingchen/Documents/Datafc/brianproject/long2/T1Raw/' + i[-15:] + '/'
    # if not os.path.exists(newpathlong2T1):
    #     os.mkdir(newpathlong2T1)
    # copy(T1long2json[0], newpathlong2T1)
    # copy(T1long2[0], newpathlong2T1)


