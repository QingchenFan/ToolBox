import pandas as pd

path = '/Volumes/QCI/GL/RData/results_rightCM.csv'
tmp = pd.read_csv(path,header=None)
allP = []
for i in range(0,tmp.shape[0]):
    print('------->',i)
    plist = []
    box = tmp.iloc[i].values.tolist()

    #key = '`Pr(>F)` = c('
    key = '`F value` = c('
    index = box[0].find(key)

    #p = box[0][index:].split('(')[2].split(',')  # Find p value
    p = box[0][index:].split('(')[1].split(',')  # Find f value
    #print('-------->',p)

    plist.append(p[0])
    plist.append(p[1])
    plist.append(p[3])
    allP.append(plist)
    #mddbox.update({j: mdddata[0, :]})
    #print('--',allP)

# 将列表转换为 DataFrame
df = pd.DataFrame(allP,columns=['diagnosis','age_group','diagnosis:age_group'])

# 将 DataFrame 保存为文件
df.to_csv('./Fvalue_rightCM.csv', index=True)