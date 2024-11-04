import nibabel as nib
from nibabel.processing import resample_from_to
import numpy as np
# 加载需要配准的两个数据文件
fixed_image = nib.load('./c_sub_0001_pcereb.nii')
moving_image = nib.load('./Sub_0001_WIP_3DT1W_TFE_sSAG_CS3_20211218183239_301_Crop_1_n4_mni_seg_post_inverse.nii.gz')



# 使用线性变换对移动图像进行配准
from nibabel.affines import (
    apply_affine,
    from_matvec,
    to_matvec,
)

# 创建一个3x3的单位矩阵
mat = np.eye(3)

# 指定需要进行的配准方法
transform = from_matvec(mat, np.array([0, 0, 0]))
print(transform)
# 进行配准，获取配准后的移动图像
resampled = resample_from_to(moving_image, fixed_image)
# 将配准后的移动图像保存为NIfTI格式
nib.save(resampled, 'resampledmaks.nii.gz')