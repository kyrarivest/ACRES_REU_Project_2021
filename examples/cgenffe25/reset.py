import os
import sys

for i in range(1,6):
    os.remove(str(sys.path[0]) + "/train_run" + str(i) + "/models/OpenChem/model_4_zfs.pkl") 

