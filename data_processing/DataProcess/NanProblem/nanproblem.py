import numpy as np
import os
#data_files_all = sorted(glob.glob("/Users/fan/Documents/Datafc/test_data/test_fc/*.txt"))
#data_files_all = np.loadtxt('/Users/fan/Documents/Datafc/test_data/test_fc/')
fcpath = '/Users/fan/Documents/Datafc/test_data/test_matrix/'

files = os.listdir(fcpath)
for file in files:
    txtfile = fcpath + file

    box = np.loadtxt(txtfile)
    print(box.shape)
    if np.isnan(box).any():
        print(file)

