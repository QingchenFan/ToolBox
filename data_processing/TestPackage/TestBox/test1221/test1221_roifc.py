import numpy as np
import nibabel as nib
from nilearn import datasets, input_data, connectome

# 加载fMRI数据（示例数据）
dataset = datasets.fetch_development_fmri(n_subjects=1)
print(dataset)

fmri_file = dataset.func[0]
print(fmri_file)
print(input_data)
exit()
# 加载坐标数据（示例数据）
coord = [10, 20, 30]  # 坐标位置

# 创建球形兴趣区（ROI）
masker = input_data.NiftiSpheresMasker(
    seeds=[coord], radius=6, detrend=True, standardize=True)

# 将fMRI数据应用于兴趣区
time_series = masker.fit_transform(fmri_file)

# 计算ROI与整个大脑的相关性
correlation_measure = connectome.ConnectivityMeasure(kind='correlation')
correlation_matrix = correlation_measure.fit_transform([time_series])[0]

# 打印相关性矩阵
print(correlation_matrix)