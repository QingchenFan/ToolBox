import numpy as np

# num = np.random.random((5,5))
# zeros = np.zeros((5, 5))
# print(num)
# zeros[1,:] = num[2,:]
# print(zeros)


num2 = np.random.randint(5, size=(5,5))
print(num2)
res = np.sum(num2,axis=1)
print(res)
pres = []
for i in range(0,5):
    tep = num2[i]
    length=len(tep[tep!=0])
    print('--le',length)
    pres.append(res[i] / length)
print(pres)