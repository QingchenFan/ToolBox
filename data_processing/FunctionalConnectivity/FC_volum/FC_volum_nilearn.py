'''
    https://nilearn.github.io/dev/index.html
    https://nilearn.github.io/dev/auto_examples/03_connectivity/plot_signal_extraction.html#extracting-signals-from-a-brain-parcellation
    Volume space functional connectivity
'''
import nibabel as nib
from nilearn import datasets
from nilearn.connectome import ConnectivityMeasure
from nilearn.maskers import NiftiLabelsMasker
from nilearn import plotting


def correlation_matrix(atlas_filename,labels,bolddata):
    masker = NiftiLabelsMasker(
        labels_img=atlas_filename,
        labels = labels,
        #standardize="zscore_sample",
        #standardize_confounds="zscore_sample",
        memory="nilearn_cache",
        verbose=5,
    )

    time_series = masker.fit_transform(bolddata)
    correlation_measure = ConnectivityMeasure(
        kind="correlation",
        #standardize="zscore_sample",
    )
    correlation_matrix = correlation_measure.fit_transform([time_series])[0]

    print('correlation_matrix dim :',correlation_matrix.shape)

    return correlation_matrix
def plot_correlation_matrix(correlation_matrix,labels):
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
# Example

schaefer_400 = datasets.fetch_atlas_schaefer_2018(n_rois=400, resolution_mm=2)  # 加载 schaefer template (可设置参数选择合适的模板)，可以选择nilearn自带template，也可以自己加载所需要的template
atlas_filename = schaefer_400.maps                                              # atlas_filename  模板数据的路径 string
labelsname = schaefer_400.labels                                                    # labels 模板的标签 list

bolddata = '/Users/qingchen/Documents/code/Data/roi_fc/sub-0062_task-rest_space-MNI152NLin6Asym_res-2_desc-denoisedSmoothed_bold.nii.gz'

correlation_matrix = correlation_matrix(atlas_filename,labelsname,bolddata)
plot_correlation_matrix(correlation_matrix,labelsname)

