import numpy as np

#import ToolBox as tb

import os
#data_files_all = sorted(glob.glob("/Users/fan/Documents/Datafc/test_data/test_fc/*.txt"))
#data_files_all = np.loadtxt('/Users/fan/Documents/Datafc/test_data/test_fc/')
fcpath = '/home/cuizaixu_lab/fanqingchen/DATA/data/ABCD_HCP2016_FC/HCPFC/'

files = os.listdir(fcpath)
print(files)
#files.sort()
feature = []
for file in files:
    txtfile = fcpath + file
    print('--txtfile--', txtfile)
    box = np.loadtxt(txtfile)
    box = tb.upper_tri_indexing(box)
    feature.append(box)

resfeature = np.array(feature)
np.savetxt('/home/cuizaixu_lab/fanqingchen/DATA/data/Feature_Matrix/HCPfeature_new.txt', resfeature)