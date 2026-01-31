import pandas as pd
from collections import Counter

# 1. 读入数据
df = pd.read_csv('/Users/qingchen/Desktop/ADII_PD_Anat.csv')

# 2. 需要检查的指标
metrics = ['efc', 'fber', 'cjv', 'cnr', 'snr', 'snrd']

# 3. 用 IQR 法找异常，并记录每个 subID 的异常次数
outlier_counter = Counter()
outlier_dict = {}
for col in metrics:
    # 去掉缺失值（-1 视为缺失）
    s = df[col].replace(-1, pd.NA).dropna()
    Q1, Q3 = s.quantile([0.25, 0.75])
    IQR = Q3 - Q1
    low, high = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR

    # 找出异常 subID 并计数
    mask = (df[col] < low) | (df[col] > high)
    outlier_dict[col] = df.loc[mask, 'subID'].tolist()
    for sub in df.loc[mask, 'subID']:
        outlier_counter[sub] += 1
# 4. 打印结果
for k, v in outlier_dict.items():
    print(f"{k}: {v}")
# 4. 筛选异常次数 >= 3 的 subID
serious_outliers = [sub for sub, cnt in outlier_counter.items() if cnt >= 3]

# 5. 打印结果
print('异常指标出现 ≥3 次的 subID：')
for sub in serious_outliers:
    print(sub)
# 5. 筛选异常次数 >= 3 的 subID，并保存
serious_outliers = [sub for sub, cnt in outlier_counter.items() if cnt >= 3]
serious_df = pd.DataFrame({'subID': serious_outliers})
serious_df.to_csv('/Users/qingchen/Desktop/ADII_PD_Anat_outliers.csv', index=False)