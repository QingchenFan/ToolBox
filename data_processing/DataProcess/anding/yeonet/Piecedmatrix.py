import os
import scipy.io as scio
import numpy as np
from scipy.io import savemat

path = '/Users/qingchen/Documents/Data/net_7/out/'
sub = os.listdir(path)

for i in range(1,8):
    box = []
    for j in sub:
        datapath = path + j +'/yeo7_'+str(i)+'.mat'
        Data = scio.loadmat(datapath)
        box.append(Data['data'])
    res = np.array(box).transpose(2, 1, 0)

    savemat(path+str(i)+'_net.mat', {'data': res})
