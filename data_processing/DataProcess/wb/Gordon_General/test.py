import numpy as np
import pandas as pd
l = [[6, 1, 2, 3, 4, 5, 1, 2, 6, 7, 7, 8, 1, 2, 5]]

arr = np.array(l)
print(arr)
index = np.where(arr == 1)
print(index)

arr[[0, 0, 0], [1,  6, 12]]
arr[index[0], index[1]]=88
arr[0, 1]
print(arr)

weightpath = './GeneralSum.csv'
weightdata = pd.read_csv(weightpath)
print(weightdata)
res = weightdata['sum'][0]
print(res)