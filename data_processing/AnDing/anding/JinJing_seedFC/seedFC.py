import os
from nilearn.maskers import NiftiSpheresMasker
from nilearn.maskers import NiftiMasker
import pandas as pd
import glob
import numpy as np
from nilearn import plotting
from nilearn.interfaces.fmriprep import load_confounds


# TODO： 这里修改路径，输入坐标文件csv
coordinate = pd.read_csv('/Users/qingchen/Documents/Dailywork/Lab/AnDing/JJ_seedFC/data_MNI/MDDTargetSpot.csv')

# TODO： 这里修改路径，输入数据路径（*/*.nii 保留）
imgePath = '/Volumes/QCII/Data135_processed/data135_HC_fmriprep_out/*/func/*_task-rest_acq-ap_run-1_space-MNI152NLin6Asym_res-2_desc-preproc_bold.nii.gz'
image = glob.glob(imgePath)

# TODO: 输入mask文件
mask = '/Users/qingchen/Documents/code/Data/FC/GMmask.nii.gz'
# TODO: 这里修改路径，输出数据路径
out = '/Volumes/QCI/JJ_SeedFC/Data135/'

for i in image:
    print(i)
    subID = i.split('/')[-3]
    print(subID)

    confounds_minimal_no_gsr, sample_mask = load_confounds(
        i,
        strategy=[ "motion", "wm_csf", "global_signal"],
        motion="basic",
        wm_csf="basic",
        global_signal="basic",
    )

    for index, row in coordinate.iterrows():
        x = coordinate['x'][index]
        y = coordinate['y'][index]
        z = coordinate['z'][index]

        coords = [(x, y, z)]
        print('coordinate - ',coords)
        # 提取种子点的信号
        seed_masker = NiftiSpheresMasker(
            coords,
            radius=6,
            standardize="zscore_sample",
            standardize_confounds="zscore_sample",
            smoothing_fwhm = 6,
            low_pass = 0.1,
            high_pass = 0.01,
            t_r=2,
            memory_level=1,
            verbose=0,
        )
        seed_time_series = seed_masker.fit_transform(i, confounds=confounds_minimal_no_gsr, sample_mask=sample_mask)

        # 使用mask获取所有体素灰质信息
        brain_masker = NiftiMasker(
            mask_img=mask,
            standardize="zscore_sample",
            standardize_confounds="zscore_sample",
            smoothing_fwhm=6,
            low_pass=0.1,
            high_pass=0.01,
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

        print(
            "Seed-to-voxel correlation shape: (%s, %s)"
            % seed_to_voxel_correlations.shape
        )
        print(
            "Seed-to-voxel correlation: min = %.3f; max = %.3f"
            % (seed_to_voxel_correlations.min(), seed_to_voxel_correlations.max())
        )


        outpath = out + subID
        if not os.path.exists(outpath):
            os.mkdir(outpath)
        exit()
        # 画图
        seed_to_voxel_correlations_img = brain_masker.inverse_transform(
            seed_to_voxel_correlations.T
        )
        display = plotting.plot_stat_map(
            seed_to_voxel_correlations_img,
            threshold=0.2,
            vmax=1,
            cut_coords=coords[0],
            title="Seed-to-voxel correlation",
        )
        display.add_markers(
            marker_coords=coords, marker_color="g", marker_size=300
        )

        # 保存pdf
        display.savefig(outpath + '/' + subID +'_' + str(index) +'_seedtovoxel.pdf')

        seed_to_voxel_correlations_fisher_z = np.arctanh(seed_to_voxel_correlations)
        print(
            "Seed-to-voxel correlation Fisher-z transformed: "
            f"min = {seed_to_voxel_correlations_fisher_z.min():.3f}; "
            f"max = {seed_to_voxel_correlations_fisher_z.max():.3f}"
        )

        seed_to_voxel_correlations_fisher_z_img = brain_masker.inverse_transform(
            seed_to_voxel_correlations_fisher_z.T
        )
        # 保存结果
        seed_to_voxel_correlations_fisher_z_img.to_filename(
            outpath + '/' + subID+'_'+ str(index) + '_seedtovoxel.nii.gz'
        )






