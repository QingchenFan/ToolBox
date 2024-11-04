from neuroCombat import neuroCombat
import pandas as pd
import numpy as np

# Getting example data
alldata = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/FCSFeature/allsubFCSfeature.csv')
#alldata = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/allSubGradientfeature.csv')
data = alldata.iloc[:,5:]
data = np.array(data).T



covars = alldata[['sitenum','sex']]

covars.columns=['batch','gender']

# To specify names of the variables that are categorical:
categorical_cols = ['gender']

# To specify the name of the variable that encodes for the scanner/batch covariate:
batch_col = 'batch'

#Harmonization step:
data_combat = neuroCombat(dat=data,
    covars=covars,  
    batch_col=batch_col,
    categorical_cols=categorical_cols)["data"]

data_combat = data_combat.T
print(data_combat)
np.savetxt('./allSubFSC_combat_out.csv', data_combat, delimiter=',')
