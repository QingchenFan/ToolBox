from brainspace.plotting import plot_hemispheres
import os
from brainspace.datasets import load_group_fc, load_parcellation, load_conte69
import scipy.io as scio
from brainspace.gradient import GradientMaps
import numpy as np
from brainspace.utils.parcellation import map_to_labels
import matplotlib.pyplot as plt

name = 'MDDv2'
path = '/Volumes/qingchen/anding/gradient/PCA/'+name+'/gradients_aligned/'
#path = '/Volumes/qingchen/anding/gradient/PCA/'+name+'/gradients_aligned/'

file = os.listdir(path)

box = np.zeros([400,10])

for i in file:
    datapath = path + i
    print(datapath)
    data = scio.loadmat(datapath)['data']
    box = np.add(box,data)

res = box / len(file)
#
# box = np.zeros([400,10])
# for p in ['hc001_50_v01', 'hc051_114_v01']:
#     path = '/Volumes/qingchen/anding/gradient/PCA/'+p+'/gradients_aligned/'
#     file = os.listdir(path)
#     for i in file:
#         datapath = path + i
#         data = scio.loadmat(datapath)['data']
#         box = np.add(box,data)
#
# res = box / 114



# First load mean connectivity matrix and Schaefer parcellation
conn_matrix = load_group_fc('schaefer', scale=400)
labeling = load_parcellation('schaefer', scale=400, join=True)   # labeling 64984
# and load the conte69 surfaces
surf_lh, surf_rh = load_conte69()


# Ask for 10 gradients (default)
mask = labeling != 0
grad = [None] * 2

for i in range(2):
    # map the gradient to the parcels
    grad[i] = map_to_labels(res[:, i], labeling, mask=mask, fill=np.nan)

plot_hemispheres(surf_lh, surf_rh,screenshot=True,filename='test22.png', array_name=grad, size=(1200, 400), cmap='coolwarm_r',
                 color_bar=True, label_text=['Grad1', 'Grad2'], zoom=1)


