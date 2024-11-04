import numpy as np
import nibabel as nib
import seaborn as sns

import scipy.io as scio
import matplotlib.pyplot as plt
import pandas as pd

'''
    将模型的权重映射回对称矩阵
'''


#wdata = pd.read_csv('Gordon_ADHD.csv')
wdata = pd.read_csv('Gorden_Int.csv')
wdata = wdata['0']

symmetryweightnp = np.ones((352, 352))
#  这个index存放上三角每个元素的坐标，第一个坐标就是对应第一个权重
index = []
for i in range(0, 352):
    for j in range(0, 352):
       if i == j or i > j:
          continue
       index.append([i, j])

for i in range(0, 61776):

    symmetryweightnp[index[i][0], index[i][1]] = wdata[i]

#  完成对称
for i in range(0, 352):
    for j in range(0, 352):
        if i == j or i < j:
            continue
        symmetryweightnp[i][j] = symmetryweightnp[j][i]

print(symmetryweightnp)

def positiveymmetryweightnp(symmetryweightnp):
    pweightnp = symmetryweightnp


    pweightnp[pweightnp < 0] = 0
    pweightroi = np.sum(pweightnp, axis=1)
    pres = []
    for i in range(0, 352):
        tmp=pweightnp[i, :]
        length=len(tmp[tmp!=0])
        pres.append(pweightroi[i] / length)

    pres = pd.DataFrame(pres)
    pres.index = pres.index + 1
    pres.to_csv('./pres.csv')


def negativemmetryweightnp(symmetryweightnp):
    nweightnp = symmetryweightnp
    nweightnp[nweightnp > 0] = 0
    print(np.where(nweightnp!=0))
    nweightroi = np.sum(nweightnp, axis=1)

    nweightroi = np.abs(nweightroi)

    nres = []
    for i in range(0, 352):
        tmp=nweightnp[i, :]
        length=len(tmp[tmp!=0])
        if length == 0:
            continue
        nres.append(nweightroi[i] / length)

    nres = pd.DataFrame(nres)
    nres.index = nres.index + 1
    nres.to_csv('./nres.csv')
#positiveymmetryweightnp(symmetryweightnp)
negativemmetryweightnp(symmetryweightnp)