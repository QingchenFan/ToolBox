import json
import csv

# JSON 文件路径
json_file_path = './sub-01000002V01_task-facematching_run-1_acp-ap_bold.json'
# 之前生成的 CSV 文件路径
csv_file_path = 'filtered_output.csv'

# 需要提取的 key 列表
keys_of_interest = ['RepetitionTime', 'FlipAngle', 'ShimSetting', 'PhaseEncodingDirection']

# 读取 JSON 文件
with open(json_file_path, 'r') as f:
    json_data = json.load(f)

# 提取所需的 key-value 对
json_entries = [(key, json_data[key]) for key in keys_of_interest if key in json_data]

# 打开之前的 CSV 文件并追加 JSON 数据
with open(csv_file_path, mode='a', newline='') as file:
    writer = csv.writer(file)
    # 写入 JSON 数据中的 key-value 对
    for entry in json_entries:
        writer.writerow(entry)