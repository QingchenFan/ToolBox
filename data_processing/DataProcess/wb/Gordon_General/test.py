
import numpy as np
from scipy.stats import ttest_ind

# 定义组1和组2的数据
group1_data = np.array([1,2,3,4,5,5,6])
group2_data = np.array([6,7,9,8,5])

# 执行t检验
t_statistic, p_value = ttest_ind(group1_data, group2_data)

# 打印t值和p值
print("t值:")
print(t_statistic)
print("p值:")
print(p_value)