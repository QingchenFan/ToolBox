import scipy.io as scio
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import glob

from statsmodels.stats.multitest import multipletests

datapath = '/Users/fan/Documents/Code/source_data_hyl/reviewwork/FDR/data/SEEG_BOLD_DSI_vector_for_calcu_corr/'


Rseegbold_pearson = {}
Pseegbold_pearson = {}
Rseegbold_spearman = {}
Pseegbold_spearman = {}
fdrlist = []
for sub in range(1, 17):
    substr = "%02d" % sub
    substr = str(substr)
    dataFile = datapath+'sub_' + substr + '_data.mat'
    data = scio.loadmat(dataFile)
    # calculate the pearson and spearman correlation between SEEG and BOLD signal
    seeg_bold = data['dsi_bold'][0]
    R = []
    P = []
    for bf in range(0, 7):
        Rpearson_seeg_bold = pearsonr(seeg_bold[bf][0], seeg_bold[bf][1])
        R.append(Rpearson_seeg_bold[0])
        P.append(Rpearson_seeg_bold[1])
    Rseegbold_pearson['sub'+substr] = R
    Pseegbold_pearson['sub'+substr] = P
    R = []
    P = []
    for bf in range(0, 7):
        Rspearman_seeg_bold = spearmanr(seeg_bold[bf][0], seeg_bold[bf][1])
        R.append(Rspearman_seeg_bold[0])
        P.append(Rspearman_seeg_bold[1])

    Rseegbold_spearman['sub'+substr] = R
    Pseegbold_spearman['sub'+substr] = P
    dsi_seeg = data['dsi_seeg'][0]
    dsi_bold = data['dsi_bold'][0]

res_bonferroni = multipletests(P, method='fdr_bh', alpha=0.05, is_sorted=False)
Rseegboldp = pd.DataFrame(Rseegbold_pearson)
Rseegboldp.to_csv('./dsi_bold-Rvalue-seegbold_pearson.csv')
Pseegboldp = pd.DataFrame(Pseegbold_pearson)
Pseegboldp.to_csv('./dsi_bold-Pvalue-seegbold_pearson.csv')
Rseegbolds = pd.DataFrame(Rseegbold_spearman)
Rseegbolds.to_csv('./dsi_bold-Rvalue-seegbold_spearman.csv')
Pseegbolds = pd.DataFrame(Pseegbold_spearman)
Pseegbolds.to_csv('./dsi_bold-Pvalue-seegbold_spearman.csv')