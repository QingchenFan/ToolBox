from nilearn import plotting
from nilearn.datasets import load_mni152_template

# # 指定 MNI 坐标
# mni_coords = [-48, 28, 10]
#
# # 加载 MNI152 模板
# template = load_mni152_template()
#
# # 显示坐标点在标准模板上的位置
# plotting.plot_anat(template, display_mode='ortho', cut_coords=mni_coords,
#                    title="MNI Coordinate (-48, 28, 10)", draw_cross=True)
# plotting.show()
# --------- ---------------------------------------
# from nilearn import plotting
# from nilearn.datasets import load_mni152_template
#
# # 指定 MNI 坐标
# mni_coords = [-48, 28, 10]  # 小球中心坐标
#
# # 加载 MNI152 模板
# template = load_mni152_template()
#
# # 创建可视化
# display = plotting.plot_anat(template, display_mode='ortho', title="MNI Coordinate with Sphere",
#                              cut_coords=mni_coords)
#
# # 添加小球体标记
# display.add_markers(marker_coords=[mni_coords], marker_color='red', marker_size=100)
#
# # 显示结果
# plotting.show()
# --------------------------------------------
from nilearn import plotting, image
from nilearn.datasets import load_mni152_template
import numpy as np

# 指定 MNI 坐标和半径
mni_coords = [-48, 28, 10]  # 小球中心坐标
radius = 5  # 半径（单位：毫米）

# 加载 MNI152 模板
template = load_mni152_template()

# 创建一个空的图像与模板相同的形状
sphere_img_data = np.zeros(template.shape)

# 将 MNI 坐标转换为体素坐标
affine = template.affine
voxel_coords = np.round(np.linalg.inv(affine).dot(np.array(mni_coords + [1]))[:-1]).astype(int)

# 获取球体范围
x, y, z = np.ogrid[:sphere_img_data.shape[0], :sphere_img_data.shape[1], :sphere_img_data.shape[2]]
sphere_mask = (x - voxel_coords[0])**2 + (y - voxel_coords[1])**2 + (z - voxel_coords[2])**2 <= (radius / np.abs(affine[0, 0]))**2

# 将球体区域填充为1
sphere_img_data[sphere_mask] = 1

# 创建图像
sphere_img = image.new_img_like(template, sphere_img_data)

# 创建 3D 交互式视图
view = plotting.view_img(sphere_img, bg_img=template, threshold=0.1, cmap='autumn', opacity=0.7)

# 保存为 HTML 文件
view.save_as_html('mni_3d_sphere.html')





