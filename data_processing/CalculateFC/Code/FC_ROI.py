import glob

import nibabel as nib
import numpy as np
import pandas as pd
from scipy.io import savemat


def extract_roi(coord, radius, image_path):
    # 加载MRI图像
    img = nib.load(image_path)
    data = img.get_fdata()

    # 获取MRI图像的空间信息
    affine = img.affine
    voxel_size = np.sqrt(np.sum(affine[:3, :3]**2))

    # 将坐标从物理空间转换为图像空间
    coord_voxel = nib.affines.apply_affine(np.linalg.inv(affine), coord)

    # 计算ROI边界范围
    min_coord = np.floor(coord_voxel - radius / voxel_size).astype(int)
    max_coord = np.ceil(coord_voxel + radius / voxel_size).astype(int)

    # 提取ROI区域
    roi_data = data[min_coord[0]:max_coord[0], min_coord[1]:max_coord[1], min_coord[2]:max_coord[2]]

    # 平均ROI
    sroi_data = np.reshape(roi_data, (roi_data.shape[3], roi_data.shape[0] * roi_data.shape[1] * roi_data.shape[2]), order='F')
    meanroi_img = np.sum(sroi_data, axis=1) / roi_data.shape[3]

    # 创建ROI图像
    roi_img = nib.Nifti1Image(roi_data, affine)

    return roi_img, meanroi_img, min_coord, max_coord


loc = pd.read_csv('/Users/qingchen/Documents/Dailywork/Lab/AnDing/6mmFC/MDDTargetSpot.csv')

imgePath = '/Users/qingchen/Documents/Dailywork/Lab/AnDing/6mmFC/sub-MDD47*'

image = glob.glob(imgePath)

for i in image:
    print(i)
    # id = i[i.index('MDD'):i.index('MDD')+6]
    # f = loc.loc[loc['ID'] == id]
    #
    # x = f['MNI'][0].split(',')[0]
    # y = f['MNI'][0].split(',')[1]
    # z = f['MNI'][0].split(',')[2]
    # coord = [x, y, z]
    coord = [10, 20, 30]
    radius = 6

    roi_img, meanroi_img, min_coord, max_coord = extract_roi(coord, radius, i)
    data = nib.load(i).get_fdata()
    print(data.shape)
    #data[min_coord[0]:max_coord[0], min_coord[1]:max_coord[1], min_coord[2]:max_coord[2]] = 0
    data = np.reshape(data, (data.shape[3], data.shape[0] * data.shape[1] * data.shape[2]), order='F')

    box = []
    for j in range(data.shape[1]):
        meanroi_img = np.transpose(meanroi_img)
        if (data[:,j] == 0).all() :
            continue
        Corr = np.corrcoef(meanroi_img, data[:,j])
        Corr = Corr[0, 1]
        box.append(Corr)
    #print(box)
    res = np.array(box)
    print(res.shape)
    #savemat('./roiMatrix_test.mat', {'data': res})




