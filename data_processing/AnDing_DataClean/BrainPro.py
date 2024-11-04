import glob
import pandas as pd


def process_data(data_dir,ln):
    # 创建一个空的DataFrame
    df = pd.DataFrame(columns=ln)
    file = glob.glob(data_dir)

    for i in file:
        data = glob.glob(i + '/*.nii')
        # 遍历data_dir目录下的所有文件
        print(i)
        subID = i.split('/')[-1]
        print('subID - ',subID)

        # 初始化各个数据类型的标志
        has_dti = False
        has_BOLD_Resting = False
        has_BOLD_Longresting = False
        has_FM_task = False
        has_UG_task = False
        has_t1_mprage = False

        # 遍历当前目录下的所有文件
        for f in data:
            # 检查文件名是否包含相应的数据类型
            if 'dti' in f:
                has_dti = True
            elif 'bold_resting' in f:
                has_BOLD_Resting = True
            elif 'bold_longresting' in f:
                has_BOLD_Longresting = True
            elif 'face_matching' in f:
                has_FM_task = True
            elif 'bold_ultimate' in f:
                has_UG_task = True
            elif 't1' in f:
                has_t1_mprage = True

        # 将结果记录到DataFrame中
        df = df._append({'subID': subID, 'DTI': has_dti, 'BOLD_Resting': has_BOLD_Resting, 'T1': has_t1_mprage,
                                'BOLD_Longresting':has_BOLD_Longresting, 'FM_task': has_FM_task, 'UG_task': has_UG_task,}, ignore_index=True)

    return df
data_dir = '/home/zhouyuan/fan/Data/brainproject/V01/BD/*'

ln = ['subID', 'DTI', 'T1', 'BOLD_Resting', 'BOLD_Longresting', 'FM_task', 'UG_task' ]
df = process_data(data_dir,ln)
df.to_csv('/home/zhouyuan/fan/Data/brainproject/V01/brain_BD_v01.csv', index=False)