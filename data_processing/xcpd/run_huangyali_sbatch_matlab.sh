#!/bin/bash
for id in {1..2000}
do
echo "subj=$id"
sbatch huangyali_sbatch_matlab.sh id

done
