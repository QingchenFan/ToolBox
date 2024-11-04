import nibabel as nib
from nilearn import datasets
from nilearn.connectome import ConnectivityMeasure
from nilearn.maskers import NiftiLabelsMasker
from scipy.io import savemat

template = './Schaefer2018_400Parcels_17Networks_order.dlabel.nii'
templateData = nib.load(template)
#  --  加载schaefer template (可设置参数选择合适的模板)
# schaefer_400 = datasets.fetch_atlas_schaefer_2018(n_rois=400, resolution_mm=2)
# atlas_filename = schaefer_400.maps
# labels = schaefer_400.labels

masker = NiftiLabelsMasker(
    labels_img=templateData,
    #labels = labels,
    standardize="zscore_sample",
    standardize_confounds="zscore_sample",
    memory="nilearn_cache",
    verbose=5,
)

boldpath = './sub-100206_task-REST1_dir-LR_space-fsLR_den-91k_desc-denoisedSmoothed_bold.dtseries.nii'
a = nib.load(boldpath).get_fdata()
print(a)
print(a.shape)
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

savemat('./sub100206_fcsurface.mat', {'data': correlation_matrix})