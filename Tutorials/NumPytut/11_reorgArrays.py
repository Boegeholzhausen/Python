import numpy as np


before = np.array([[1,2,3,4],[5,6,7,8]])
print(before.shape)

after = before.reshape((8,1))
print(after)