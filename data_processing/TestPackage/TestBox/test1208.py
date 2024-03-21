import os
import subprocess

a = 'export FREESURFER_HOME=/Applications/freesurfer/7.4.1'
b = 'export SUBJECTS_DIR=$FREESURFER_HOME/subjects'
c = 'source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh'

os.system(a)

os.system(b)

os.system(c)
#subprocess.run(c,shell=True)

subprocess.run('freesurfer',shell=True)

#os.system('freesurfer')