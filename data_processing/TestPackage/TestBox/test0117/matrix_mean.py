import numpy as np

array = np.array([[1, 2, 3],
                  [1, 0, 2],
                  [4, 5, 6],
                  [1, 3, 1]])
a = np.array([0,1,3])

res = array[a,:]
print(res)
b = np.mean(res,axis=0)
print(b)
