import numpy as np

#stacking arrays
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack([v1,v2,v1,v2]))


h1 = np.ones((2,4))
h2 = np.zeros((2,4))
h3 = np.hstack((h1,h2))

print(h3)