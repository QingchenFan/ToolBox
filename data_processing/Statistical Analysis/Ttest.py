import scipy.stats as stats
import pandas as pd

data = pd.read_csv('./data.csv')
female_age_data = data[data['sex'] == 1]['s_volume']
male_age_data = data[data['sex'] == 2]['s_volume']



# 执行双样本T检验
t_statistic, p_value = stats.ttest_ind(male_age_data, female_age_data)

# 计算置信区间（例如，使用95%置信水平）
confidence_level = 0.95
lower_ci, upper_ci = stats.t.interval(confidence_level, len(male_age_data) + len(female_age_data) - 2, loc=t_statistic, scale=stats.sem(male_age_data + female_age_data))

# 输出结果
print("T： ", t_statistic)
print("P值：", p_value)
print("置信区间：", (lower_ci, upper_ci))