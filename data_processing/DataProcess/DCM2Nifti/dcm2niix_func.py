
from nipype.interfaces.dcm2nii import Dcm2niix
import os

def dcm2niix(input_path, out_path, name):
    converter = Dcm2niix()
    converter.inputs.source_dir = input_path
    converter.inputs.compression = 5
    converter.inputs.out_filename = name
    converter.inputs.output_dir = out_path
    converter.cmdline
    converter.run()

# intpath = '/Users/fan/Documents/ZhouLab/data/Twin_fmri_2013/1_Rest/'
# outpath = '/Users/fan/Documents/ZhouLab/data/Twin_fmri_2013/1_Rest_nii/'
intpath = '/Users/fan/Documents/ZhouLab/data/ChenJieRawData/'
outpath = '/Users/fan/Documents/ZhouLab/data/c_nii/'
foldername = os.listdir(intpath)

for i in foldername:

    print('-i-', i)
    input_path = intpath + i

    if not os.path.exists(input_path):
        print('no exit path--', input_path)
        continue
    out_path = outpath + 'sub-'+ i[18:22]


    if not os.path.exists(out_path):
        os.makedirs(out_path)
    name = 'sub-'+i+'_task-rest_bold'   # if  dicm to nii for resbold , remove single-line comments
#    name = 'sub-'+i+'_T1w'
    dcm2niix(input_path, out_path, name)
    print('---------------------------done--------------------------------')
    exit()
