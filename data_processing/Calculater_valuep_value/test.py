import scipy.io as scio
import pingouin as pg
import pandas as pd
data = scio.loadmat('/Users/fan/Documents/Code/source_data_hyl/reviewwork/data/Python_test_wm_connect_vs_distance_0129/sub_01_data.mat')
#data = scio.loadmat('/Users/fan/Documents/Code/source_data_hyl/reviewwork/FDR/data/SEEG_BOLD_DSI_vector_for_calcu_corr/sub_01_data.mat')
print(data)
exit()
print(data['seeg_bold'])
print(data['seeg_bold'].shape)

data1 = data['seeg_bold'][0][0][0].tolist()
print('data1:\n',data1)

data1 = pd.DataFrame(data1, columns=['c1'])

data2 = data['seeg_bold'][0][0][1].tolist()
print('data2:\n',data2)
data2 = pd.DataFrame(data2, columns=['c2'])

data3 = data['seeg_bold'][0][0][0].tolist()
#print('data3:\n',data3)
data3 = pd.DataFrame(data3, columns=['c3'])

temp = pd.concat([data1, data2], axis=1)
res = pd.concat([temp, data3], axis=1)

print(res)
resCovari = pg.partial_corr(data=res, x='c1', y='c2', covar=['c3'], method='spearman')
print(resCovari)