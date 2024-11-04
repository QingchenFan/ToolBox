
import subprocess
import json
import csv
sy = '''
        export FREESURFER_HOME=/Applications/freesurfer/7.4.1
        export SUBJECTS_DIR=$FREESURFER_HOME/subjects
        source $FREESURFER_HOME/SetUpFreeSurfer.sh
        mri_info /Users/qingchen/Documents/Data/brianproject/facemapping1/FunRaw/sub-01000002V01/sub-01000002V01_task-facematching_run-1_acp-ap_bold.nii'''

def adb_shell(cmd):
    result = subprocess.getstatusoutput(cmd)
    return result

b = adb_shell(sy)[1]
print(b)

# 需要获取的key列表
keys_of_interest = ['type', 'dimensions', 'voxel sizes', 'fov', 'TR', 'nframes', 'PhEncDir', 'FieldStrength', 'Orientation']

# 初始化空列表来存储key-value对
data = []

# 将字符串按行分割并遍历
for line in b.splitlines():
    # 去除行首尾的空格
    line = line.strip()
    # 检查是否是key-value对
    if ':' in line:
        key, value = line.split(':', 1)
        key = key.strip()
        value = value.strip()
        # 如果key在感兴趣的列表中，则添加到数据中
        if key in keys_of_interest:
            data.append((key, value))

# 保存到CSV文件
csv_filename = './filtered_output.csv'

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Key', 'Value'])
    writer.writerows(data)

print(f"Filtered data has been saved to {csv_filename}.")

#   读取json文件

# JSON 文件路径
json_file_path = './sub-01000002V01_task-facematching_run-1_acp-ap_bold.json'
# 之前生成的 CSV 文件路径
csv_file_path = './filtered_output.csv'

# 需要提取的 key 列表
keys_of_interest = ['RepetitionTime', 'FlipAngle', 'SliceTiming', 'PhaseEncodingDirection']

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

