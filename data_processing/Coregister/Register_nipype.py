# reg.inputs.fixed_image = "/Users/qingchen/Desktop/MNI152_T1_2mm_brain.nii.gz"
# reg.inputs.moving_image = "/Users/qingchen/Documents/Dailywork/Lab/AnDing/seedFC/ZY/Amygdala_BNA_SPMAna_rLB.nii"

from nipype.interfaces.fsl import FLIRT
import os

# 定义输入和输出路径
input_img = "/Users/qingchen/Desktop/registertest/Right_Amygdala_LB.nii"
reference_img = "/Users/qingchen/Desktop/MNI152_T1_2mm_brain.nii.gz"
output_img = "/Users/qingchen/Desktop/registertest/Right_Amygdala_LB_to_MNI.nii"

# 配准设置
flirt = FLIRT()
flirt.inputs.in_file = input_img
flirt.inputs.reference = reference_img
flirt.inputs.out_file = output_img

# 运行 FLIRT 配准
flirt.run()

# 检查输出文件
if os.path.exists(output_img):
    print("配准完成，输出文件:", output_img)
else:
    print("配准失败")
