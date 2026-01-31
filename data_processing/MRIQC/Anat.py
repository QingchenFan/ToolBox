import glob
import json
import pandas as pd


path = '/Volumes/QCI/MRIQC/AD_II/sub-*/anat/sub-*_T1w.json'
json_files = glob.glob(path)

# 2. 准备结果容器
records = []

# 3. 逐个文件解析
for file in json_files:
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)


    # 从文件名提取 subID（去掉后缀和 _T1w 部分）
    sub_id = file.split('/')[-3]

    # 提取需要的字段
    records.append({
        'subID': sub_id,
        'efc': data['efc'],
        'fber': data['fber'],
        'cjv': data['cjv'],
        'cnr': data['cnr'],
        'snr': data['snr_total'],
        'snrd': data['snrd_total']
    })

# 4. 生成 DataFrame
df = pd.DataFrame(records)

# 5. 保存到 csv（也可打印或返回）
df.to_csv('./ADII_PD_Anat.csv', index=False)

