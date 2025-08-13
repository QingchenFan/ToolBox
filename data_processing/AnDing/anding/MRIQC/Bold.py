import glob
import json
import pandas as pd


path = '/Volumes/QCI/MRIQC/AD/PD_V1/sub-*/func/*_task-rest_acq-ap_run-1_bold.json'
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
        'aor': data['aor'],
        'aqi': data['aqi'],
        'dvars_std': data['dvars_std'],
        'dvars_vstd': data['dvars_vstd'],
        'snr': data['snr'],
        'tsnr': data['tsnr']
    })

# 4. 生成 DataFrame
df = pd.DataFrame(records)

# 5. 保存到 csv（也可打印或返回）
df.to_csv('./ADI_PD_Bold.csv', index=False)

