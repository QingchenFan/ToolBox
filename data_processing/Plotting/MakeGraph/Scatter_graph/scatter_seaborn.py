import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv('Predict_Score_bagging_General_9_2.csv')

sns.scatterplot(x='true', y='prediction', data=iris,)
# 显示图形
plt.show()