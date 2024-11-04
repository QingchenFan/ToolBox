import os
from nilearn.maskers import NiftiSpheresMasker
from nilearn.maskers import NiftiMasker
import pandas as pd
import glob
import numpy as np
from nilearn import plotting
'''
 1、一共修改路径4处
    a.csv文件路径
    b.影像数据路径
    c.mask文件路径
 2、本代码使用先验概率图谱，卡阈值0.2生成二值化图谱  
'''

# TODO： 这里修改路径，输入坐标文件csv
loc = pd.read_csv('/Users/qingchen/Documents/Dailywork/Lab/AnDing/6mmFC/MDDTargetSpot.csv')
# TODO: 输入数据，修改为：/xxx/xxx/xx/*/*  (保留/*/*)
imgePath = '/Users/qingchen/Desktop/test/*/*'
imgePath = '/Users/qingchen/Documents/Dailywork/Lab/AnDing/JJ_seed2roi/check_FC_qingcheng/check_data/pre/session4/*/*'
image = glob.glob(imgePath)

# TODO: 输入mask文件
mask = '/Users/qingchen/Documents/code/Data/FC/GMmask.nii.gz'


for i in image:
    print(i)
    # 获取被试ID
    id = i[-10:-4]
    # 获取坐标信息
    f = loc.loc[loc['ID'] == id]
    x = round(eval(f['MNI'].tolist()[0].split(',')[0]))
    y = round(eval(f['MNI'].tolist()[0].split(',')[1]))
    z = round(eval(f['MNI'].tolist()[0].split(',')[2]))
    coords = [(x, y, z)]
    # 提取种子点的信号
    seed_masker = NiftiSpheresMasker(
        coords,
        radius=6,
        standardize="zscore_sample",
        standardize_confounds="zscore_sample",
        t_r=2,
        memory_level=1,
        verbose=0,
    )
    seed_time_series = seed_masker.fit_transform(i)


    # 使用mask获取所有体素灰质信息
    brain_masker = NiftiMasker(
        mask_img=mask,
        standardize="zscore_sample",
        standardize_confounds="zscore_sample",
        t_r=2,
        memory_level=1,
        verbose=0,
    )

    brain_time_series = brain_masker.fit_transform(i)

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



    # 保存输出数据路径 # TODO:输出数据路径"/Users/qingchen/Desktop/out/"替换掉
    outpath = '/Users/qingchen/Desktop/out/' + id
    if not os.path.exists(outpath):
        os.mkdir(outpath)

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
    display.savefig(outpath +'/'+id+'_seedtovoxel.pdf')

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
        outpath +'/'+id+'_seedtovoxel.nii.gz'
    )



