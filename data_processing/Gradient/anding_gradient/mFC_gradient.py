import glob

import numpy as np
from brainspace.datasets import load_parcellation, load_conte69
from brainspace.gradient import GradientMaps
from brainspace.plotting import plot_hemispheres
from brainspace.utils.parcellation import map_to_labels
from scipy.io import savemat
import scipy.io as scio

filename = ['hc_v2', 'hc001_50_v01', 'hc051_114_v01', 'MDDv1', 'MDDv2']
#filename = ['hc_v2', 'hc001_114_v01', 'MDDv1', 'MDDv2']
path = '/Volumes/qingchen/anding/gradient/'
databox = []
box = np.zeros([400,400])
reference = scio.loadmat('./reference.mat')
for i in filename:
    print('>====== ', i, ' ======<')
    filepath = path + i +'/Schaefer400Fcglobal/*.mat'
    FCpath = glob.glob(filepath)
    for j in FCpath:
        print(j)
        m = scio.loadmat(j)
        fisherzFC = np.arctanh(m['data'])
        box = np.add(box,fisherzFC)
    mFC = box / len(FCpath)
    print(mFC)
    mFC = np.tanh(mFC)
    print(mFC)

    print('>====== ', i, ' end ======<')
    gp = GradientMaps(kernel='normalized_angle', approach='pca', alignment='procrustes', n_components=10,
                      random_state=0)
    gp.fit(mFC, reference=reference['data'])
    res = gp.gradients_

    labeling = load_parcellation('schaefer', scale=400, join=True)
    surf_lh, surf_rh = load_conte69()
    mask = labeling != 0

    grad = [None] * 2

    for i in range(2):
        # map the gradient to the parcels
        grad[i] = map_to_labels(res[:, i], labeling, mask=mask, fill=np.nan)

    plot_hemispheres(surf_lh, surf_rh, array_name=grad, size=(2000, 800), cmap='coolwarm',
                     color_bar=True, label_text=['Grad1', 'Grad2'], zoom=1)

    # Plot Explained Variance
    import matplotlib.pyplot as plt

    expl_var = gp.lambdas_ / sum(gp.lambdas_)

    plt.figure(figsize=(5, 4))
    plt.scatter(range(expl_var.size), expl_var * 100, alpha=0.7, color='#00063F')
    plt.xlabel('Gradient', fontsize=14, fontname='Avenir')
    plt.ylabel('Explained variance (%)', fontsize=14, fontname='Avenir')
    plt.xticks(np.arange(len(expl_var)), np.arange(1, len(expl_var) + 1))  # axis ticks start at 1 not 0
    plt.show()
