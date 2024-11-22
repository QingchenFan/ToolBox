import pandas as pd
import glob
import nibabel as nib
from scipy.stats import norm
from nilearn.glm.second_level import SecondLevelModel
import matplotlib.pyplot as plt
from nilearn import plotting
data = glob.glob('/Volumes/QCI/ZY/zy_seedFC_all_data135/*.nii.gz')
second_level_input = data
design_matrix = pd.DataFrame(
    [1] * len(second_level_input),
    columns=["intercept"],
)


second_level_model = SecondLevelModel(smoothing_fwhm=8.0, n_jobs=2)
second_level_model = second_level_model.fit(
    second_level_input,
    design_matrix=design_matrix,
)

z_map = second_level_model.compute_contrast(
    second_level_contrast="intercept",
    output_type="z_score",
)


p_val = 0.001
p001_unc = norm.isf(p_val)
display = plotting.plot_glass_brain(
    z_map,
    threshold=p001_unc,
    colorbar=True,
    display_mode="z",
    plot_abs=False,
    title="group left-right button press (unc p<0.001)",
    figure=plt.figure(figsize=(5, 5)),
)
plotting.show()

import numpy as np

from nilearn.image import get_data, math_img

p_val = second_level_model.compute_contrast(output_type="p_value")
n_voxels = np.sum(get_data(second_level_model.masker_.mask_img_))
# Correcting the p-values for multiple testing and taking negative logarithm
neg_log_pval = math_img(
    f"-np.log10(np.minimum(1, img * {n_voxels!s}))",
    img=p_val,
)

from nilearn.glm.second_level import non_parametric_inference

out_dict = non_parametric_inference(
    second_level_input,
    design_matrix=design_matrix,
    model_intercept=True,
    n_perm=500,  # 500 for the sake of time. Ideally, this should be 10,000.
    two_sided_test=False,
    smoothing_fwhm=8.0,
    n_jobs=2,
    threshold=0.001,
)