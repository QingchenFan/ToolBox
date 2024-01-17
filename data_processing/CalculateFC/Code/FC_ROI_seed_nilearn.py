from nilearn.maskers import NiftiSpheresMasker
import nibabel as nib
from nilearn.maskers import NiftiMasker
import pandas as pd
import glob
import numpy as np
loc = pd.read_csv('/Users/qingchen/Documents/Dailywork/Lab/AnDing/6mmFC/MDDTargetSpot.csv')

imgePath = '/Users/qingchen/Documents/Dailywork/Lab/AnDing/6mmFC/sub-HC010*_bold*'
image = glob.glob(imgePath)

for i in image:
    print(i)
    coords = [(10, 20, 30)]
    seed_masker = NiftiSpheresMasker(
        coords,
        radius=2,
        standardize="zscore_sample",
        standardize_confounds="zscore_sample",
        t_r=2,
        memory_level=1,
        verbose=0,
    )
    seed_time_series = seed_masker.fit_transform(i)

    maskpath = '/Users/qingchen/Documents/Dailywork/Lab/AnDing/6mmFC/sub-001_task-rest_space-MNI152NLin6Asym_desc-brain_mask.nii.gz'
    brain_masker = NiftiMasker(
        mask_img=maskpath,
        standardize="zscore_sample",
        standardize_confounds="zscore_sample",
        t_r=2,
        memory_level=1,
        verbose=0,
    )

    brain_time_series = brain_masker.fit_transform(i)

    print(f"Seed time series shape: ({seed_time_series.shape})")
    print(f"Brain time series shape: ({brain_time_series.shape})")



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

    from nilearn import plotting

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
    # At last, we save the plot as pdf.
    display.savefig("./seed_correlation.pdf")

    seed_to_voxel_correlations_fisher_z = np.arctanh(seed_to_voxel_correlations)
    print(
        "Seed-to-voxel correlation Fisher-z transformed: "
        f"min = {seed_to_voxel_correlations_fisher_z.min():.3f}; "
        f"max = {seed_to_voxel_correlations_fisher_z.max():.3f}"
    )

    seed_to_voxel_correlations_fisher_z_img = brain_masker.inverse_transform(
        seed_to_voxel_correlations_fisher_z.T
    )
    # seed_to_voxel_correlations_fisher_z_img.to_filename(
    #     "./seed_correlation_z.nii.gz"
    # )



