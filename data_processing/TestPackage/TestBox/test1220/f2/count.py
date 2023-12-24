import pandas as pd
import numpy as np
data = pd.read_csv('times.csv')

id = data['id']
wave = data.iloc[:,8:38]


#ndata = pd.concat([data['id'],data.iloc[:,8:38]],axis = 1)
res = []
for i in range(0,146):
    one = wave.loc[i].tolist()
    box = []
    temp = 0
    print(one)
    for j in range(0,len(one)):
        t = one[j]
        if int(t) == 0 :
            if temp != 0:
                box.append(temp)
            box.append(t)
            temp = 0
        if int(t) == -1:
            if temp != 0:
                box.append(temp)
            box.append(t)
            temp = 0
        if int(t) == 1:
            temp = temp + 1
            if j == len(one)-1:
                box.append(temp)
    a = [c for c in box if c!=0 and c !=-1]
    box.append(len(a))
    print(box)
    res.append(box)

df = pd.DataFrame(res)
# 将 DataFrame 保存为文件
df.to_csv('./my_file.csv', index=False)