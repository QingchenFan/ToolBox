
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.io as scio
from PIL import Image


m1 = scio.loadmat('sub_20_BOLD_SEEG_corr_matrix_0815.mat')

m1_np = m1['BOLD_wm_corr']   # -0.36  0.93
print(m1_np.shape)
#以corr的形状生成一个全为0的矩阵
mask = np.zeros_like(m1_np)
#将mask的对角线及以上设置为True#这部分就是对应要被遮掉的部分
mask[np.triu_indices_from(mask)] = False
with sns.axes_style("white"):
    ax = sns.heatmap(m1_np, xticklabels=False, yticklabels=False, vmin=-0.4, vmax=1.0, mask=mask, annot=False, cmap="Blues",
                     cbar_kws={'ticks': [-0.4, 0.3, 1.0]}
        )                    # -0.36  0.93
    #设置colorbar字体大小
    cbar = ax.collections[0].colorbar

    cbar.ax.tick_params(labelsize=24, left=False, right=False)  #direction='in' 标签位置
    plt.savefig('BOLD_wm_corr_815.png', dpi=300)
    plt.show()



m2 = scio.loadmat('sub_20_BOLD_SEEG_corr_matrix_0815.mat')
m2_np = m2['SEEG_wm_corr']    # -0.64  0.97
#以corr的形状生成一个全为0的矩阵
mask = np.zeros_like(m2_np)
#将mask的对角线及以上设置为True#这部分就是对应要被遮掉的部分
mask[np.tril_indices_from(mask)] = False
with sns.axes_style("white"):
    ax = sns.heatmap(m2_np, xticklabels=False, yticklabels=False, vmax=1.0, mask=mask, annot=False, cmap="Blues",
                    cbar_kws={'ticks': [-0.6, 0.2, 1.0]}
                     )   # -0.64  0.97
    cbar_2 = ax.collections[0].colorbar
    cbar_2.ax.tick_params(labelsize=24, left=False, right=False)
    #plt.figure(dpi=300, figsize=(4, 3))
    plt.savefig('SEEG_wm_corr_815.png', dpi=300)
    plt.show()


'''
#合并到一起
img_a = Image.open('./a.png')
img_a = img_a.convert('RGBA')
img_b = Image.open('./b.png')
img_b = img_b.convert('RGBA')
img = Image.blend(img_a,img_b,0.3)
img.show()
'''
'''

#旋转
im = Image.open('./Figure_1.png')
im.rotate(180,expand=True).save('./1-1.png')
'''

'''
#上三角+下三角 画图  这种方法不可取
m1 = scio.loadmat('./sub_01_BOLD_wm_corr_2.mat')
m1_np = m1['corr']
print(m1_np)
m1_np_u = np.triu(m1_np)

m2 = scio.loadmat('./sub_01_seeg_corr_1_4Hz.mat')
m2_np = m2['corr']
print(m2_np)

m2_np_l = np.tril(m2_np)
print('m1_np_u---',m1_np_u)
print('m2_np_l---',m2_np_l)
m1_m2 = m1_np_u + m2_np_l
print('m1_m2---',m1_m2)

ax = sns.heatmap(m1_m2, xticklabels= False,yticklabels= False,annot=False,cmap="Blues")
cbar_2 = ax.collections[0].colorbar
cbar_2.ax.tick_params(labelsize=14)
#plt.figure(dpi=300, figsize=(4, 3))
plt.savefig('b.png',dpi=300)
plt.show()


#水平放置colorbar
ax = sns.heatmap(m1_np,xticklabels= False,yticklabels= False,vmax=1,mask=mask,annot=False,cmap="Blues",cbar_kws={"orientation":"horizontal"}
        )
'''



