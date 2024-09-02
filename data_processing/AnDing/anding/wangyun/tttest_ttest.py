import glob
from scipy.io import loadmat
from scipy.stats import ttest_ind
import numpy as np
import numpy as np
from scipy.io import loadmat
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import os
import nibabel

# TODO: perm_num=10
def Permutation(HcFC, MddFC,perm_num=1000):
    # 随机生成列索引
    random_indices = np.random.permutation(HcFC.shape[1])
    # # 按列随机打乱
    HcFC_shuffled = HcFC[:, random_indices]
    MddFC_shuffled = MddFC[:, random_indices]
    p_list = []
    for i in range(perm_num):
        print('Permutation - i',i)
        t_stat, p_value = ttest_ind(HcFC_shuffled, MddFC_shuffled)
        p_list.append(p_value)
    return p_list
hcpath = '/Volumes/QCI/wangyun/NAc_rLH_rsFC_core_z/sub-HC*'
HC = glob.glob(hcpath)
HcFC=[]
for i in HC:
    fc = loadmat(i)['data']
    HcFC.append(fc.flatten())

mddpath = '/Volumes/QCI/wangyun/NAc_rLH_rsFC_core_z/sub-MDD*'
MDD = glob.glob(mddpath)
MddFC = []
for i in MDD:
    fc = loadmat(i)['data']
    MddFC.append(fc.flatten())

HcFC = np.array(HcFC)
MddFC = np.array(MddFC)

HcFC[np.isnan(HcFC)] = 0
MddFC[np.isnan(MddFC)] = 0


t_stat, p_list = ttest_ind(HcFC, MddFC)

p_list = np.array(p_list)
print('p_list-',p_list.shape)      #  (64984, 3)

# Load the template gifti file for data storage
img_L = nibabel.load('/Volumes/QCI/wangyun/qingchen/tt.L.midthickness.32k_fs_LR.func.gii') # any gifti file is ok, or"'./area.L.midthickness.32k_fs_LR.func.gii"
img_R = nibabel.load('/Volumes/QCI/wangyun/qingchen/tt.R.midthickness.32k_fs_LR.func.gii')
# Load the vertex area
area_L = nibabel.load('/Volumes/QCI/wangyun/qingchen/area.L.midthickness.32k_fs_LR.func.gii')
vertex_area_L = area_L.agg_data()
area_R = nibabel.load('/Volumes/QCI/wangyun/qingchen/area.R.midthickness.32k_fs_LR.func.gii')
vertex_area_R = area_R.agg_data()

name_list = ['Core_rLH', 'Core_rRH','Shell_rLH','Shell_rRH']
ind = 0
# save the ANOVA result as GIFTI file
name = name_list[0];i=0;
os.system(f'mkdir /Volumes/QCI/wangyun/{name}')
os.system(f'mkdir /Volumes/QCI/wangyun/{name}/perm_surf')

tmp_darray_L = nibabel.gifti.GiftiDataArray(p_list[:32492]*-1,datatype='NIFTI_TYPE_FLOAT32')
tmp_darray_R = nibabel.gifti.GiftiDataArray(p_list[32492:]*-1,datatype='NIFTI_TYPE_FLOAT32')
img_L.darrays = [tmp_darray_L]
img_R.darrays = [tmp_darray_R]
img_L.to_filename(f'/Volumes/QCI/wangyun/{name_list[ind]}/p.L.midthickness.32k_fs_LR.func.gii')
img_R.to_filename(f'/Volumes/QCI/wangyun/{name_list[ind]}/p.R.midthickness.32k_fs_LR.func.gii')
# workbench cluster metric
os.system(f'wb_command -metric-find-clusters /Volumes/QCI/wangyun/fsaverage/fsaverage_LR32k/fsaverage.L.midthickness.32k_fs_LR.surf.gii /Volumes/QCI/wangyun/{name_list[ind]}/p.L.midthickness.32k_fs_LR.func.gii -0.05 20 /Volumes/QCI/wangyun//{name_list[ind]}/cluster.L.midthickness.32k_fs_LR.func.gii')
os.system(f'wb_command -metric-find-clusters /Volumes/QCI/wangyun/fsaverage/fsaverage_LR32k/fsaverage.R.midthickness.32k_fs_LR.surf.gii /Volumes/QCI/wangyun/{name_list[ind]}/p.R.midthickness.32k_fs_LR.func.gii -0.05 20 /Volumes/QCI/wangyun/{name_list[ind]}/cluster.R.midthickness.32k_fs_LR.func.gii')

data = Permutation(HcFC, MddFC)
# TODO:perm_num = 10
perm_num = 1000
for perm in range(perm_num):
    print('--perm--',perm)
    data_tmp = data[perm]
    # save the gifti surface data
    tmp_darray_L = nibabel.gifti.GiftiDataArray(data_tmp[:32492]*-1,datatype='NIFTI_TYPE_FLOAT32')
    tmp_darray_R = nibabel.gifti.GiftiDataArray(data_tmp[32492:]*-1,datatype='NIFTI_TYPE_FLOAT32')

    img_L.darrays = [tmp_darray_L]
    img_R.darrays = [tmp_darray_R]
    img_L.to_filename(f'/Volumes/QCI/wangyun/{name_list[i]}/perm_surf/perm_{perm}.L.midthickness.32k_fs_LR.func.gii')
    img_R.to_filename(f'/Volumes/QCI/wangyun/{name_list[i]}/perm_surf/perm_{perm}.R.midthickness.32k_fs_LR.func.gii')

    # workbench cluster metric
    os.system(f'wb_command -metric-find-clusters /Volumes/QCI/wangyun/fsaverage/fsaverage_LR32k/fsaverage.L.midthickness.32k_fs_LR.surf.gii /Volumes/QCI/wangyun/{name_list[i]}/perm_surf/perm_{perm}.L.midthickness.32k_fs_LR.func.gii -0.05 10 /Volumes/QCI/wangyun/{name_list[i]}/perm_surf/perm_{perm}_cluster.L.midthickness.32k_fs_LR.func.gii')
    os.system(f'wb_command -metric-find-clusters /Volumes/QCI/wangyun/fsaverage/fsaverage_LR32k/fsaverage.R.midthickness.32k_fs_LR.surf.gii /Volumes/QCI/wangyun/{name_list[i]}/perm_surf/perm_{perm}.R.midthickness.32k_fs_LR.func.gii -0.05 10 /Volumes/QCI/wangyun/{name_list[i]}/perm_surf/perm_{perm}_cluster.R.midthickness.32k_fs_LR.func.gii')

# read the permutation result
perm_dict = {}
i=0
tmp_clutser_list = []
for perm in range(1000):

    img_L = nibabel.load(f'/Volumes/QCI/wangyun/{name_list[i]}/perm_surf/perm_{perm}_cluster.L.midthickness.32k_fs_LR.func.gii')
    data_L = img_L.agg_data().astype(int)
    img_R = nibabel.load(f'/Volumes/QCI/wangyun/{name_list[i]}/perm_surf/perm_{perm}_cluster.R.midthickness.32k_fs_LR.func.gii')
    data_R = img_R.agg_data().astype(int)

    max_id_L = int(np.unique(data_L)[-1])
    max_id_R = int(np.unique(data_R)[-1])

    count = []
    count_L = []
    count_R = []
    for k in range(1,max_id_L+1):
        count.append(np.sum((data_L==k)*vertex_area_L))
        count_L.append(np.sum((data_L==k)*vertex_area_L))
    for k in range(1,max_id_R+1):
        count.append(np.sum((data_R==k)*vertex_area_R))
        count_R.append(np.sum((data_R==k)*vertex_area_R))
    max_cluster_size = np.max(count)
    max_cluster_size_L = np.max(count_L)
    max_cluster_size_R = np.max(count_R)
    tmp_clutser_list.append([max_cluster_size_L,max_cluster_size_R])
    perm_dict[f'perm_{name_list[i]}_LR'] = np.array(tmp_clutser_list)

### 4. Print out the cluster-level permutation result
i=0;j=0;
name = name_list[i]

# load the empirical cluster info
img_L = nibabel.load(f'/Volumes/QCI/wangyun/{name_list[ind]}/cluster.L.midthickness.32k_fs_LR.func.gii')
data_L = img_L.agg_data().astype(int)
img_R = nibabel.load(f'/Volumes/QCI/wangyun/{name_list[ind]}/cluster.R.midthickness.32k_fs_LR.func.gii')
data_R = img_R.agg_data().astype(int)
# record the clutser nums: 1-max_id_L/R
max_id_L = int(np.unique(data_L)[-1])
max_id_R = int(np.unique(data_R)[-1])
# cluster size
count = []
count_L = []
count_R = []
for k in range(1,max_id_L+1):
    count.append(np.sum((data_L==k)*vertex_area_L))
    count_L.append(np.sum((data_L==k)*vertex_area_L))
for k in range(1,max_id_R+1):
    count.append(np.sum((data_R==k)*vertex_area_R))
    count_R.append(np.sum((data_R==k)*vertex_area_R))

# p-value list & dict
p_dict = {}
p_L = []
p_R = []
# significant result
sig_dict = {}
sig_L = []
sig_R = []
# significant p-value
sig_L_p = []
sig_R_p = []

corr_map_L = np.zeros(shape=data_L.shape)
corr_map_R = np.zeros(shape=data_R.shape)
for k, elem in enumerate(count_L):
    tmp_p = np.sum(perm_dict[f'perm_{name_list[i]}_LR'][:,0]>elem)/1000*2 # calculate the p-value for the cluster
    p_L.append(tmp_p)
    # keep significant result
    if tmp_p<0.05:
        sig_L.append(k+1)
        corr_map_L = corr_map_L + (data_L==(k+1))*(k+1)
        sig_L_p.append(tmp_p)

for k, elem in enumerate(count_R):
    tmp_p = np.sum(perm_dict[f'perm_{name_list[i]}_LR'][:,1]>elem)/1000*2 # calculate the p-value for the cluster
    p_R.append(tmp_p)
     # keep significant result
    if tmp_p<0.05:
        sig_R.append(k+1)
        corr_map_R = corr_map_R + (data_R==(k+1))*(k+1+max_id_L)
        sig_R_p.append(tmp_p)

# only keep the significant cluster
p_dict['L'] = np.array(p_L)
p_dict['R'] = np.array(p_R)
sig_dict['L'] = np.array(sig_L)
sig_dict['R'] = np.array(sig_R)
p_result = [p_dict,sig_dict]
if (len(sig_L)!=0 or len(sig_R)!=0):
    print(f'{name}',sig_L_p,sig_R_p)
    corr_map_L = np.array(corr_map_L,dtype=int)
    corr_map_R = np.array(corr_map_R,dtype=int)
    tmp_darray_L = nibabel.gifti.GiftiDataArray(corr_map_L,datatype='NIFTI_TYPE_UINT8')
    tmp_darray_R = nibabel.gifti.GiftiDataArray(corr_map_R,datatype='NIFTI_TYPE_UINT8')
    img_L.darrays = [tmp_darray_L]
    img_R.darrays = [tmp_darray_R]
    img_L.to_filename(f'/Volumes/QCI/wangyun/corr_cluster_{name_list[i]}.L.midthickness.32k_fs_LR.func.gii')
    img_R.to_filename(f'/Volumes/QCI/wangyun/corr_cluster_{name_list[i]}.R.midthickness.32k_fs_LR.func.gii')

np.save(f'./p_result_{name}.npy',p_result)