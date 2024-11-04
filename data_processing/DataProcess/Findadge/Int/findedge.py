import numpy as np
import nibabel as nib
import seaborn as sns

import scipy.io as scio
import matplotlib.pyplot as plt
import pandas as pd

'''
    将模型的权重映射回对称矩阵
'''

imadata = nib.load('gorden.nii').get_data()
print(imadata.shape)

wdata = pd.read_csv('Gordon_ADHD.csv')
wdata = pd.read_csv('Gorden_General.csv')
onenp = np.ones((352, 352))

wdata = wdata['0']


index = []
for i in range(0, 352):
    for j in range(0, 352):
       if i == j or i > j:
          continue
       index.append([i, j])

for i in range(0, 61776):

    onenp[index[i][0], index[i][1]] = wdata[i]


for i in range(0, 352):
    for j in range(0, 352):
        if i == j or i < j:
            continue
        onenp[i][j] = onenp[j][i]

np.savetxt('./duichen.txt', onenp)
#----------------------------------------------------------
'''
    属于同一个网络下的脑区放到一起，
'''
label = pd.read_csv('../roi_name(1).csv')
print(label)
rotname = [i for i in label['roi_name']]
rotname = list(set(rotname))


listbox = [list(label.loc[label['roi_name']==i]['number']) for i in rotname]
print(listbox)
onenp2 = np.ones((352, 352))

num = 0
for i in range(0, len(listbox)):
    for j in listbox[i]:
        print('num--', num)
        onenp2[num, :] = onenp[j-1, :]
        num = num + 1

numt = 0
onenp3 = np.ones((352, 352))
for i in range(0, len(listbox)):
    for j in listbox[i]:
        print('num--', numt)
        onenp3[:, numt] = onenp2[:, j-1]
        numt = numt + 1

#onenp3[onenp3 >= -0.0002 and onenp3 <= 0.0002] = 0
onenp3[(onenp3 >= -0.0002) & (onenp3 <= 0.0002)] = 0


mm = onenp
mm3 = onenp3
data1 = pd.DataFrame(np.round(mm, 8))
data2 = pd.DataFrame(np.round(mm3, 8))



# cx = sns.heatmap(data1,
#                 xticklabels=False, yticklabels=False,  cmap='afmhot', shading='gouraud', annot=False,
#                 #cbar_kws ={'format': '%.1f', 'ticks': [-1.0, 0.0, 1.0]},
#                 vmax=0.0001, vmin=-0.0004
#                 )    # xticklabels/yticklabels x轴的titel  "Spectral"  范围 , vmin=0

cx = sns.heatmap(data2,
                xticklabels=False, yticklabels=False,  cmap='coolwarm', shading='gouraud', annot=False,
                #cbar_kws ={'format': '%.1f', 'ticks': [-1.0, 0.0, 1.0]},
                vmax=0.0004, vmin=-0.0004
                )
cx.tick_params(labelsize=100, left=False, bottom=False)  # 控制去掉小刻度线
# cx.set_xticklabels(newlabel, fontsize=4, font='Arial')# x轴上字体大小
# cx.set_yticklabels(newlabel, fontsize=4, font='Arial')

cbar_3 = cx.collections[0].colorbar
cbar_3.ax.tick_params(labelsize=12, left=False, right=False)
#plt.savefig('FunctionalConnectivity.png', dpi=300, bbox_inches='tight')  #bbox_inches='tight' 字体展示完整

plt.show()