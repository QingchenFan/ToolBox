import nibabel as nib
from nilearn import image
from nilearn import plotting
import matplotlib.pyplot as plt
img1 = nib.load('./c_sub_0001_pcereb.nii')
img2 = nib.load('./Sub_0001_WIP_3DT1W_TFE_sSAG_CS3_20211218183239_301_Crop_1_n4_mni_seg_post_inverse.nii.gz')


# 使用线性配准将img2对齐到img1
aligned_img2 = image.resample_img(img2, target_affine=img1.affine, target_shape=img1.shape)

nib.save(aligned_img2, 'aligned_img2.nii.gz')

# 显示img1和aligned_img2的配准结果
plotting.plot_anat(img1, title="Image 1")
plotting.plot_anat(aligned_img2, title="Aligned Image 2")
plt.show()