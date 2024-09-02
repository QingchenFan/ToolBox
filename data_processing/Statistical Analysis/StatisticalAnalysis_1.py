import math

import pandas as pd
import statsmodels.formula.api as smf

# 读取数据
data = pd.read_csv('data.csv')

# 对数转换体积变量
data['log_volume'] = data['a_volume'].apply(lambda x: math.log(x))

# 将孕龄变量以31周为中心
data['centered_ga'] = data['ga'] - 31

# 嵌套混合效应回归模型（具有左右两侧表示的结构）
mixed_model_lr = smf.mixedlm("log_volume ~ centered_ga * sex + side", data)
mixed_results_lr = mixed_model_lr.fit()
print(mixed_results_lr.summary())

# 混合效应回归模型（中线结构）
mixed_model_mr = smf.mixedlm("log_volume ~ centered_ga * sex", data)
mixed_results_mr = mixed_model_mr.fit()
print(mixed_results_mr.summary())