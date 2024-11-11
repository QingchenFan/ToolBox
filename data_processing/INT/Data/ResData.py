import scipy.io as sio
import numpy as np
path = '/Volumes/QCI/NormativeModel/Data135/HC/INT/Group/Group_0.mat'

a = sio.loadmat(path)


print(a['hwhm'].shape)
res = a['hwhm']

np.savetxt('group.csv', res, delimiter=',')
path2 = '/Volumes/QCI/NormativeModel/Data135/HC/INT/Ind/Ind_0.mat'

b = sio.loadmat(path2)

print(b['hwhms'].shape)