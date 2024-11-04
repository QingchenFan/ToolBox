import pandas as pd

fd = pd.read_csv('./adult_confounds.csv')

label = pd.read_csv('/Volumes/QCI/wangyun/Data135_MDD.csv')

subID = label['subID']
res = pd.DataFrame()
for i in subID:
    subID = 'sub-' + i

    FD = fd.loc[fd['subID'] == subID]

    res = pd.concat([res,FD])

res.to_csv('./MDD_FD.csv')