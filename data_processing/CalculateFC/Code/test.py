import nibabel as nib
from scipy.io import savemat

a = nib.load('./sub-06202_task-rest_space-fsLR_atlas-Schaefer417_den-91k_measure-pearsoncorrelation_conmat.pconn.nii').get_fdata()

savemat('sub06202pconn.mat', {'data': a})