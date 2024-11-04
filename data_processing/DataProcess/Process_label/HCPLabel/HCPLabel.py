

import numpy as np

with open('job.1074830.txt', mode='r') as file_name:
    list_subname = file_name.readlines()
ls = []
for j in list_subname:
    ls.append(j.strip('\n'))

with open('ABCD_HCP_Label.csv', mode='r') as label:
    label_name = label.readlines()

label_list = []
for i in label_name:
    label_list.append(i[0:15])

index_list = []
for m in ls:
    if m in label_list:
        index_list.append(label_list.index(m))
res = []
for index in index_list:
    res.append(int(label_name[index]))
resFile = open('./HCPLable_G.csv', mode='w')

for k in res:
    resFile.write(k)
