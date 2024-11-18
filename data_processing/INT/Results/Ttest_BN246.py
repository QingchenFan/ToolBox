import glob
import scipy.io as sio
import numpy as np
from scipy.stats import ttest_ind
HCData = sio.loadmat('/Volumes/QCI/NormativeModel/Data135/HC/INT/INT_BN246/INT_ind/sub-HC114_Ind.mat')['hwhms']
MDDData = sio.loadmat('/Volumes/QCI/NormativeModel/Data135/MDD/INT/INT_BN246/INT_ind/sub-MDD140_Ind.mat')['hwhms']
box = []
for i in range(0,246):
    print('ROI:', i+1)
    hcdata = HCData[i,:]
    mdddata = MDDData[i,:]

    t, p = ttest_ind(hcdata, mdddata)
    box.append(p)
    if p < 0.05:
        print('ROI:', i+1,' ','P-value:', p, ' ','T-value:', t)

pvalue = np.array(box)

print(pvalue)
print(pvalue.shape)