import numpy as np
from scipy.io import loadmat
import pandas as pd
import statsmodels.formula.api as smf 
import statsmodels.api as sm 
import os
import nibabel

### Only two things need to be changes:
### 1. the smf formula (specified for the ANCOVA factors)
### 2. the file path to read and save

# Permutation for ANCOVA analysis
def Permutation(FC,info,perm_num=1000):
    np.random.seed(999)
    sub_num = FC.shape[0]
    perm_result=[]
    for perm_id in range(perm_num):
        shuffle_id = np.arange(sub_num)
        np.random.shuffle(shuffle_id)
        FC_perm = FC[shuffle_id,:]
        p_list = []
        for i in range(FC.shape[1]):
            ana = smf.ols(' FC_perm[:,i] ~ diagnosis*age_group+sex+FD', data=info).fit() 
            # anova_lm:多因素方差分析 
            result = sm.stats.anova_lm(ana)
            result = result[:3]
            f_score_tmp = np.array(result['F'])
            p_tmp = np.array(result['PR(>F)'])
            p_list.append(p_tmp)
        p_list = np.array(p_list)
        perm_result.append(p_list)
    return perm_result

### 1. Load the dataset
### 1.1 Load the subjects' information
info = pd.read_excel('./participants_info_withFD.xlsx')
info['group'] = info['diagnosis']+2*info['age_group']-3 # encode the group info
# 0: young_MDD
# 1: young_HC
# 2: adult_MDD
# 3: adult_HC

### 1.2 Load FC data
# Take CM_L FC data for demo
name_list = ['CM_L', 'CM_R','LB_L','LB_R','SF_L','SF_R']
ind = 0
FC=[]
for elem in info[info['group']==1]['subject']:
    fc = loadmat(f'./guanling/young/HC_Amygdala_{name_list[ind]}_FC/sub-{elem}_AMGYDALA_{name_list[ind]}_FC.mat')['data']
    FC.append(fc.flatten())

for elem in info[info['group']==0]['subject']:
    fc = loadmat(f'./guanling/young/MDD_Amygdala_{name_list[ind]}_FC/sub-{elem}_AMGYDALA_{name_list[ind]}_FC.mat')['data']
    FC.append(fc.flatten())

for elem in info[info['group']==3]['subject']:
    fc = loadmat(f'./guanling/adult/HC_Amygdala_{name_list[ind]}_FC/sub-{elem}_AMGYDALA_{name_list[ind]}_FC.mat')['data']
    FC.append(fc.flatten())

for elem in info[info['group']==2]['subject']:
    fc = loadmat(f'./guanling/adult/MDD_Amygdala_{name_list[ind]}_FC/sub-{elem}_AMGYDALA_{name_list[ind]}_FC.mat')['data']
    FC.append(fc.flatten())

FC=np.array(FC)

### 2. Empirical ANCOVA for the age & dignosis factor
FC[np.isnan(FC)] = 0 # replace nan with zeros

### 2.1 ANOVA analysis (p-value kept)
p_list = []
for i in range(FC.shape[1]):
    # Main Factors: diagnosis + age + diagnosis*age
    # Nuisance Factor: sex + FD
    ana = smf.ols(' FC[:,i] ~ diagnosis*age_group+sex+FD', data=info).fit() 
    # anova_lm implents the multi-factor ANOVA

    result = sm.stats.anova_lm(ana)
    result = result[:3] # only keep the main factor result
    f_score_tmp = np.array(result['F'])
    p_tmp = np.array(result['PR(>F)'])
    p_list.append(p_tmp)
p_list = np.array(p_list)
print('p_list :',p_list.shape)
exit()
# Load the template gifti file for data storage
img_L = nibabel.load('/Volumes/QCI/wangyun/qingchen/tt.L.midthickness.32k_fs_LR.func.gii') # any gifti file is ok, or"'./area.L.midthickness.32k_fs_LR.func.gii"
img_R = nibabel.load('/Volumes/QCI/wangyun/qingchen/tt.R.midthickness.32k_fs_LR.func.gii')
# Load the vertex area
area_L = nibabel.load('/Volumes/QCI/wangyun/qingchen/area.L.midthickness.32k_fs_LR.func.gii')
vertex_area_L = area_L.agg_data()
area_R = nibabel.load('/Volumes/QCI/wangyun/qingchen/area.R.midthickness.32k_fs_LR.func.gii')
vertex_area_R = area_R.agg_data()
# save the ANOVA result as GIFTI file
tmp_darray_L = nibabel.gifti.GiftiDataArray(p_list[:32492]*-1,datatype='NIFTI_TYPE_FLOAT32')
tmp_darray_R = nibabel.gifti.GiftiDataArray(p_list[32492:]*-1,datatype='NIFTI_TYPE_FLOAT32')
img_L.darrays = [tmp_darray_L]
img_R.darrays = [tmp_darray_R]
img_L.to_filename(f'./guanling/{name_list[ind]}/p.L.midthickness.32k_fs_LR.func.gii')
img_R.to_filename(f'./guanling/{name_list[ind]}/p.R.midthickness.32k_fs_LR.func.gii')
# workbench cluster metric
os.system(f'wb_command -metric-find-clusters /n01dat01/cswang/Master/Data/atlas/fsaverage/fsaverage_LR32k/fsaverage.L.midthickness.32k_fs_LR.surf.gii /n01dat01/cswang/Master/anding/guanling/{name_list[ind]}/p.L.midthickness.32k_fs_LR.func.gii -0.05 20 /n01dat01/cswang/Master/anding/guanling/{name_list[ind]}/cluster.L.midthickness.32k_fs_LR.func.gii')
os.system(f'wb_command -metric-find-clusters /n01dat01/cswang/Master/Data/atlas/fsaverage/fsaverage_LR32k/fsaverage.R.midthickness.32k_fs_LR.surf.gii /n01dat01/cswang/Master/anding/guanling/{name_list[ind]}/p.R.midthickness.32k_fs_LR.func.gii -0.05 20 /n01dat01/cswang/Master/anding/guanling/{name_list[ind]}/cluster.R.midthickness.32k_fs_LR.func.gii')

### 3. Permutation ANCOVA
prefix = ['diag','age','mul_diag_age','sex']
perm_num = 1000
# Take diagnosis effect for demo use
name = name_list[0];i=0;
data = Permutation(FC,info)
os.system(f'mkdir ./{name}')
os.system(f'mkdir ./{name}/perm_surf')
for perm in range(perm_num):
    data_tmp = data[perm,:,:].T

    j=0; # diagnosis
    # save the gifti surface data
    tmp_darray_L = nibabel.gifti.GiftiDataArray(data_tmp[j][:32492]*-1,datatype='NIFTI_TYPE_FLOAT32')
    tmp_darray_R = nibabel.gifti.GiftiDataArray(data_tmp[j][32492:]*-1,datatype='NIFTI_TYPE_FLOAT32')
    img_L.darrays = [tmp_darray_L]
    img_R.darrays = [tmp_darray_R]
    img_L.to_filename(f'./guanling/{name_list[i]}/perm_surf/perm_{perm}_{prefix[j]}.L.midthickness.32k_fs_LR.func.gii')
    img_R.to_filename(f'./guanling/{name_list[i]}/perm_surf/perm_{perm}_{prefix[j]}.R.midthickness.32k_fs_LR.func.gii')

    # workbench cluster metric
    os.system(f'wb_command -metric-find-clusters /n01dat01/cswang/Master/Data/atlas/fsaverage/fsaverage_LR32k/fsaverage.L.midthickness.32k_fs_LR.surf.gii /n01dat01/cswang/Master/anding/guanling/{name_list[i]}/perm_surf/perm_{perm}_{prefix[j]}.L.midthickness.32k_fs_LR.func.gii -0.05 20 /n01dat01/cswang/Master/anding/guanling/{name_list[i]}/perm_surf/perm_{perm}_cluster_{prefix[j]}.L.midthickness.32k_fs_LR.func.gii')
    os.system(f'wb_command -metric-find-clusters /n01dat01/cswang/Master/Data/atlas/fsaverage/fsaverage_LR32k/fsaverage.R.midthickness.32k_fs_LR.surf.gii /n01dat01/cswang/Master/anding/guanling/{name_list[i]}/perm_surf/perm_{perm}_{prefix[j]}.R.midthickness.32k_fs_LR.func.gii -0.05 20 /n01dat01/cswang/Master/anding/guanling/{name_list[i]}/perm_surf/perm_{perm}_cluster_{prefix[j]}.R.midthickness.32k_fs_LR.func.gii')

# read the permutation result
perm_dict = {}
i=0;j=0; # diagnosis demo
tmp_clutser_list = []
for perm in range(1000):
    img_L = nibabel.load(f'./guanling/{name_list[i]}/perm_surf/perm_{perm}_cluster_{prefix[j]}.L.midthickness.32k_fs_LR.func.gii')
    data_L = img_L.agg_data().astype(int)
    img_R = nibabel.load(f'./guanling/{name_list[i]}/perm_surf/perm_{perm}_cluster_{prefix[j]}.R.midthickness.32k_fs_LR.func.gii')
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
    perm_dict[f'perm_{name_list[i]}_{prefix[j]}_LR'] = np.array(tmp_clutser_list)

### 4. Print out the cluster-level permutation result
i=0;j=0;
name = name_list[i]

# load the empirical cluster info
img_L = nibabel.load(f'./guanling/{name_list[ind]}/cluster.L.midthickness.32k_fs_LR.func.gii')
data_L = img_L.agg_data().astype(int)
img_R = nibabel.load(f'./guanling/{name_list[ind]}/cluster.R.midthickness.32k_fs_LR.func.gii')
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
    tmp_p = np.sum(perm_dict[f'perm_{name_list[i]}_{prefix[j]}_LR'][:,0]>elem)/1000*2 # calculate the p-value for the cluster
    p_L.append(tmp_p)
    # keep significant result
    if tmp_p<0.05:
        sig_L.append(k+1)
        corr_map_L = corr_map_L + (data_L==(k+1))*(k+1)
        sig_L_p.append(tmp_p)

for k, elem in enumerate(count_R):
    tmp_p = np.sum(perm_dict[f'perm_{name_list[i]}_{prefix[j]}_LR'][:,1]>elem)/1000*2 # calculate the p-value for the cluster
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
    print(f'{name}_{prefix[j]}',sig_L_p,sig_R_p)
    corr_map_L = np.array(corr_map_L,dtype=int)
    corr_map_R = np.array(corr_map_R,dtype=int)
    tmp_darray_L = nibabel.gifti.GiftiDataArray(corr_map_L,datatype='NIFTI_TYPE_UINT8')
    tmp_darray_R = nibabel.gifti.GiftiDataArray(corr_map_R,datatype='NIFTI_TYPE_UINT8')
    img_L.darrays = [tmp_darray_L]
    img_R.darrays = [tmp_darray_R]
    img_L.to_filename(f'./guanling/corr_cluster_{name_list[i]}_{prefix[j]}.L.midthickness.32k_fs_LR.func.gii')
    img_R.to_filename(f'./guanling/corr_cluster_{name_list[i]}_{prefix[j]}.R.midthickness.32k_fs_LR.func.gii')

np.save(f'./p_result_{name}_{prefix[j]}.npy',p_result)
