import pandas as pd

import nibabel as nib

dlablelp = '/Users/qingchen/Documents/code/Data/FC/Schaefer2018_400Parcels_17Networks_order.dlabel.nii'
dlabel = nib.load(dlablelp).get_fdata()

pdata = pd.read_csv('/Users/qingchen/Desktop/Interaction/rightSF.csv')
indx = pdata['index']
box = []
for i in indx:
    print(i)
    print(dlabel[:,i+1])
    box.append(dlabel[:, i + 1])
df = pd.DataFrame(box)
df.columns = ['Region']

reshc = pd.concat([pdata, df], axis=1, join='inner')
reshc.to_csv('./rightSF_region.csv', index=False)