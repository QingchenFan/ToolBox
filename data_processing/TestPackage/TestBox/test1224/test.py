import matlab.engine
eng = matlab.engine.start_matlab()

a = eng.cifti_read('./sub-06202_task-rest_space-fsLR_den-91k_desc-denoisedSmoothed_bold.dtseries.nii')
print(a)