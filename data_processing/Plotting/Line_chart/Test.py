import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import datetime

# 此设置为使图形能显示带特殊格式的字符
plt.rcParams['axes.unicode_minus'] = False

# 构建虚拟数据
"""
x轴为日期
左y轴为y1，y2
右y轴为 y1-y2 及其均值
"""
date = [(datetime.datetime.strptime("2019-12-08 00:00:00","%Y-%m-%d %H:%M:%S") + datetime.timedelta(days=i)).strftime("%Y-%m-%d%H:%M:%S")[:10] for i in range(300)]
x = np.arange(300)
x_ticks = [int(i) for i in np.linspace(0, (x.shape[0] - 1), 5)]
y1 = np.random.randn(300) *2 + 75
y2 = np.random.randn(300) *2 + 70

# 设置字体
font = FontProperties(fname="C:\Windows\Fonts\simsun.ttc", size=30)

figure = plt.figure(figsize=[30, 16], dpi=72)

ax1 = figure.add_subplot(111)

fig1 = ax1.plot(x, y1, color="c", label="y1")
fig2 = ax1.plot(x, y2, color="b", label="y2")
plt.yticks(fontproperties=font)
plt.xlabel("date", fontproperties=FontProperties(fname="C:\Windows\Fonts\simsun.ttc", size=45))
plt.xticks(x_ticks, date, fontproperties=FontProperties(fname="C:\Windows\Fonts\simsun.ttc", size=30), rotation=15)
ax1.set_ylim(40, 83)
ax1.set_ylabel("y", fontproperties=FontProperties(fname="C:\Windows\Fonts\simsun.ttc", size=45))

ax2 = ax1.twinx()

fig3 = ax2.plot(x, y1-y2, color="m", label="y1-y2")
fig4 = ax2.plot(x, [(y1-y2).mean()] * (x.shape[0]), color="g", linestyle="--", linewidth=5, label="mean of y1-y2")
ax2.set_ylim(-5, 40)
ax2.set_ylabel("y1-y2", fontproperties=FontProperties(fname="C:\Windows\Fonts\simsun.ttc", size=45))
plt.yticks(fontproperties=font)

# 显示均值
ax2.text(x.shape[0], (y1-y2).mean() - 0.1, str((y1-y2).mean())[:4], fontdict={"size": 30, "color": "g"})

# 设置图列
legends = fig1 + fig2 + fig3 + fig4
labels = [l.get_label() for l in legends]
plt.legend(legends, labels, prop=font, loc=(0.8, 0.4))

plt.show()
