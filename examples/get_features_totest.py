import pickle
from classicalgsg.molreps_models.utils import scop_to_boolean
from classicalgsg.molreps_models.gsg import GSG
import numpy as np
import shutil 
import sys
import os

from sklearn import decomposition
from sklearn import datasets


#STUFF TO CHANGE
NUM_COMPS = int(sys.argv[1])

with open('huuskonen.pkl', 'rb') as f:
    data = pickle.load(f)

with open('full_huuskonen_matrix.pkl', 'rb') as f:
    X = pickle.load(f)


newX = np.asarray(X)


#PCA STUFF
pca = decomposition.PCA(n_components=NUM_COMPS)
pca.fit(newX)
pcaX = pca.transform(newX)
print("PCA row length: " + str(len(pcaX[0])))
print("PCA col length: "+ str(len(pcaX)))


print("length of feat molecuels: " + str(len(pcaX)))
print("length of logp molecuels: " + str(len(data['logp'])))
print("length of logp molecuels: " + str(len(data['molid'])))

openchem_dict = {"molid":[], "features":[], "logp":[]}


for i in range(len(pcaX)):
	openchem_dict['features'].append(pcaX[i])

for i in range(len(pcaX)):   
    openchem_dict['logp'].append(data['logp'][i])

for i in range(len(pcaX)):   
    openchem_dict['molid'].append(data['molid'][i])




#print(str(openchem_dict['logp']))
print(str(len(openchem_dict['features'])))
print(str(len(openchem_dict['features'][0])))
print(str(len(openchem_dict['logp'])))
print(list(openchem_dict.keys()))


#put data into train_runs
for i in range(5):
    #Deletee old OpenCHem test set
    os.remove("/mnt/home/f0102398/ClassicalGSG/examples/cgenffe" + str(NUM_COMPS) + "/train_run" + str(i + 1) + "/data_4_zfs/OpenChem/OpenChem_test.pkl") 
    
    file_path = "/mnt/home/f0102398/ClassicalGSG/examples/cgenffe" + str(NUM_COMPS) + "/train_run" + str(i + 1) + "/data_4_zfs/OpenChem/OpenChem_test.pkl"
    open_file = open(file_path, "wb")
    pickle.dump(openchem_dict, open_file)
    open_file.close()
    


print("done")
