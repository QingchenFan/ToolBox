import numpy as np
import scipy.stats

# 定义时间窗口大小和重叠
window_size = 2  # in seconds
overlap = 4  # in seconds

# 加载数据
#data = np.load('fMRI_data.npy')  # data shape: (time_points, regions)
data = np.random.randint(1, 10, (16, 5))
# 计算每个时间窗口的功能连接网络
print(data)
fcms = []
for i in range(0, len(data) - window_size, overlap):
    window_data = data[i:i+window_size, :]
    print('-window_data-\n', window_data)
    print('-window_data.T-\n', window_data.T)

    fcm = np.corrcoef(window_data.T)
    print('fcm\n', fcm)
    fcms.append(fcm)
print('-fcms-\n', fcms)
# 合并所有时间窗口的功能连接网络
dfcn = np.mean(fcms, axis=0)
print('dfcn', dfcn)
# 进一步分析dfcn，例如使用社区检测算法寻找子网络
