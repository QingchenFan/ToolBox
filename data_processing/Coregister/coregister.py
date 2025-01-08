
import ants

# 读取标准空间模板和种子点mask
# standard_image = ants.image_read('/Users/qingchen/Documents/Data/template/MNITemplate-master/inst/extdata/MNI152_T1_2mm_Brain_Mask.nii')
# seed_mask = ants.image_read('/Users/qingchen/Desktop/ZY/Amygdala_all.nii')
# 读取标准空间模板和种子点mask
standard_image = ants.image_read("/Users/qingchen/Desktop/MNI152_T1_2mm_brain.nii.gz")
#seed_mask = ants.image_read('/Users/qingchen/Desktop/sub-HC029V01_T1w.nii')
seed_mask = ants.image_read("/Users/qingchen/Desktop/registertest/Right_Amygdala_LB.nii")
# 进行配准
transform = ants.registration(fixed=standard_image, moving=seed_mask, type_of_transform='SyN')

# 应用变换
registered_mask = ants.apply_transforms(fixed=standard_image, moving=seed_mask, transformlist=transform['fwdtransforms'], interpolator='nearestNeighbor')

# 保存结果
ants.image_write(registered_mask, "/Users/qingchen/Desktop/registertest/Right_Amygdala_LB_to_MNI.nii")
