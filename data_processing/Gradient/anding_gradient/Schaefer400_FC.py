import glob
import numpy as np
import os
from scipy.io import savemat
import scipy.io as scio

name = ['hc_v2', 'hc001_50_v01', 'hc051_114_v01', 'MDDv1', 'MDDv2']
for filename in name:
     subfile = 'ROISignals_SurfLHSurfRHVolu_FunSurfWglobalCF'
     mark = 'global'

     # subfile = 'ROISignals_SurfLHSurfRHVolu_FunSurfWCF'
     # mark = ''

     path = '/Volumes/qingchen/anding/gradient/'+filename+'/'+subfile+'/*.mat'
     dataPath = glob.glob(path)
     for i in dataPath:
          print(i)
          Data = scio.loadmat(i)
          data = Data['Datafc']
          A = data[180:380, 180:380]
          B = data[180:380, 560:760]
          Schaefer400FC_AB = np.concatenate((A, B), axis=1)
          C = data[560:760, 180:380]
          D = data[560:760, 560:760]
          Schaefer400FC_CD = np.concatenate((C, D), axis=1)
          Schaefer400FC = np.concatenate((Schaefer400FC_AB, Schaefer400FC_CD), axis=0)
          if filename in ['MDDv1', 'MDDv2']:
               id = i[-14:-4]
          else:
               id = i[-13:-4]
          newpath = '/Volumes/qingchen/anding/gradient/'+filename+'/Schaefer400Fc'+mark+'/'
          if not os.path.exists(newpath):
               os.makedirs(newpath)
          savemat(newpath + '/'+id+'_Schaefer400Fc'+mark+'.mat', {'data': Schaefer400FC})


