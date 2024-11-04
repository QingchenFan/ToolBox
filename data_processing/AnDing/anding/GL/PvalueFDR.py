import pandas as pd
from statsmodels.stats.multitest import multipletests
import numpy as np
mask = 'Pvalue_rightSF'
path = '/Volumes/QCI/GL/RData/'+mask+'.csv'
data = pd.read_csv(path)
dataII = data
iterm = ['diagnosis','age_group','diagnosis:age_group']
res = []
for i in iterm:
    #i = 'age_group'
    print('--->',i)
    Lp = []

    Lp = [value for value in data[i] if pd.notna(value)]

    res_fdr = multipletests(Lp, method='fdr_bh', alpha=0.05, is_sorted=False)

    box = np.zeros(data[i].shape)
    datanumpy = data[i].to_numpy()
    pvalue_indexes = np.where(~np.isnan(datanumpy))[0]

    box[pvalue_indexes] = res_fdr[1]

    res.append(box)
    #print(res)
res = np.array(res).T
df = pd.DataFrame(res,columns=['diagnosis_FDR','age_group_FDR','diagnosis:age_group_FDR'])

# 将 DataFrame 保存为文件
#df.to_csv('/Users/qingchen/Desktop/Pvalue_rightCM_bonferroni_test.csv', index=True)
df.to_csv('/Volumes/QCI/GL/RData/'+mask+'_FDR.csv', index=True)