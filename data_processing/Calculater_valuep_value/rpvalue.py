import glob

import scipy.io as scio
import numpy as np
import pandas as pd
import scipy.stats
from statsmodels.sandbox.stats.multicomp import multipletests
from scipy.stats import rankdata
#datapath = '/Users/fan/Documents/Code/source_data_hyl/reviewwork/FDR/spearman_and_pearson_data_and_P_R_code/result_review_spearman/sub_01_results_step4_SEEG_DSI_BOLD.mat'

datafile = sorted(glob.glob('/Users/fan/Documents/Code/source_data_hyl/reviewwork/data/Python_test_wm_connect_vs_distance_0129/*.mat'))


# rlistPearson = []
# plistPearson = []
#
# for i in datafile:
#
#     for j in range(0, 7):
#         data = scio.loadmat(i)
#         box = data['dsi_seeg'][0][j]
#         pcorr, pvalue = scipy.stats.pearsonr(box[0], box[1])
#         #print('--correlation:', correlation, '--pvalue:', pvalue)
#         rlistPearson.append(pcorr)
#         plistPearson.append(pvalue)
#
# pearsonPvalueFDR = multipletests(plistPearson, method='fdr_bh', alpha=0.05, is_sorted=False)


rlistSpearman = []
plistSpearman = []
for i in datafile:
    for j in range(0, 7):

        data = scio.loadmat(i)
        box = data['SEEG_distance'][0][j]  # # dsi_seeg dsi_bold seeg_bold
        scorr, pvalue = scipy.stats.spearmanr(box[0], box[1])
        #print('--correlation:', correlation, '--pvalue:', pvalue)
        rlistSpearman.append(scorr)
        plistSpearman.append(pvalue)

spearmanPvalueFDR = multipletests(plistSpearman, method='fdr_bh', alpha=0.05, is_sorted=False)

spearmanPvalueFDR = spearmanPvalueFDR[1].tolist()


Rvaluespearman = pd.DataFrame(rlistSpearman, columns=['r'])
Rvaluespearman = pd.DataFrame(Rvaluespearman.values.T, columns=Rvaluespearman.index, index=Rvaluespearman.columns) # 将pandas一列变成一行


Pvaluespearman = pd.DataFrame(plistSpearman, columns=['p'])
Pvaluespearman = pd.DataFrame(Pvaluespearman.values.T, columns=Pvaluespearman.index, index=Pvaluespearman.columns)

FDRpspearman = pd.DataFrame(spearmanPvalueFDR, columns=['FDR-p'])
FDRpspearman = pd.DataFrame(FDRpspearman.values.T, columns=FDRpspearman.index, index=FDRpspearman.columns)


temp = pd.concat([Rvaluespearman, FDRpspearman], axis=0)
#res = pd.concat([temp, Pvaluespearman], axis=0)

# temp.to_csv('./native_space_seeg_bold-spearman0131.csv')
end = 0
temprp = pd.DataFrame(np.zeros((2, 7)), columns=['0', '1', '2', '3', '4', '5', '6'])
for i in range(0, 106, 7):
    end = 6 + i
    r = temp.iloc[0, i:end+1]
    fdrp = temp.iloc[1, i:end+1]

    r = pd.DataFrame(r, columns=['r'])
    r = pd.DataFrame(r.values.T, columns=r.index, index=r.columns)

    fdrp = pd.DataFrame(fdrp, columns=['FDR-p'])
    fdrp = pd.DataFrame(fdrp.values.T, columns=fdrp.index, index=fdrp.columns)

    resbox = pd.concat([r, fdrp], axis=0)
    resbox.columns = ['0', '1', '2', '3', '4', '5', '6']
    print('resbox--',resbox)
    temprp = pd.concat([temprp, resbox], axis=0)
    print('temprp--', temprp)

temprp.drop(index=[0,1], inplace=True)
temprp.to_csv('./wm_connect_vs_distance_seeg_bold-spearman0131.csv')





