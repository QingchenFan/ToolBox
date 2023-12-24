import nibabel as nib
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import nibabel as nib
from scipy import stats
from sympy.stats import FisherZ
import math
import glob
data = '/home/cuizaixu_lab/fanqingchen/DATA/data/ABCD_HCP2016/sub-NDARINVZZZNB0XC_'
print(data[58:73])
data = sorted(glob.glob("/Users/fan/Documents/Datafc/test_data/test_fc/*.nii"))
for i in data:

    name = i[48:63]
    print(name)
    img_data = nib.load(i)
    img_data = img_data.get_data()
    print(img_data, img_data.shape)
    res = np.corrcoef(img_data, rowvar=False)
    print(res, res.shape)
    z_res = np.arctanh(res)
    np.savetxt(name, z_res)
    print(z_res, z_res.shape)

