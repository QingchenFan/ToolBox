import glob
import pingouin as pg
import scipy.io as scio
import numpy as np
import pandas as pd
import scipy.stats
from statsmodels.sandbox.stats.multicomp import multipletests
from scipy.stats import rankdata

datafile = sorted(glob.glob('/Users/fan/Documents/Code/source_data_hyl/reviewwork/data/Fig2SM_SEEGFCBOLDFCspearman_controllingdistance/Fig2SM_SEEGFCBOLDFCspearman_controllingdistance/*.mat'))
rlistSpearman = []
plistSpearman = []
for i in datafile:
    for j in range(0, 7):
        data = scio.loadmat(i)  # dsi_seeg dsi_bold seeg_bold BOLD_distance
        data_one = data['seeg_bold'][0][j][0].tolist()
        data1 = pd.DataFrame(data_one, columns=['data_one'])

        data_two = data['seeg_bold'][0][j][1].tolist()
        data2 = pd.DataFrame(data_two, columns=['data_two'])

        covar = data['seeg_bold'][0][j][2].tolist()
        data3 = pd.DataFrame(covar, columns=['covar'])

        temp = pd.concat([data1, data2], axis=1)
        res = pd.concat([temp, data3], axis=1)

        resCovari = pg.partial_corr(data=res, x='data_one', y='data_two', covar=['covar'], method='spearman')


        rlistSpearman.append(resCovari['r'][0])
        plistSpearman.append(resCovari['p-val'][0])


spearmanPvalueFDR = multipletests(plistSpearman, method='fdr_bh', alpha=0.05, is_sorted=False)
spearmanPvalueFDR = spearmanPvalueFDR[1].tolist()

Rvaluespearman = pd.DataFrame(rlistSpearman, columns=['r'])
Rvaluespearman = pd.DataFrame(Rvaluespearman.values.T, columns=Rvaluespearman.index, index=Rvaluespearman.columns)

Pvaluespearman = pd.DataFrame(plistSpearman, columns=['p'])
Pvaluespearman = pd.DataFrame(Pvaluespearman.values.T, columns=Pvaluespearman.index, index=Pvaluespearman.columns)

FDRpspearman = pd.DataFrame(spearmanPvalueFDR, columns=['FDR-p'])
FDRpspearman = pd.DataFrame(FDRpspearman.values.T, columns=FDRpspearman.index, index=FDRpspearman.columns)

Res = pd.concat([Rvaluespearman, FDRpspearman], axis=0)

#res = pd.concat([temp, Pvaluespearman], axis=0)

#Res.to_csv('./distance_regress-dsi_seeg-spearman0129.csv')

end = 0
temprp = pd.DataFrame(np.zeros((2, 7)), columns=['0', '1', '2', '3', '4', '5', '6'])
for i in range(0, 106, 7):
    end = 6 + i
    r = Res.iloc[0, i:end+1]
    fdrp = Res.iloc[1, i:end+1]

    r = pd.DataFrame(r, columns=['r'])
    r = pd.DataFrame(r.values.T, columns=r.index, index=r.columns)

    fdrp = pd.DataFrame(fdrp, columns=['FDR-p'])
    fdrp = pd.DataFrame(fdrp.values.T, columns=fdrp.index, index=fdrp.columns)

    resbox = pd.concat([r, fdrp], axis=0)
    resbox.columns = ['0', '1', '2', '3', '4', '5', '6']

    temprp = pd.concat([temprp, resbox], axis=0)

temprp.drop(index=[0, 1], inplace=True)
temprp.to_csv('./SEEGFCBOLDFCspearman_controllingdistance0202.csv')