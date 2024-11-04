# import ants
# import nibabel as nib
# #template = load_mni152_template(resolution=1)
# template = './MNI152_T1_1mm.nii.gz'
# sourcedata = './MDD002/MDD002_t1_mprage_sag_p2_iso_20210520203739_3_Crop_1.nii'
#
# from nilearn.image import resample_to_img
#
# resampled_stat_img = resample_to_img(sourcedata, template)
# nib.Nifti1Image(resampled_stat_img.get_fdata(), resampled_stat_img.affine, resampled_stat_img.header).to_filename('./MDD02_t1_2.nii')
# # 加载源图像和目标图像
# source_image = ants.image_read( './MDD02_t1_2.nii')
# target_image = ants.image_read('./MNI152_T1_1mm.nii.gz')
#
# # 执行配准
# transform = ants.registration(source_image, target_image, type_of_transform='SyN')
#
# # 应用变换到源图像
# registered_image = ants.apply_transforms(source_image, target_image, transformlist=transform['fwdtransforms'])
#
# # 保存配准后的图像
# ants.image_write(registered_image, 'registered_image.nii.gz')

import ants
def registration(fix_path,move_path,save_path,label_path =None,save_label_path = None):
    types = ['Translation', 'Rigid', 'Similarity', 'QuickRigid', 'DenseRigid', 'BOLDRigid', 'Affine', 'AffineFast', 'BOLDAffine',
         'TRSAA', 'ElasticSyN', 'SyN', 'SyNRA', 'SyNOnly', 'SyNCC', 'SyNabp', 'SyNBold', 'SyNBoldAff', 'SyNAggro', 'TVMSQ']
    fix_img = ants.image_read(fix_path)
    move_img = ants.image_read(move_path)
    outs = ants.registration(fix_img,move_img,type_of_transform=types[1])
    reg_img = outs['warpedmovout']
    ants.image_write(reg_img,save_path)
    if label_path != None:
        move_label_img = ants.image_read(move_path)
        reg_label_img = ants.apply_transforms(fix_img,move_label_img,transformlist = out['fwdtransforms'],interpolator='nearestNeighbor')
        ants.image_write(reg_label_img,save_label_path)


fix_path = 'MNI152_T1_1mm.nii.gz'
move_path = './MDD002/MDD002_t1_mprage_sag_p2_iso_20210520203739_3_Crop_1.nii'
save_path = 'reg_2min.nii.gz'
registration(fix_path,move_path,save_path)




