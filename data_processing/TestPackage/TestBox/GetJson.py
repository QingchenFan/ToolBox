import sys
import json
import SimpleITK as sitk
path = '/Users/fan/Documents/Datafc/HCPData/HCPDtest/sub-HCD0001305_task-rest_space-MNI152NLin6Asym_desc-residual_smooth_bold.nii.gz'
reader = sitk.ImageFileReader()
print(reader)
exit()
reader.SetFileName(sys.argv[1])
reader.LoadPrivateTagsOn()

reader.ReadImageInformation()

data_dictionary = {}

for k in reader.GetMetaDataKeys():
    v = reader.GetMetaData(k)
    data_dictionary[k] = v

print(json.dumps(data_dictionary))