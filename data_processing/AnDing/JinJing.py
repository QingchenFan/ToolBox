import os
import glob
from shutil import copytree

def walkFile(file):
    dirlist = []
    for root, dirs, files in os.walk(file):
        # 遍历所有的文件夹
        for d in dirs:
            dirlist.append(os.path.join(root, d))
    return dirlist,root

subpath = '/Users/qingchen/Desktop/test/test/*'   # 数据路径
targetpath = '/Users/qingchen/Desktop/tar'        # 存放数据的新文件夹路径
subdata = glob.glob(subpath)

for i in subdata:
    dir,root = walkFile(i)
    funpath = [d for d in dir if '0005_Functional_PA' in d]
    T1wpath = [t for t in dir if '0002_t1_mprage_sag_p2_iso' in t]
    if 'MDD' in root:
      subid = root[root.index('MDD'):root.index('MDD')+6]
    else:
      subid = root[root.index('HC'):root.index('HC') + 5]

    tarpath = targetpath
    FunRawpath = tarpath + '/FunRaw/'
    T1Rawpath = tarpath + '/T1Raw/'
    if not os.path.exists(FunRawpath) :
        os.makedirs(FunRawpath)
    if not os.path.exists(T1Rawpath) :
        os.makedirs(T1Rawpath)
    copytree(funpath[0], FunRawpath + subid)
    copytree(T1wpath[0], T1Rawpath + subid)




