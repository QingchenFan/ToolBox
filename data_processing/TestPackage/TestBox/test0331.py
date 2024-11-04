# from nilearn import datasets, surface
# fsaverage = datasets.fetch_surf_fsaverage("fsaverage6")
#
# img = datasets.load_mni152_template(2)
# a = img.get_fdata()
# print(a.shape)
# pial = '/Users/qingchen/Documents/Notes/datalearn/lianxi/bids/derivatives/fmriprep/sub-001/freesurfer/fsaverage/surf/lh.pial'
# white_left = '/Users/qingchen/Documents/Notes/datalearn/lianxi/bids/derivatives/fmriprep/sub-001/freesurfer/fsaverage/surf/lh.white'
#
# surf_data = surface.vol_to_surf(
#     img,
#     # surf_mesh=fsaverage["pial_left"],
#     # inner_mesh=fsaverage["white_left"],
#     surf_mesh=pial,
#     inner_mesh=white_left
# )
# print(surf_data.shape)

import nibabel as nib
path = '/Users/qingchen/Desktop/fs_LR_32k_file.gii'

a = nib.load(path).darrays[0].data
print(a.shape)