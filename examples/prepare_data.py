import pickle
from classicalgsg.molreps_models.utils import scop_to_boolean
from classicalgsg.molreps_models.gsg import GSG
from sklearn import decomposition
from sklearn import datasets
import numpy as np
import shutil 
import sys
import os



NUM_COMPS = int(sys.argv[1])
DATASET = str(sys.argv[2])
MODE = str(sys.argv[3])


dataset_path = "/datasets/" + DATASET + "/" + DATASET + ".pkl"


with open(dataset_path, 'rb') as f:
    data = pickle.load(f)


#Generates GSG features from DATASET

wavelet_step_num = 4
scattering_operators = scop_to_boolean('(z,f,s)')
gsg = GSG(wavelet_step_num, scattering_operators)

feat_mat = []

for i in range(len(data['adjacency'])):
	features=(gsg.features(data['adjacency'][i], data['cgenff_signals'][i]))
	feat_row = []
	for j in features:
		feat_row.append(j[0])

	feat_mat.append(feat_row)


gsg_feature_matrix = np.asarray(feat_mat)


#Optinal: save the GSG feature matrix as a pkl file or csv file

#dataset_name = DATASET + "_GSG"
#open_file = open(dataset_name + ".pkl", "wb")
#pickle.dump(X, open_file)
#open_file.close()
#np.savetxt(dataset_name + ".csv", X, delimiter=" ")



#PCA Step
pca = decomposition.PCA(n_components=NUM_COMPS)
pca.fit(gsg_feature_matrix)
pca_features = pca.transform(gsg_feature_matrix)

print("PCA features row length: " + str(len(pca_features[0])))
print("PCA features column length: "+ str(len(pca_features)))



#Creates neural network model training input
openchem_dict = {"molid":[], "features":[], "logp":[]}


for i in range(len(pca_features)):
	openchem_dict['features'].append(pca_features[i])

for i in range(len(pca_features)):   
    openchem_dict['logp'].append(data['logp'][i])

for i in range(len(pca_features)):   
    openchem_dict['molid'].append(data['molid'][i])




#Puts data into the files
if MODE == "train":
    if not os.path.isdir(sys.path[0] + "cgenffe" + NUM_COMPS):
        src = sys.path[0] + "/cgenffgsg"
        dest = sys.path[0] + "/cgenffe" + str(NUM_COMPS)
        shutil.copytree(src, dest) 
    else:
        for i in range(5):
            os.remove(sys.path[0] + "/cgenffe" + str(NUM_COMPS) + "/train_run" + str(i + 1) + "/data_4_zfs/OpenChem/OpenChem.pkl") 
            os.remove(sys.path[0] + "/cgenffe" + str(NUM_COMPS) + "/train_run" + str(i + 1) + "/data_4_zfs/OpenChem/OpenChem_training.pkl") 
            os.remove(sys.path[0] + "/cgenffe" + str(NUM_COMPS) + "/train_run" + str(i + 1) + "/data_4_zfs/OpenChem/OpenChem_test.pkl") 


    for i in range(5):
        file_path = sys.path[0] + "/cgenffe" + str(NUM_COMPS) + "/train_run" + str(i + 1) + "/data_4_zfs/OpenChem/OpenChem.pkl"
        open_file = open(file_path, "wb")
        pickle.dump(openchem_dict, open_file)
        open_file.close()

else:
    for i in range(5):
        os.remove(sys.path[0] + "/cgenffe" + str(NUM_COMPS) + "/train_run" + str(i + 1) + "/data_4_zfs/OpenChem/OpenChem_test.pkl") 
        file_path = sys.path[0] + "/cgenffe" + str(NUM_COMPS) + "/train_run" + str(i + 1) + "/data_4_zfs/OpenChem/OpenChem_test.pkl"
        open_file = open(file_path, "wb")
        pickle.dump(openchem_dict, open_file)
        open_file.close()


print("Data Preparation complete")
