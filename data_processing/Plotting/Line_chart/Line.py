import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
fmri = sns.load_dataset("fmri")
print(fmri)
# sns.relplot(
#     data=fmri, kind="line",
#     x="timepoint", y="signal",
#     hue="event", style="event",
# )
# plt.show()
# exit()

fmri = pd.read_csv('/Users/qingchen/Documents/code/Data/mean_r.csv')
print(fmri)
# sns.relplot(
#     data=fmri, kind="line",
#     x="edge", y="z",
#     hue="group", style="group",errorbar="sd"
# )

sns.lineplot(
    data=fmri,
    x="edge", y="z",
    hue="group", style="group",  errorbar=("ci", 95)  # 使用标准差作为置信区间的度量
)
plt.show()
plt.show()