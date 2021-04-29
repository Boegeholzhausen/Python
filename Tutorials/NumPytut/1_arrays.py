import numpy as np

#create
a = np.array([1,2,3], dtype="int16")
print(a)

b = np.array([[9.0,8.0,7.0], [8.0,7.0, 6.0]])
print(b)

#GetDimension
print(a.ndim)

#GetShape
print(b.shape)

#GetType
print(a.dtype)

#GetSize
print(b.itemsize)
print(b.nbytes)
