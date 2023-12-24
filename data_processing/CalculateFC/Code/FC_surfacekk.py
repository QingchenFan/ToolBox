import nibabel as nib
import numpy as np


def find_martrix_min_value(data_matrix):
    '''
    功能：找到矩阵最小值
    '''
    new_data = []
    for i in range(len(data_matrix)):
        new_data.append(min(data_matrix[i]))
    print('data_matrix min:', min(new_data))


def find_martrix_max_value(data_matrix):
    '''
    功能：找到矩阵最大值
    '''
    new_data = []
    for i in range(len(data_matrix)):
        new_data.append(max(data_matrix[i]))
    print('data_matrix max:', max(new_data))
# 读取cifti文件
from scipy.io import savemat
dirc_L = '/Users/qingchen/Documents/code/ToolBox/data_processing/CalculateFC/Code/metric_index_L.txt'
select_ind_L = np.loadtxt(dirc_L).astype(int)

dirc_R = '/Users/qingchen/Documents/code/ToolBox/data_processing/CalculateFC/Code/metric_index_R.txt'
select_ind_R = np.loadtxt(dirc_R).astype(int) + 32492

label = np.concatenate((select_ind_L,select_ind_R), axis=0)
print(label[:50])
#ind=np.zeros(64984).astype(int)
#for i in label:

    #ind[i]=i
#print(np.where(ind==0))

cifti_file = '/Users/qingchen/Documents/code/ToolBox/data_processing/CalculateFC/Code/sub-06202_task-rest_space-fsLR_den-91k_desc-denoisedSmoothed_bold.dtseries.nii'
cifti_img = nib.load(cifti_file).get_fdata()

cifti_img = cifti_img[:,label]
cifti_f=np.zeros((166,64984))
for i in range(0,len(label)):

    cifti_f[:,label[i]]=cifti_img[:,i]
cifti_img=cifti_f

# 获取数据数组和标签数组
cifti_label_path = '/Users/qingchen/Documents/code/ToolBox/data_processing/CalculateFC/Datafc/Schaefer2018_400Parcels_7Networks_order.dlabel.nii'
cifti_label = nib.load(cifti_label_path).get_fdata()

print(cifti_label.shape)



# 获取ROI标签列表
roilist = []
for r in range(1, 401):
    index = np.where(cifti_label == r)

    roi = cifti_img[:, index[1]]  # ROI内所有的voxel

    roiBoldsum=np.mean(roi,axis=1)

    roilist.append(roiBoldsum)
roiMatrix = np.array(roilist)
print(roiMatrix.shape)
resFC = np.corrcoef(roiMatrix)
savemat('/Users/qingchen/Documents/code/ToolBox/data_processing/CalculateFC/Code/sub062021.mat', {'data': resFC})
