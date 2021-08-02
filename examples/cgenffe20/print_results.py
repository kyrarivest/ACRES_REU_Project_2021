import json
import sys

file = open("results.json", "r")
scores = json.load(file)
file.close()

print(str(scores))


avgs = []

pcc = 0
for i in range(len(scores['PCC']) - 5,len(scores['PCC'])):
    pcc += scores['PCC'][i]

avgs.append((pcc/4))

rmse = 0
for i in range(len(scores['PCC']) - 5,len(scores['PCC'])):
    rmse += scores['RMSE'][i]

avgs.append((rmse/4))



#Code ot save results to total list
num_comps = str(sys.path[0])[len("/mnt/ufs18/home-088/f0102398/ClassicalGSG/examples/"):]

file = open("/mnt/home/f0102398/ClassicalGSG/examples/results.txt", "a")
file.write("\n")
file.write(num_comps + "\n")
file.write(str(avgs))
file.close()

