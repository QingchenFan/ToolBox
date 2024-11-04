import os
import glob
from shutil import copy
path = '/Volumes/QCCC/HCP_xcpd_out2/sub*'

filename = glob.glob(path)

subfile = [i for i in filename if os.path.isdir(i)]

for j in subfile:
    subid = j[-10:]
    print(subid)
    fcpath = j +'/func/'+subid +'*Schaefer417_*.pconn.nii'
    fcfile = glob.glob(fcpath)
    print(fcfile)
    targrtpath = '/Volumes/QCCC/HCP_Schaeder400FC/'+ subid
    if not os.path.exists(targrtpath) :
        os.makedirs(targrtpath)
    for f in fcfile :
        copy(f,targrtpath)