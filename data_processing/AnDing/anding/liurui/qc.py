import glob
import pandas as pd
path = '/Volumes/qingchen/anding/checkdata/freesurfer_v2_mdd/freesurfer/sub*'
data = glob.glob(path)
# 质控 欧拉值

T ={}
for d in data:
    subpath = d +'/stats/aseg.stats'
    print(subpath)
    with open(subpath, mode='r', encoding='utf-8') as s:
        c = s.readlines()
        box = [i for i in c]
    rh = box[31].split(',')
    lh = box[32].split(',')
    rhEulernum = 2 - 2 * int(rh[-2])
    lhEulernum = 2 - 2 * int(lh[-2])
    avgEulernum = (rhEulernum + lhEulernum)/2
    T.update({d[-10:]:[rhEulernum,lhEulernum,avgEulernum]})
    print(T)

csv = pd.DataFrame(T)
csv = pd.DataFrame(csv.values.T, columns=csv.index, index=csv.columns)
csv.to_csv('./MDD_v2_euler.csv')

