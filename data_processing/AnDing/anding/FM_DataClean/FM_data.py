import os
import glob
from shutil import copy

import os
import glob
from shutil import copy

path = "/home/zhouyuan/fan/Data/duilie/nifti/V01/*/*FM*"

data = glob.glob(path)

for i in data:
    subID = i.split('/')[-2]
    print("subID: ", subID)
    dataname = i.split('/')[-1]
    print("dataname: ", dataname)
    npath = "/home/zhouyuan/fan/Data/To_Wangyun/Queue/V1" + subID
    if not os.path.exists(npath):
        os.mkdir(npath)

    copy(i,npath + '/' + dataname)
    exit()


path = "/home/zhouyuan/fan/Data/To_Wangyun/Queue/V01/*"
spath = "/home/zhouyuan/fan/Data/duilie/nifti/V01/"
data = glob.glob(path)
for i in data:
    subID = i.split('/')[-1]
    t1path = glob.glob(spath + '/' + subID + '/'+ '*t1_mprage*')
    for j in t1path:
        npath = "/home/zhouyuan/fan/Data/To_Wangyun/Queue/V01" + subID
        dataname = j.split('/')[-1]
        copy(j, npath + '/' + dataname)

#path = "/home/zhouyuan/fan/Data/duilie/nifti/V28/*/*t1_mprage*"
#path = "/home/zhouyuan/fan/Data/brainproject/V01/BD/*/*face*"

# name = ['BD','HC','NaturalDepression','PrecisionDepression']
# for n in name:
#     path = "/home/zhouyuan/fan/Data/brainproject/V01/"+n+"/*/*face*"
#     data = glob.glob(path)
#     for i in data:
#         subID = i.split('/')[-2]
#         print('subID: ',subID)
#         dataname = i.split('/')[-1]
#         print('dataname: ',dataname)
#         npath = "/home/zhouyuan/fan/Data/To_Wangyun/BrainProject/V01/"+n+"/" + subID
#         if not os.path.exists(npath):
#          os.mkdir(npath)
#         copy(i,npath + '/' + dataname)

'''
name = ['BD', 'HC', 'NaturalDepression', 'PrecisionDepression']
for n in name:
    print('------------------------------', n, '---------------------------')

    path = "/home/zhouyuan/fan/Data/To_Wangyun/BrainProject/V01/" + n + "/*/"
    spath = "/home/zhouyuan/fan/Data/brainproject/V01/"+n+"/"
    data = glob.glob(path)
    for i in data:
        ID = i.split('/')[8]
        print(ID)
        d = glob.glob(spath + ID + '/*t1*')
        print('d',spath + ID + '/*t1*')
        for j in d:
            subID = j.split('/')[-2]
            print('subID: ', subID)
            dataname = j.split('/')[-1]
            print('dataname: ', dataname)
            npath = "/home/zhouyuan/fan/Data/To_Wangyun/BrainProject/V01/" + n + "/" + subID
            if not os.path.exists(npath):
                os.mkdir(npath)
            copy(j, npath + '/' + dataname) 
'''

name = ['BD', 'HC', 'NaturalDepression', 'PrecisionDepression']
for n in name:
    data_path = "/home/zhouyuan/fan/Data/To_Wangyun/BrainProject/V01/" + n + "/*/"
    data_path = "/home/zhouyuan/fan/Data/To_Wangyun/Queue/V1/*"
    data = glob.glob(data_path)
    for i in data:
        face_data = glob.glob(i + '/*FM*')
        if len(face_data) == 0:
           print(i,'No - facce data found')
        t1_data = glob.glob(i + '/*t1*')
        if len(t1_data) == 0:
            print(i,'No - t1 data found')