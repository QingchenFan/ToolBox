import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#iris = sns.load_dataset('name',data_home='/Users/fan/PycharmProjects/data_processing/MakeGraph/Scatter_graph/Predict_Score_Int.csv',cache=True)
iris = pd.read_csv('correlationgraph.csv')
#print(iris)
'''
# seaborn模块绘制分组散点图
sns.lmplot(x = 'pre', # 指定x轴变量
           y = 'y', # 指定y轴变量
           hue = 'Species', # 指定分组变量
           data = iris, # 指定绘图数据集
           legend_out = False, # 将图例呈现在图框内
           truncate=True # 根据实际的数据范围，对拟合线作截断操作
          )
          '''
cx = sns.lmplot(x='ROI10', y='Alpha', data=iris,
                markers=".",
                line_kws={'color': '#130c0e', 'lw': 1.30},
                scatter_kws={'color': '#a1a3a6'}
                )  # line_kws={'color': 'black'}, scatter_kws={'color': 'blue'}

# 修改x轴和y轴标签
plt.xlabel('Right Anterior Insula', fontdict={'size': 16, 'font': 'Arial'})
plt.ylabel('Learning Rate', fontdict={'size': 16, 'font': 'Arial'})

plt.tick_params(size=2, width=1.25)  # 轴上的小刻度长度
plt.yticks(ticks=[0.01, 0.02, 0.03], fontproperties='Arial', size=14)
plt.xticks(ticks=[-5.0,  0, 5.0], fontproperties='Arial', size=14)
#plt.text(2, -0.70, "r = 0.18\nMAE = 0.70", size=10, bbox=dict(alpha=0.2))
# 添加标题
#plt.title('General', x=0.5, y=0.95, loc='center', color='#fab27b')
plt.savefig('Insula.png', dpi=300)
# 修改x轴 y轴 轴的粗细
ax=plt.gca()
ax.spines['bottom'].set_linewidth(1.25);###设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(1.25)
plt.subplots_adjust()
# 显示图形
plt.show()