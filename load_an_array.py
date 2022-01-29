import numpy as np

filename = input("Which array to load???")

arr = np.load(filename)
print(arr)