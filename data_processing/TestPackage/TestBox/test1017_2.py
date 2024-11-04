import glob
import pandas as pd
#  根据id 找到一行所在位置，然后根据索引获取正一行，保存到list中，然后list变成pandas,最后保存成表格

path = '/Volumes/qingchen/BNU/Twin_fMRI_2015_bids/*'
csvpath = '/Users/qingchen/Documents/Datafc/Twin_2015_FC/scale/twin2015all.csv'
filepath = glob.glob(path)
inf = pd.read_csv(csvpath)

idlist = inf['id'].tolist()

inflist = []
for i in filepath:
    subID = i[-4:]
    mark = '9'+ subID[:-1] + '0' + subID[-1]
    mark = int(mark)
    if mark in idlist:
        index = idlist.index(mark)
        print(inf.loc[index])

        inflist.append(inf.loc[index])
# 将列表转换为 DataFrame
df = pd.DataFrame(inflist)

# 将 DataFrame 保存为文件
df.to_csv('./my_file.csv', index=False)

