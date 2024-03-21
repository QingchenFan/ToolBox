import nibabel as nib
import numpy as np
import pandas as pd
from scipy.io import savemat,loadmat

import pandas as pd

labelpath = '/Users/qingchen/Documents/code/Data/FC/Schaefer2018_400Parcels_7Networks_order.dlabel.nii'
label = nib.load(labelpath).get_fdata()

data = loadmat('./amgydala_allvertex.mat')['data']


roilist = []
dic = {}
for i in range(1,4):

    index = np.where(label == i)

    roi = data[:,index[1]]

    dic[i] = roi[0,:]

df = pd.DataFrame.from_dict(dic, orient='index').transpose()




