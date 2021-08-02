import json
import sys

file = open("results.json", "r")
scores = json.load(file)
file.close()

print(str(scores))


#Code ot save results to total list
num_comps = str(sys.path[0])[len("/mnt/ufs18/home-088/f0102398/ClassicalGSG/examples/"):]

file = open("/mnt/home/f0102398/ClassicalGSG/examples/results.txt", "a")
file.write("\n")
file.write(num_comps + "\n")
file.write("Times: " + str(scores['time']) + "\n")
file.write("PCC: " + str(scores['PCC']) + "\n")
file.write("RMSE: " + str(scores['RMSE']) + "\n")
file.close()

