from shutil import copytree
import pandas as pd
import os

hclabel = pd.read_csv('/home/zhouyuan/fan/Data/brainproject_label/HC.csv')
hclabel = hclabel['subID']

for i in hclabel:
    subID = '0'+ str(i) + '_V01'
    datapath = '/home/zhouyuan/fan/Data/from_qiaokn/20240530085046/cbpd4ZY_checked_all/' + subID
    print(datapath)
    if not os.path.exists(datapath):
        print('No -',subID)
        continue
    tp = '/home/zhouyuan/fan/Data/brainproject/V01/HC/' + subID

    copytree(datapath,tp)

