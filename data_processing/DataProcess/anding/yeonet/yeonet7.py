import glob
import numpy as np
import os
from scipy.io import savemat
import scipy.io as scio

def Extract(data, a, b, c, d):
    A = data[a:b,a:b]
    B = data[a:b,c:d]
    C = data[c:d, a:b]
    D = data[c:d, c:d]
    AB = np.concatenate((A, B), axis=1)
    CD = np.concatenate((C, D), axis=1)
    subFC = np.concatenate((AB, CD), axis=0)

    return subFC
def subnet(item, data):
    switcher = {'1' : Extract(data, 0, 31, 201, 231),
                '2' : Extract(data, 31, 68, 230, 270),
                '3' : Extract(data, 68, 91, 270, 293),
                '4' : Extract(data, 91, 113, 293, 318),
                '5' : Extract(data, 113, 126, 318, 331),
                '6' : Extract(data, 126, 148, 331, 361),
                '7' : Extract(data, 148, 200, 361, 400),
                }
    return switcher.get(item,"nothing")

datapath = '/Users/qingchen/Documents/Datafc/net_7/data/*.mat'  # 输入路径
n = glob.glob(datapath)
box = []
for i in n :
    Data = scio.loadmat(i)
    data = Data['NetworkMatrix']
    id = i[-14:-4]
    p = '/Users/qingchen/Documents/Datafc/net_7/'+ id   # 每个被试创建一个新路径
    if not os.path.exists(p):
        os.makedirs(p)
    for j in range(1,8):
        res = subnet(str(j), data)
        savemat(p + '/yeo7_'+str(j)+'.mat',{'data': res})




