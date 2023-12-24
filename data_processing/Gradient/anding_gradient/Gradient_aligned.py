import glob

from brainspace.gradient import GradientMaps
from scipy.io import savemat
import scipy.io as scio

filename = ['hc_v2', 'hc001_50_v01', 'hc051_114_v01', 'MDDv1', 'MDDv2']
#filename = ['hc_v2', 'hc001_114_v01', 'MDDv1', 'MDDv2']
path = '/Volumes/qingchen/anding/gradient/'
databox = []
for i in filename:
    print('>====== ', i, ' ======<')
    filepath = path + i +'/Schaefer400Fcglobal/*.mat'
    FCpath = glob.glob(filepath)
    for j in FCpath:
        print(j)
        m = scio.loadmat(j)
        databox.append(m['data'])
    print('>====== ', i, ' end ======<')
print(len(databox))


gp = GradientMaps(kernel='normalized_angle',approach='pca', alignment='procrustes', n_components=10, random_state=0)
gp.fit(databox)
ref = gp.gradients_
print(len(ref))
print(ref[0].shape)
savemat('/Volumes/qingchen/anding/gradient/all_gradient_global_pca.mat', {'data': ref})
