import pandas as pd
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('./group_validation_index.csv', header=None)
#print(data)
data_x = pd.DataFrame(data.loc[0,1:])

data_tpd = pd.DataFrame(data.loc[1, 2:])

data_leftdice = pd.DataFrame(data.loc[2, 2:])
data_rightdice = pd.DataFrame(data.loc[3, 2:])
dataframe = [data_tpd, data_leftdice, data_rightdice, data_x]
data_res = pd.concat(dataframe)
data_res.columns = ['data_tpd', 'data_leftdice', 'data_rightdice', 'data_x']
fig, ax = plt.subplots()
sns.lineplot(data=data_res, x='data_x', y='data_leftdice', linewidth=2.0, color='indianred')
sns.lineplot(data=data_res, x='data_x', y='data_rightdice', linewidth=3.0, color='darkred')#powderblue
#修改x轴、y轴描述
plt.xlabel('Cluster number', fontdict={'color': 'black',
                             'fontstyle': 'normal',
                             'family': 'Times New Roman',
                             'weight': 'normal',
                             'size': 16})
plt.ylabel('Dice', fontdict={'color': 'black',
                          'fontstyle': 'normal',
                          'family': 'Times New Roman',
                          'weight': 'normal',
                          'size': 16})
plt.ylim(0.6, 0.95)
plt.xlim(0, 30)

plt.xticks(size=10)
plt.yticks(size=10)



ax2 = ax.twinx()
sns.lineplot(data=data_res, x='data_x', y='data_tpd', linewidth=3.0, ax=ax2, color='steelblue')
plt.ylabel('TpD', fontdict={'color': 'black',
                          'fontstyle': 'normal',
                          'family': 'Times New Roman',
                          'weight': 'normal',
                          'size': 16})

plt.yticks(size=10)
plt.savefig('line.png', dpi=300)
plt.show()
