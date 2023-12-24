import pandas as pd

# data_1 = pd.read_csv('./factor_score_wx.csv')
#
# data_2 = pd.read_csv('./ABCD_CBCL_FQC.csv')

with open('/Users/fan/Documents/Datafc/ABCD_HCP/file_name_hcp.csv', mode='r') as data_1:  # 多
    data_1 = data_1.readlines()

with open('/Users/fan/Documents/Datafc/ABCD_HCP/ABCD_HCP_Label.csv', mode='r')as data_2:  # 少
    data_2 = data_2.readlines()




list_all = []
for j in data_1:
    list_all.append(j[4:19])
#print(list_all,len(list_all))

list_less = []
for i in data_2:
    list_less.append(i[0:15])
#print(list_less,len(list_less))



for m in list_all:
    if m not in list_less:
        print(m)

# list_f = []
# for p in data_1:
#     list_f.append(p)
# fw = open("./ABCD_HCP_Label.csv", mode='w')
# for i in list_index:
#     #fw.write('\n')
#
#     fw.write(list_f[i])







