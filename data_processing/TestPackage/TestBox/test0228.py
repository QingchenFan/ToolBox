
import numpy as np
import nibabel as nib
from nilearn import image
from nilearn.image import smooth_img
# a = np.random.randint(1, 10, (3, 2, 5))
# print(a)
# b = np.reshape(a, (1, 30))
# print(b)
#
# c = np.random.randint(1, 10, (4, 3, 2, 5))
# print(c)
# d = np.reshape(c, (4, 30))
# print(d)

def cal(a,b):
    dic = {'add':a+b,
            'sub':a-b

    }
    for i in range(1,10):
        print('--in--', i)
    return dic

def cal2(a,b):
    dic = {'add':a+b,
            'sub':a-b

    }
    for i in range(1,10):
        print('--in--2')
    return dic

# if __name__ == '__main__':
#     a = 5
#     b = 2
#     res = cal(a, b)
#     print(res)


a = 5
b = 2
res = cal(a, b)

print(res)
cal2(a,b)