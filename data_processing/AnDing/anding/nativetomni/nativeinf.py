import nibabel as nib

# 加载NIfTI图像
nifti_file = './MDD002/MDD002_t1_mprage_sag_p2_iso_20210520203739_3_Crop_1.nii'
nii = nib.load(nifti_file)

# 获取空间坐标信息
voxel_size = nii.header.get_zooms()[:3]  # 获取体素尺寸
origin = nii.header.get_sform()[:3, 3]  # 获取原点坐标

# 打印空间坐标信息
print('Voxel size:', voxel_size)
print('Origin:', origin)