import os

from nilearn.interfaces.fmriprep import load_confounds
from nilearn.maskers import NiftiSpheresMasker
from nilearn.maskers import NiftiMasker
import pandas as pd
import glob
import numpy as np
from nilearn import plotting
import matplotlib.pylab as plt
# 使用mask获取所有体素灰质信息
seedmask = 'E:/ZY_SeedFC/rAmygdala_BNA_SPMAna_rLB.nii'

brainmask = 'E:/ZY_SeedFC/GMmask.nii.gz'
outpath = 'E:/ZY_SeedFC/zy_seedFC_BNA_SPMAna_rLB_MDD135/'
imgePath = 'E:/Data_13_5/data135_MDD_fmriprep_out_V1/fmriprep/sub-*/sub-*/func/*_task-rest_acq-ap_run-1_space-MNI152NLin6Asym_res-2_desc-preproc_bold.nii.gz'
#imgePath = 'E:/Data_13_5/duilie_temp/*/*_task-rest_acq-ap_run-1_space-MNI152NLin6Asym_res-2_desc-preproc_bold.nii.gz'
file = glob.glob(imgePath)
for i in file:
    print(i)
    subID = i.split("/")[-1].split("\\")[-3]
    #subID = i.split("/")[-1].split("\\")[1]
    print('subID :',subID)

    confounds_minimal_no_gsr, sample_mask = load_confounds(
        i,
        strategy=[ "motion", "wm_csf", "global_signal"],
        motion="basic",
        wm_csf="basic",
        global_signal="basic",
    )

    seed_masker = NiftiMasker(
        mask_img=seedmask,
        standardize="zscore_sample",
        standardize_confounds="zscore_sample",
        smoothing_fwhm = 6,
        low_pass = 0.1,
        high_pass = 0.01,
        t_r=2,
        memory_level=1,
        verbose=0,
    )
    seed_time_series = seed_masker.fit_transform(i,confounds=confounds_minimal_no_gsr, sample_mask=sample_mask)
    seed_time_series = seed_time_series.mean(axis=1)
    brain_masker = NiftiMasker(
        mask_img=brainmask,
        standardize="zscore_sample",
        standardize_confounds="zscore_sample",
        smoothing_fwhm = 6,
        low_pass = 0.1,
        high_pass = 0.01,
        t_r=2,
        memory_level=1,
        verbose=0,
    )
    brain_time_series = brain_masker.fit_transform(i,confounds=confounds_minimal_no_gsr, sample_mask=sample_mask)

    print(f"Seed time series shape: ({seed_time_series.shape})")
    print(f"Brain time series shape: ({brain_time_series.shape})")

    # 种子点与所有灰质体素计算correlation
    seed_to_voxel_correlations = (
            np.dot(brain_time_series.T, seed_time_series) / seed_time_series.shape[0]
    )
    print(seed_to_voxel_correlations.shape)

    seed_to_voxel_correlations_fisher_z = np.arctanh(seed_to_voxel_correlations)
    print(
        "Seed-to-voxel correlation Fisher-z transformed: "
        f"min = {seed_to_voxel_correlations_fisher_z.min():.3f}; "
        f"max = {seed_to_voxel_correlations_fisher_z.max():.3f}"
    )

    seed_to_voxel_correlations_fisher_z_img = brain_masker.inverse_transform(
        seed_to_voxel_correlations_fisher_z.T
    )

    # 画图
    from nilearn import plotting
    pngpath =  outpath + '/' + subID + '_seedFC.png'
    plotting.plot_stat_map(seed_to_voxel_correlations_fisher_z_img, title='Amygdala-Whole Brain Connectivity',output_file= pngpath)
    #plt.savefig()
    #plotting.show()


    #

    seed_to_voxel_correlations_fisher_z = np.arctanh(seed_to_voxel_correlations)
    print(
        "Seed-to-voxel correlation Fisher-z transformed: "
        f"min = {seed_to_voxel_correlations_fisher_z.min():.3f}; "
        f"max = {seed_to_voxel_correlations_fisher_z.max():.3f}"
    )
    # # 保存结果
    seed_to_voxel_correlations_fisher_z_img.to_filename(
        outpath + '/' + subID + '_seedtovoxel.nii.gz'
    )

#seed_to_voxel_correlations_img = brain_masker.inverse_transform(
#     seed_to_voxel_correlations.T
# )
# display = plotting.plot_stat_map(
#     seed_to_voxel_correlations_img,
#     threshold=0.2,
#     vmax=1,
#     title="Seed-to-voxel correlation",
# )
# display.add_markers(
#      marker_color="g", marker_size=300
# )
#
# # 保存pdf
# display.savefig('./test_seedtovoxel.pdf')
