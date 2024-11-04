with open('./age_sex_fd.csv', mode='r')as cov:
    ageSexFd = cov.readlines()
cov_list = []
for cov in ageSexFd:
    m = cov.strip('\n')
    covm = m[0:14]
    cov_list.append(covm)
with open('./HCPLable.csv', mode='r')as ab:
    abcd = ab.readlines()
abcd_list = []
for i in abcd:
    box = i.strip('\n')
    res = box[0:14]
    abcd_list.append(res)
index_list = []
for fi in abcd_list:
    if fi  in cov_list:
        index_list.append(cov_list.index(fi))
fw = open('./ageSexFd_hcp.csv', mode='w')
res_list = []
for ind in index_list:
    res_list.append(ageSexFd[ind])
print(len(res_list))
i = 0
for wri in res_list:
    i = i + 1
    ress = str(i)+'---'+wri
    print(ress)
    fw.write(wri)

fw.close()
