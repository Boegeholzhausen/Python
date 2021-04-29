import numpy as np

a = np.full((2,3), 1)
print(a)

b = np.full((3,2), 2)
print(b)

print(np.matmul(a,b))