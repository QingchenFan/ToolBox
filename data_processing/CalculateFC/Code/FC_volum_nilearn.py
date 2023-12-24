import nibabel as nib
from nilearn import datasets
from nilearn.connectome import ConnectivityMeasure
from nilearn.maskers import NiftiLabelsMasker
# template = './Schaefer2018_400Parcels_7Networks_order_FSLMNI152_2mm.nii.gz'
# templateData = nib.load(template)
#  --  加载schaefer template (可设置参数选择合适的模板)
schaefer_400 = datasets.fetch_atlas_schaefer_2018(n_rois=400, resolution_mm=2)
atlas_filename = schaefer_400.maps
labels = schaefer_400.labels



masker = NiftiLabelsMasker(
    labels_img=atlas_filename,
    labels = labels,
    standardize="zscore_sample",
    standardize_confounds="zscore_sample",
    memory="nilearn_cache",
    verbose=5,
)

boldpath = './sub-MDD001_task-rest_space-MNI152NLin6Asym_res-2_desc-denoisedSmoothed_bold.nii.gz'

# Here we go from nifti files to the signal time series in a numpy
# array. Note how we give confounds to be regressed out during signal
# extraction
time_series = masker.fit_transform(boldpath)



correlation_measure = ConnectivityMeasure(
    kind="correlation",
    #standardize="zscore_sample",
)
correlation_matrix = correlation_measure.fit_transform([time_series])[0]

print(correlation_matrix)
print(correlation_matrix.shape)

# # Plot the correlation matrix
import numpy as np

from nilearn import plotting

# Make a large figure
# Mask the main diagonal for visualization:
#np.fill_diagonal(correlation_matrix, 0)
# The labels we have start with the background (0), hence we skip the
# first label
# matrices are ordered for block-like representation
plotting.plot_matrix(
    correlation_matrix,
    figure=(10, 8),
    labels=labels,
    vmax=0.8,
    vmin=-0.8,
    #title="Confounds",
    reorder=True,
)
plotting.show()