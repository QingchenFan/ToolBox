import glob
import os
import numpy as np
from brainspace.datasets import load_parcellation, load_conte69
from brainspace.gradient import GradientMaps
from brainspace.plotting import plot_hemispheres
from brainspace.utils.parcellation import map_to_labels
from scipy.io import savemat
import scipy.io as scio


labeling = load_parcellation('schaefer', scale=400, join=True)
surf_lh, surf_rh = load_conte69()
path = '/Volumes/qingchen/anding/gradient/hc_v2/Schaefer400Fcglobal/'
filename = os.listdir(path)
for i in filename:

    file = path + i
    print('====='+file+'=====')

    data = glob.glob(file)
    print(data)

    m = scio.loadmat(data[0])
    gp = GradientMaps(kernel='normalized_angle', approach='pca', alignment='procrustes', n_components=10, random_state=0)
    gp.fit(m['data'])
    res = gp.gradients_
    newpath = '/Volumes/qingchen/anding/gradient/hc_v2/gradients_aligned_global/'+i
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    #savemat(newpath +'/'+ i +'_gradient.mat', {'data': res})

    #  画图

    labeling = load_parcellation('schaefer', scale=400, join=True)
    surf_lh, surf_rh = load_conte69()
    mask = labeling != 0

    grad = [None] * 2

    for i in range(2):
        # map the gradient to the parcels
        grad[i] = map_to_labels(res[:, i], labeling, mask=mask, fill=np.nan)

    plot_hemispheres(surf_lh, surf_rh, array_name=grad, size=(2000, 800), cmap='coolwarm',
                     color_bar=True, label_text=['Grad1', 'Grad2'], zoom=1)


