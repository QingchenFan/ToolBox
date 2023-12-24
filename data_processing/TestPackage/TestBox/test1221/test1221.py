from nilearn import image

BOLDdata = image.load_img('./sub-MDD001_task-rest_space-MNI152NLin6Asym_res-2_desc-denoisedSmoothed_bold.nii.gz')
c = BOLDdata.get_fdata()
print(c.shape)
a = image.index_img(BOLDdata, 1).get_fdata()

print(a)
print(a.shape)

