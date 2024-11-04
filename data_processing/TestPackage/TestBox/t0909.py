import matplotlib.pyplot as plt

# 假设的字典数据
info = {'num': [10, 5, 4, 3, 2, 1], 'sum': [10, 20, 30, 40, 50, 60]}

# 提取num和sum的值
x = info['num']
y = info['sum']

# 绘制柱状图
plt.bar(x, y, color='skyblue')
# 只保留左侧和下侧的轴线
plt.gca().spines['top'].set_visible(False)  # 去掉上侧轴线
plt.gca().spines['right'].set_visible(False)  # 去掉右侧轴线
plt.gca().spines['bottom'].set_color('black')  # 设置下侧轴线为黑色
plt.gca().spines['left'].set_color('black')  # 设置左侧轴线为黑色
# 添加标题和轴标签
plt.title('Sum by Number')
plt.xlabel('Number')
plt.ylabel('Sum')

# 显示图表
plt.show()