import numpy as np

a = np.zeros((1,10))

ind = np.array([0,2,5,6,8])

v = np.array([0.1,0.6,0.7,1,0.9])

a[:,ind] = v

print(a)