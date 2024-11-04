import numpy as np
import pandas as pd
path = '/Users/fan/Desktop/HCPfeature_new.txt'

label = pd.read_csv('./HCPLable.csv')
reslabel = label['General'].values.astype(float)
print(reslabel)



