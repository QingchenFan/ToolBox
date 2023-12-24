import nibabel as nib

path = '/Users/fan/Documents/Datafc/HCPData/HCPDtest/sub-HCD0001305_task-rest_space-MNI152NLin6Asym_desc-residual_smooth_bold.nii.gz'

# import nibabel as nib
#
# # 加载NIfTI文件
# img = nib.load(path)
#
# # 获取数据头
# header = img.header
# print('header--\n', header)
#
# # 获取切片数量
# num_slices = header.get_data_shape()[2]
# print('header.get_data_shape()\n', header.get_data_shape())
# print('num_slices--\n', num_slices)
#
# # 获取每个切片之间的时间间隔
# slice_duration = header.get_zooms()[2]
# print('header.get_zooms()()\n', header.get_zooms())
# print('slice_duration--\n', slice_duration)
#
# # 获取第一张图像的时间偏移量
# toffset = header.get_data_offset()
# print('header.get_time_offset()\n', header.get_data_offset())
# print('toffset--\n', toffset)
#
# # 计算每张图像的扫描时间
# for i in range(num_slices):
#     time = toffset + i * slice_duration
#     print("Scan time for slice ", i+1, ": ", time)
#

import nibabel as nib

# 加载nifti文件
img = nib.load(path)

# 获取TR和切片顺序信息
tr = img.header['pixdim'][4]
print(tr)
slice_order = img.header.get_slice_times()

# 计算每个切片的时间
num_slices = img.shape[2]
slice_timing = [(slice_order[i] - 1) * tr / num_slices for i in range(num_slices)]