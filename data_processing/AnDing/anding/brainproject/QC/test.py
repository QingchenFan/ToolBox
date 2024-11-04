import subprocess
import csv

# 定义 NIfTI 文件路径
nifti_file_path = '/mnt/data/sub-01000002V01_task-facematching_run-1_acp-ap_bold.nii'

# 使用 mri_info 获取文件信息
try:
    result = subprocess.run(['mri_info', nifti_file_path], stdout=subprocess.PIPE, text=True)
    output = result.stdout
except FileNotFoundError:
    print("mri_info command not found. Please ensure FreeSurfer is installed and added to your PATH.")
    exit()

# 将信息按行分割
lines = output.splitlines()

# 打开CSV文件进行写入
csv_filename = 'mri_info_output.csv'
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Key', 'Value'])

    for line in lines:
        # 查找冒号并分割key-value对
        if ':' in line:
            key, value = line.split(':', 1)
            writer.writerow([key.strip(), value.strip()])

print(f"Information from mri_info has been saved to {csv_filename}.")
