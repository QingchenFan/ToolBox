import glob
import pandas as pd
# 提取 label
path = '/Volumes/QCI/wangyun/NAc_rLH_rsFC_core/*MDD*'
datapath = glob.glob(path)

lp = '/Users/qingchen/Documents/Data/zhouLabData/Data135/Data135_MDD.csv'
label = pd.read_csv(lp)
nl = pd.DataFrame()
for i in datapath:
    subID = i.split('/')[-1][4:10]
    print(subID)
    result = label.loc[label['subID'] == subID]
    print(result)
    nl = pd.concat([nl, result], ignore_index=True)


nl.to_csv('./Data135_MDD.csv',index=False)