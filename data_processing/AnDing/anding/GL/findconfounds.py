import glob
from shutil import copy
import pandas as pd
path = glob.glob('/Volumes/QCI/GL/adult_confounds/*')

results_df = pd.DataFrame(columns=['subID', 'FD'])
for i in path :
    if 'HC' in i :
        subid = i.split('/')[-1][0:9]
        print(subid)
        data = pd.read_csv(i, sep='\t')
        fd = data['framewise_displacement']
        fd_res= fd[1:].mean()

        results_df = results_df._append({'subID': subid, 'FD': fd_res}, ignore_index=True)

    if 'MDD' in i:
        subid = i.split('/')[-1][0:10]
        print(subid)
        data = pd.read_csv(i, sep='\t')
        fd = data['framewise_displacement']
        fd_res = fd[1:].mean()

        results_df = results_df._append({'subID': subid, 'FD': fd_res}, ignore_index=True)
results_df.to_csv('./adult_confounds.csv',index=False)