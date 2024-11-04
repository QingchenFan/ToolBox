import glob
import os
import pandas as pd
path = '/home/zhouyuan/dicom/*/*CBPD_bold_FM_*'

data = glob.glob(path)
dic = {}
sub = []
count = []
for i in data :
    subId = i.split('/')[-2]
    sub.append(subId)
    sum = len(os.listdir(i))
    count.append(sum)

dic = {'subID':sub,'count':count}
df = pd.Dataframe(dic)
df.to_csv('/home/zhouyuan/fan/sum.csv')