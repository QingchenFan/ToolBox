import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


import seaborn as sns
import matplotlib.pyplot as plt



sns.set_theme(style="white", context="talk")


# Set up the matplotlib figure
f, ax1 = plt.subplots(1, 1, figsize=(8.5, 8), sharex=True)

# Generate some sequential data
df = pd.read_csv('./Gorden_General_res/General_avgweight.csv')
x_name = df['roi']

x = np.array(list(x_name))
x=np.arange(1, len(x_name)+1)
y_name = df['num']
y1 = np.array(list(y_name))
sns.barplot(x=x, y=y1, data=df, palette="Blues_r", hue='roi', dodge=False, ax=ax1, ci=None)
ax1.set_xticklabels(df['roi'], rotation=45, fontsize=14, font='Aprial')
ax1.axhline(0, color="k", clip_on=True)
ax1.set_xlabel("networks")
ax1.set_ylabel("Rank of Weights")
ax1.set_title("General", size=28)
# Finalize the plot
sns.despine(bottom=True)

#plt.xticks(rotation=45, fontsize=10)

plt.tight_layout(h_pad=2)

plt.legend(bbox_to_anchor=(2, 1), ncol=2, prop={'size': 10})
plt.savefig('General.png')
plt.show()
