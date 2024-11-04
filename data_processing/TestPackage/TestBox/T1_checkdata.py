import pandas as pd

s1 = '/Users/qingchen/Documents/Data/zhouLabData/duilie/s1.csv'
t1 = '/Users/qingchen/Documents/Data/zhouLabData/duilie/t1.csv'

d1 = pd.read_csv(s1)
d2 = pd.read_csv(t1)

res = pd.merge(d1, d2, how='outer',on='subID')

res.to_csv('./res.csv')