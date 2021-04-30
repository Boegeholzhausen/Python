import numpy as np


stats = np.array([[1,2,3],[4,5,6]])
print(stats)

#print(np.min(stats, axis = 0)) # alle firstrow

print(np.max(stats, axis = 0))

print(np.sum(stats))