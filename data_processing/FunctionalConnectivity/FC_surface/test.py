import glob
import os
import numpy as np
import nibabel as nib
from nilearn.maskers import NiftiMasker
from scipy.io import savemat
from nilearn import plotting

path = '/Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_freesurfer/fsaverage/fsaverage_LR32k/fsaverage.R.BN_Atlas.32k_fs_LR.label.gii'
a = nib.load(path)
dataa = a.darrays[0].data
print(dataa.shape)
savemat('r.mat', {'dataR': dataa})

path = '/Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_freesurfer/fsaverage/fsaverage_LR32k/fsaverage.L.BN_Atlas.32k_fs_LR.label.gii'
b = nib.load(path)
datab = b.darrays[0].data
print(datab.shape)
savemat('l.mat', {'dataL': datab})
