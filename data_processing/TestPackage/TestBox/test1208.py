# import os
# import subprocess
#
# a = 'export FREESURFER_HOME=/Applications/freesurfer/7.4.1'
# b = 'export SUBJECTS_DIR=$FREESURFER_HOME/subjects'
# c = 'source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh'
#
# os.system(a)
#
# os.system(b)
#
# os.system(c)
# #subprocess.run(c,shell=True)
#
# subprocess.run('freesurfer',shell=True)
#
# #os.system('freesurfer')
import csv

data = [1, 1, -1, -1]
filename = 'tc.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(data)


import csv

# matrix = [
#     [1, 0, 0, 0],
#     [1, 0, 0, 0],
#     [0, 1, 0, 0],
#     [0, 1, 0, 0],
#     [0, 1, 0, 0],
#     [0, 0, 1, 0],
#     [0, 0, 1, 0],
#     [0, 0, 0, 1],
#     [0, 0, 0, 1],
#     [0, 0, 0, 1]
# ]
matrix = [
    [1,1,-1,-1],
    [1,-1,1,-1],
    [1,-1,-1,1],
    [1,1,1,1]
]
filename = 'fc.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(matrix)