import pandas as pd

# data_1 = pd.read_csv('./factor_score_wx.csv')
#
# data_2 = pd.read_csv('./ABCD_CBCL_FQC.csv')

with open('/Users/fan/Documents/Datafc/ABCD_HCP/factor_score_wx.csv', mode='r') as data_1:
    data_1 = data_1.readlines()

with open('/Users/fan/Documents/Datafc/ABCD_HCP/file_name_hcp.csv', mode='r')as data_2:
    data_2 = data_2.readlines()

list_f = []
for p in data_1:
    list_f.append(p)

list_all = []
for j in data_1:
    list_all.append(j[0:15])

list_hcp = []
for i in data_2:
    list_hcp.append(i[4:19])


list_index = []
for m in list_hcp:
    if m in list_all:
        list_index.append(list_all.index(m))

fw = open("./ABCD_HCP_Label.csv", mode='w')
for i in list_index:
    #fw.write('\n')

    fw.write(list_f[i])







