import pandas as pd

import glob

dp = '/Users/qingchen/Desktop/Data_20240330/*'

alldata = glob.glob(dp)
for i in alldata:
    mask = i.split('/')[-1]
    data = pd.read_csv(i)
    if len(data['id']) < 3856 or len(data['id']) > 3857:
        print(mask,'----->',len(data['id']))

