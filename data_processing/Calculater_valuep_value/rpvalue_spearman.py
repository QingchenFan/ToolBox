import glob

import scipy.io as scio
import numpy as np
import pandas as pd
import scipy.stats
from statsmodels.sandbox.stats.multicomp import multipletests
from scipy.stats import rankdata
#datapath = '/Users/fan/Documents/Code/source_data_hyl/reviewwork/FDR/spearman_and_pearson_data_and_P_R_code/result_review_spearman/sub_01_results_step4_SEEG_DSI_BOLD.mat'

datafile = sorted(glob.glob('/Users/fan/Documents/Code/source_data_hyl/reviewwork/FDR/data/SEEG_BOLD_DSI_vector_for_calcu_corr/*.mat'))


rlist = []
plist = []

for i in datafile:

    for j in range(0, 7):
        data = scio.loadmat(i)
        box = data['dsi_seeg'][0][j]  # dsi_seeg dsi_bold seeg_bold
        correlation, pvalue = scipy.stats.spearmanr(box[0], box[1])
        #print('--correlation:', correlation, '--pvalue:', pvalue)
        rlist.append(correlation)
        plist.append(pvalue)

res_bonferroni = multipletests(plist, method='fdr_bh', alpha=0.05, is_sorted=False)
np.savetxt('./dsi_seeg_PvalueFDR_spearman.txt', res_bonferroni[1])
filer = open('./dsi_seeg_Rvalue_spearman.csv', mode='w')
filep = open('./dsi_seeg_Pvalue_spearman.csv', mode='w')
for i in rlist:
    filer.write(str(i))
    filer.write('\n')

for j in plist:
    filep.write(str(j))
    filep.write('\n')

