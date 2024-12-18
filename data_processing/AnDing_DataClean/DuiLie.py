import glob
import pandas as pd


def process_data(data_dir,ln):
    # 创建一个空的DataFrame
    df = pd.DataFrame(columns=ln)
    file = glob.glob(data_dir)

    for i in file:
        data = glob.glob(i + '/*.nii.gz')
        # 遍历data_dir目录下的所有文件
        print(i)
        subID = i.split('/')[-1]
        print('subID - ',subID)

        # 初始化各个数据类型的标志
        has_dti = False
        has_functional_ap = False
        has_FM_task = False
        has_UG_task = False
        has_t1_mprage = False

        # 遍历当前目录下的所有文件
        for f in data:
            # 检查文件名是否包含相应的数据类型
            if 'DTI' in f:
                has_dti = True
            elif 'Functional_AP' in f:
                has_functional_ap = True
            elif 'FM_task' in f:
                has_FM_task = True
            elif 'UG_task' in f:
                has_UG_task = True
            elif 't1_mprage' in f:
                has_t1_mprage = True

        # 将结果记录到DataFrame中
        df = df._append({'subID': subID, 'DTI': has_dti,  'Functional_AP': has_functional_ap,'t1_mprage': has_t1_mprage,
                                'FM_task': has_FM_task, 'UG_task': has_UG_task,}, ignore_index=True)

    return df
data_dir = '/Volumes/QCII/duilie/duilie_2024512/nifti/V01/*'

ln = ['subID', 'DTI',  'Functional_AP', 't1_mprage','FM_task','UG_task' ]
df = process_data(data_dir,ln)
df.to_csv('./duilie_v01.csv', index=False)