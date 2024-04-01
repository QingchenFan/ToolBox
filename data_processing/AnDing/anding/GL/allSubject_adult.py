import glob
import scipy.io as scio
import pandas as pd
import os

lp = '/Volumes/QCI/GL/adultSubid.csv'
label = pd.read_csv(lp)
lab = pd.read_csv(lp)['subject']

fp = '/Volumes/QCI/GL/FC_amygdala_vertex_adult/*_*FC'
fpbox = glob.glob(fp)
for i in fpbox:
    print('-----------'+i+'-----------')
    mask = i[-7:]
    mddbox = {}
    hcbox = {}
    for j in lab:
        subId = 'sub-' + j
        print('-----------'+subId+'-----------')
        if 'HC' in subId and 'HC' in i :
            dp = i + '/' + subId + '_AMGYDALA_' + mask + '.mat'
            if not os.path.exists(dp):
                print(subId + '------->No')
                continue
            data = scio.loadmat(dp)['data']
            hcbox.update({j:data[0,:]})

        if 'MDD' in subId and 'MDD' in i :
            dpmdd = i + '/' + subId + '_AMGYDALA_' + mask + '.mat'
            if not os.path.exists(dpmdd):
                print(subId + '------->No')
                continue
            mdddata = scio.loadmat(dpmdd)['data']
            mddbox.update({j:mdddata[0,:]})

    dfhc = pd.DataFrame.from_dict(hcbox, orient='index')
    dfhc.index.name = 'subject'

    #reshc = pd.concat([dfhc, label], axis=1, join='inner')
    reshc = pd.merge(label,dfhc, on='subject', how='inner')

    if not reshc.empty:
        reshc.to_csv('/Volumes/QCI/GL/allsubject_adult/HC_' + mask + '.csv', index=False)


    dfmdd = pd.DataFrame.from_dict(mddbox, orient='index')
    dfmdd.index.name = 'subject'
    #resmdd = pd.concat([dfmdd, label], axis=1, join='inner')
    resmdd = pd.merge(label, dfmdd, on='subject', how='inner')
    if not resmdd.empty:
        resmdd.to_csv('/Volumes/QCI/GL/allsubject_adult/MDD_' + mask + '.csv', index=False)




