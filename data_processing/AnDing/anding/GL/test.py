import nibabel as nib
import numpy as np
import pandas as pd
from scipy.io import savemat,loadmat

import pandas as pd

# labelpath = '/Users/qingchen/Documents/code/Data/FC/Schaefer2018_400Parcels_7Networks_order.dlabel.nii'
# label = nib.load(labelpath).get_fdata()
#
# data = loadmat('./amgydala_allvertex.mat')['data']
#
#
# roilist = []
# dic = {}
# for i in range(1,4):
#
#     index = np.where(label == i)
#
#     roi = data[:,index[1]]
#
#     dic[i] = roi[0,:]
#
# df = pd.DataFrame.from_dict(dic, orient='index').transpose()

# import pandas as pd
# import pandas as pd
#
# my_dict = {'a': [1, 2, 3, 4], 'f': [6, 2, 8, 9], 'e': [1, 1, 1, 1]}
#
# df = pd.DataFrame.from_dict(my_dict, orient='index')
# df.index.name = 'subject'
#
#
# my_dict2 = {'a': 1, 'b': 6, 'd': 9,'e': 100}
#
# df2 = pd.DataFrame.from_dict(my_dict2, orient='index')
# df2.index.name = 'subject'
# merged_df = pd.merge(df, df2, on='subject', how='inner')
# print(merged_df)
# concatenated_df = pd.concat([df, df2], axis=1, join='inner')
# print(concatenated_df)
# if not concatenated_df.empty:
#     concatenated_df.to_csv('./text.csv',)

# data = loadmat('./sub-HC008_AMGYDALA_CM_L_FC.mat')['data']
# nan_indices = np.argwhere(np.isnan(data))
#
# print(nan_indices[:,1])
# a = nan_indices[:,1]
# print(len(a))
#
#
# labelpath = '/Users/qingchen/Documents/code/Data/FC/Schaefer2018_400Parcels_17Networks_order.dlabel.nii'
# label = nib.load(labelpath).get_fdata()
# # print(label.shape)
# b = np.argwhere(label == 0)
# res = b[:,1]
# print(res)
# print(len(res))
#
# for i,j in enumerate(a,res):
#     print(i,'--',j)
# import pandas as pd
# path = '/Users/qingchen/Desktop/results_CM_R_list.csv'
# pd.set_option('display.max_rows', None)  # 设置为None以显示所有行
# pd.set_option('display.max_columns', None)
# a = pd.read_csv(path)
# list = []
# list.append(a.iloc[1,:])
# import pandas as pd
# from nilearn.datasets import fetch_localizer_contrasts
#
# n_subjects = 16
# data = fetch_localizer_contrasts(
#     ["left vs right button press"],
#     n_subjects,
#     legacy_format=False,
# )
# second_level_input = data["cmaps"]
# design_matrix = pd.DataFrame(
#     [1] * len(second_level_input), columns=["intercept"]
# )
# from nilearn.glm.second_level import SecondLevelModel
#
# second_level_model = SecondLevelModel(smoothing_fwhm=8.0, n_jobs=2)
# second_level_model = second_level_model.fit(
#     second_level_input, design_matrix=design_matrix
# )
# z_map = second_level_model.compute_contrast(output_type="z_score")
# print(z_map)
import matplotlib.pyplot as plt
import numpy as np

import mne
from mne.datasets import sample
from mne.stats import f_mway_rm, f_threshold_mway_rm, fdr_correction
from mne.time_frequency import tfr_morlet

print(__doc__)
def stat_fun(*args):
    return f_mway_rm(
        np.swapaxes(args, 1, 0),
        factor_levels=factor_levels,
        effects=effects,
        return_pvals=False,
    )[0]


# # The ANOVA returns a tuple f-values and p-values, we will pick the former.
# pthresh = 0.001  # set threshold rather high to save some time
# f_thresh = f_threshold_mway_rm(n_replications, factor_levels, effects, pthresh)
# tail = 1  # f-test, so tail > 0
# n_permutations = 256  # Save some time (the test won't be too sensitive ...)
# F_obs, clusters, cluster_p_values, h0 = mne.stats.permutation_cluster_test(
#     epochs_power,
#     stat_fun=stat_fun,
#     threshold=f_thresh,
#     tail=tail,
#     n_jobs=None,
#     n_permutations=n_permutations,
#     buffer_size=None,
#     out_type="mask",
# )