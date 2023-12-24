import zipfile
from shutil import copy
import glob
import os

# path = '/Volumes/MyBook/HCP_Resting_State_fMRI1_Preprocessed_sourcedata/*rfMRI*.zip'
# file = glob.glob(path)
# newpath = '/Volumes/MyBook/HCP_func/'

path = '/Volumes/MyBook/HCP_Structure_zip/*Structural*.zip'
file = glob.glob(path)
newpath = '/Volumes/MyBook/HCP_stru/'
for i in file:
    print('-i-', i)
    filename = i[-32:]  # HCP name



    f = newpath + i[34:40]
    # if os.path.exists(f):
    #     print(i[40:46], '--done--')
    #     continue

    copy(i, newpath)
    os.remove(i)  # 将原始文件删除

    with zipfile.ZipFile(newpath + filename, 'r') as fzip:
        # 文件全部加压缩到destpath目录
        fzip.extractall(newpath)
    os.remove(newpath + filename)  # 删除copy过来的压缩文件






