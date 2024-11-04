import glob
import os.path
from scipy.io import loadmat,savemat
import numpy as np
from matplotlib import pyplot as plt


def hotmap(data, outpath):
    fig, ax = plt.subplots()
    im = ax.imshow(data, cmap='Blues')  # 创建热图并返回可映射对象

    ax.tick_params(labelsize=10, left=False, bottom=False)
    ax.axis('off')
    cbar = fig.colorbar(im, ax=ax, shrink=0.6)
    cbar.ax.tick_params(labelsize=12, left=False, right=False)
    cbar.outline.set_visible(False)
    plt.savefig(outpath, dpi=300)


# TODO：修改下面两个路径，输入和输出。
datapath = '/Users/qingchen/Documents/code/Data/JJ_FC/Data/*'
outpath = '/Users/qingchen/Documents/code/Data/JJ_FC_out/'

data = glob.glob(datapath)

for i in data:
    print(i)
    subID = i[-6:]
    sdata = sorted(glob.glob(i + '/TC/*.mat'))


    # Rename
    for m in range(0,len(sdata)):
        if len(sdata[m]) < len(sdata[0]):
            newname = sdata[m][:-6] + '_0' + sdata[m][-5:]
            os.rename(sdata[m],newname)

    sdata = sorted(glob.glob(i + '/TC/*.mat'))

    fcBox = []
    for j in sdata:
        print('>>>>>>',j)
        matrix = loadmat(j)['a']
        fcBox.append(matrix.T[0,:])
    subpath = outpath + '/' +subID
    if not os.path.exists(subpath):
        os.mkdir(subpath)
    r = np.array(fcBox)

    # FC
    resFC = np.corrcoef(r)

    savemat(subpath + '/' + subID +'_FCroi.mat',{'FC':resFC})
    hotmap(resFC,subpath + '/' + subID +'_FCroi')
    #  FC Fisher Z
    z_res = np.arctanh(resFC)
    z_res[z_res >= 18] =np.arctanh(1)
    plt.clf()
    savemat(subpath + '/' + subID + '_FCroi_FZ.mat', {'FC': z_res})
    hotmap(z_res,subpath + '/' + subID + '_FCroi_FZ')

