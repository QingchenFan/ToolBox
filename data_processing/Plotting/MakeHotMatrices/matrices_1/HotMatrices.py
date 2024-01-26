import scipy.io as scio
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

#np.set_printoptions(threshold=np.sys.maxsize)


m1 = scio.loadmat('sub_20_BOLD_SEEG_corr_matrix_0815.mat')
m1_np = m1['corr']
m1_tril = np.tril(m1_np)
print(m1_tril)

m2 = scio.loadmat('sub_20_BOLD_SEEG_corr_matrix_0815.mat')
m2_np = m2['corr']
m2_triu = np.triu(m2_np)
print(m2_triu)
#fig, ax = plt.subplots(figsize = (38,38))

#二维的数组的热力图，横轴和数轴的ticklabels要加上去的话，既可以通过将array转换成有column
#和index的DataFrame直接绘图生成，也可以后续再加上去。后面加上去的话，更灵活，包括可设置labels大小方向等。
sns.heatmap(pd.DataFrame(np.round(m1_tril, 2)),
                annot=False, xticklabels=False, yticklabels=False, vmax=0.8, cmap="Blues")
#square=True,
#vmax=1, vmin=0,#设置展示最大值，最小值
#plt.figure(dpi=300,figsize=(120,100))
plt.savefig('sub_01_BOLD_wm_corr_2.png')

plt.show()

sns.heatmap(pd.DataFrame(np.round(m2_triu,2)),
                annot=False, xticklabels=False, yticklabels=False, vmax=1.0, cmap="Blues")
#plt.figure(dpi=300,figsize=(120,100))

plt.savefig('sub_01_seeg_corr_1_4Hz.png')

plt.show()


mm = scio.loadmat('/Users/fan/Documents/Datafc/HCPData/HCPDtest/HCPDFC/sub-HCD0001305_FC2.mat')
mm = mm['data']

label = pd.read_csv('/Users/fan/Documents/Datafc/HCPData/JHU_ICBM/rICBM_DTI_81_WMPM_FMRIB58_68_2.csv', header=None)
newlabel = []
for i in range(0, 68):
    if i <10:
      newlabel.append(label[0][i][2:])
    else:
      newlabel.append(label[0][i][3:])

data = pd.DataFrame(np.round(mm, 2), columns=newlabel, index=newlabel)
print(data)

cx = sns.heatmap(data,
                 xticklabels=True, yticklabels=True, cmap='mako', annot=False,
                #cbar_kws ={'format': '%.1f','ticks': [-1.0, 0.0, 1.0]}
                )    # xticklabels/yticklabels x轴的titel  "Spectral"
cx.tick_params(labelsize=100, left=False, bottom=False)  # 控制去掉小刻度线
cx.set_xticklabels(newlabel, fontsize=4, font='Arial')# x轴上字体大小
cx.set_yticklabels(newlabel, fontsize=4, font='Arial')

cbar_3 = cx.collections[0].colorbar
cbar_3.ax.tick_params(labelsize=12, left=False, right=False)
#plt.savefig('FunctionalConnectivity.png', dpi=300, bbox_inches='tight')  #bbox_inches='tight' 字体展示完整

plt.show()