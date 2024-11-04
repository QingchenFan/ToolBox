import pandas as pd

f1 = pd.read_csv('./n00_QC_omit_file.csv')  # w

f2 = pd.read_csv('./sbjListPaths_scz_t1.csv')  # s

l2 = f2['path']

for i in f1['0']:
    a = i.split('/')[8][:-3]
    newpath = '/n02dat01/users/wyshi/scz_t1/'+a+'/'+a+'_t1.nii'
    print(newpath)