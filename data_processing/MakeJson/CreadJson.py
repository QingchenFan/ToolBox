import os
import json
import nibabel as nib

# 1. 指定 NIfTI 文件路径
nii_path = '/Users/qingchen/Desktop/sub-01_ses-localizer1_acq-prescannormalized_rec-pydeface_T1w.nii.gz'


def generate_json(nii_path):

    sidecar = {
        "Modality": "MR",
        "Manufacturer": "Siemens",

    }

    # 5. 清除空值
    sidecar = {k: v for k, v in sidecar.items() if v is not None}

    # 6. 写出 JSON，格式化缩进为 4 空格
    json_path = os.path.splitext(nii_path)[0] + '.json'
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(sidecar, f, indent=4)  # 使用 indent 参数美化输出 :contentReference[oaicite:12]{index=12}

    print(f"已生成 JSON sidecar：{json_path}")
generate_json(nii_path)