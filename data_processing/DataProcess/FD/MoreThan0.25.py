import glob
import pandas as pd
path = '/Volumes/qingchen/Images_QC/confounds/MDD/*.tsv'
fl = glob.glob(path)
for i in fl:
    id = i[i.index('sub-'):i.index('sub-')+15]

    conf = pd.read_csv(i,sep='\t')
    fd = conf['framewise_displacement'][1:239]
    a = fd[fd > 0.20]
    res = len(a) / len(fd)
    if res > 0.10:
        print('exclude:', id)
    print(id,':'+'res=%.2f%%' % (res*100))
    print('-------------------------------------------')




