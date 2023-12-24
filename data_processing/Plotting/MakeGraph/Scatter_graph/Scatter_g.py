import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#iris = sns.load_dataset('name',data_home='/Users/fan/PycharmProjects/data_processing/MakeGraph/Scatter_graph/Predict_Score_Int.csv',cache=True)
iris = pd.read_csv('Predict_Score_bagging_General_9_2.csv')
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
cx = sns.lmplot(x='true', y='prediction', data=iris, line_kws={'color': '#fab27b'}, scatter_kws={'color': '#fab27b'})  # line_kws={'color': 'black'}, scatter_kws={'color': 'blue'}

# 修改x轴和y轴标签
plt.xlabel('Actual Score', fontdict={'size': 16, 'font': 'Apri'})
plt.ylabel('Predicted Score', fontdict={'size': 16, 'font': 'Apri'})
plt.tick_params(size=0)
plt.yticks(fontproperties='Apri', size=12)
plt.xticks(fontproperties='Apri', size=12)
#plt.text(2, -0.70, "r = 0.18\nMAE = 0.70", size=10, bbox=dict(alpha=0.2))
# 添加标题
plt.title('General', x=0.5, y=0.95, loc='center', color='#fab27b')
plt.savefig('General.png', dpi=300)

# 显示图形
plt.show()