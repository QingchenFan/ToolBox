import numpy as np
import pandas as pd
file_2 ='/Volumes/QC/Data/To_LMH/Queue_MDD_NAD.csv'
file_1 ='/Volumes/QC/Data/To_LMH/Queue_MDD_reho_4S456Parcels.csv'
#Read the CSV files into DataFrames
df1 = pd.read_csv(file_1, na_filter=False)
df2 = pd.read_csv(file_2, na_filter=False)

df_new = pd.merge(df2, df1, on='subID', how='outer')
df_new.to_csv('/Volumes/QC/Data/To_LMH/Queue_MDD_NAD_reho_4S456Parcels_Final.csv', index=False, encoding='utf-8-sig')