import numpy as np
from sympy.stats import FisherZ

# #              a  b   c
# a = np.array([[1, 2, 5],
#               [3, 4, 6],
#               [1, 4, 2],
#               [2, 5, 1]
#               ])
#
# res = np.corrcoef(a, rowvar=False)
#
# t1 = np.array([1, 3, 1, 2])
# t2 = np.array([2, 4, 4, 5])
# res2 = np.corrcoef(t1, t2)
# #print(res2)
# #print(res, res.shape, type(res))
# from scipy import stats
# zz = np.array([[1, 2, 3],
#               [20, 2, 4],
#               [90, 5, 1],
#               ])
# print('--zz--\n', zz)
# r_res = np.corrcoef(zz)
# print('--r_res--\n', r_res)
# z_res = FisherZ(zz)
# print('--z_res--', z_res)
#


'''
[[-1.22474487  0.          1.22474487]
 [-0.70710678 -0.70710678  1.41421356]
 [ 0.          1.22474487 -1.22474487]]
'''

'''
[[-1.22474487  0.          1.22474487]
 [ 1.40693001 -0.82760589 -0.57932412]
 [ 0.          1.22474487 -1.22474487]]
 
 [[-1.22474487  0.          1.22474487]
 [ 1.40693001 -0.82760589 -0.57932412]
 [ 1.41309384 -0.65781954 -0.75527429]]
'''
import glob
import ToolBox as tb
import os
#data_files_all = sorted(glob.glob("/Users/fan/Documents/Data/test_data/test_fc/*.txt"))
#data_files_all = np.loadtxt('/Users/fan/Documents/Data/test_data/test_fc/')
fcpath = '/home/cuizaixu_lab/fanqingchen/DATA/data/ABCD_HCP2016_FC/'

files = os.listdir(fcpath)
feature = []
for file in files:
    txtfile = fcpath + file
    box = np.loadtxt(txtfile)
    box = tb.upper_tri_indexing(box)
    feature.append(box)

resfeature = np.array(feature)
print('--resfeature--', resfeature.shape)
np.savetxt('./HCPfeature.txt',resfeature)


mid = np.loadtxt('./HCPfeature.txt')
print('--mid--', mid.shape)

exit()
#All data
files_data = []
for i in data_files_all:
    img_data_reshape = tb.upper_tri_indexing(i)
    files_data.append(img_data_reshape)
x_data = np.asarray(files_data)
np.savetxt('./featurn_HCP.txt', x_data)