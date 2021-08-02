import pickle
import numpy as np

with open('results.pkl', 'rb') as f:
    data = pickle.load(f)


print(data)
print(list(data.keys()))
print()
print(str(len(data)))
print()
print(str(data['RMSE']))
print()
print(str(data['RMSE'][0]))