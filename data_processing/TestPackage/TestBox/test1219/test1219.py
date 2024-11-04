
import nibabel as nib
import numpy as np

def extract_roi(coord, radius, image_path):
    # 加载MRI图像
    img = nib.load(image_path)
    data = img.get_fdata()

    # 获取MRI图像的空间信息
    affine = img.affine
    print(affine)
    print(affine[:3, :3])
    voxel_size = np.sqrt(np.sum(affine[:3, :3]**2))
    print('voxel-size--',voxel_size)
    # 将坐标从物理空间转换为图像空间
    coord_voxel = nib.affines.apply_affine(np.linalg.inv(affine), coord)
    print('coord_voxel--', coord_voxel)
    # 计算ROI边界范围
    min_coord = np.floor(coord_voxel - radius / voxel_size).astype(int)
    max_coord = np.ceil(coord_voxel + radius / voxel_size).astype(int)
    print(coord_voxel - radius / voxel_size)
    print('min_coord-',min_coord)
    print('max_coord-', max_coord)
    # 提取ROI区域
    roi_data = data[min_coord[0]:max_coord[0], min_coord[1]:max_coord[1], min_coord[2]:max_coord[2]]
    print('roi_data-',roi_data)
    print('roi_data_shape-',roi_data.shape)
    # 平均ROI
    sroi_data = np.reshape(roi_data, (roi_data.shape[3], roi_data.shape[0] * roi_data.shape[1] * roi_data.shape[2]), order='F')
    print('sroi_data',sroi_data)
    print('sroi_data.shape', sroi_data.shape)
    meanroi_img = np.sum(sroi_data, axis=1) / roi_data.shape[3]
    print('meanroi_img-',meanroi_img.shape)
    # 创建ROI图像
    roi_img = nib.Nifti1Image(roi_data, affine)

    return roi_img, meanroi_img, min_coord, max_coord

# 示例使用
coord = [0, 0, 0]  # 坐标
radius = 6  # 半径（毫米）
#image_path = "./sub-001_task-rest_space-MNI152NLin2009cAsym_desc-residual_smooth_bold.nii.gz"  # MRI图像路径
image_path = './sub-MDD001_task-rest_space-MNI152NLin6Asym_res-2_desc-denoisedSmoothed_bold.nii.gz'
roi = extract_roi(coord, radius, image_path)



nib.Nifti1Image(roi.get_fdata(), roi.affine, roi.header).to_filename('./testROI.nii.gz')

data = roi.get_fdata()
fmri_img = nib.load(image_path).get_fdata()
#print(data)
print(data.shape)
