import numpy as np

import numpy as np

matrix2 = np.ones((5, 3))
#matrix2 = np.random.randint(low=1, high=5, size=(5, 5))
print(matrix2)
a = matrix2[:,1]
print(a)
res = (a == 1).all()
if (a == 0).all():
    print('12345')
print(res)


exit()


matrix = np.random.randint(low=1, high=5, size=(5, 5))
print(matrix)
print(matrix.shape)
print(matrix[:,3])
exit()

# 创建两个矩阵
matrix1 = np.ones((3, 3))
matrix2 = np.zeros((3, 3))
print(matrix1)
print(matrix2)
# 在行方向上拼接矩阵
result = np.concatenate((matrix1, matrix2), axis=1)

# 打印结果
print(result)
exit()
# 创建示例数组
arr = np.array([[[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]],

                [[10, 11, 12],
                 [13, 14, 15],
                 [16, 17, 18]],

                [[19, 20, 21],
                 [22, 23, 24],
                 [25, 26, 27]]
                ])
# 删除指定的行和列
matrix = np.random.randint(low=1, high=2, size=(5, 5, 5))

# 打印结果
print(matrix)
re1 = matrix[2:4,3:5,1:3]
print(re1)

# re = matrix[slice(2,4),slice(3,5),slice(1,3)] = 0
# print(re)

matrix[2:4,3:5,1:3] = 0
print(matrix)
exit()
arr_without_rows_cols = np.delete(arr,slice(2, 4), axis=0)
arr_without_rows_cols = np.delete(arr_without_rows_cols, slice(0,1), axis=1)

# 打印结果
print(arr_without_rows_cols)