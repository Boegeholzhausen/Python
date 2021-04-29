import numpy as np

# All 0s Matrix
print(np.zeros((2,2)), end="\n\n")

print(np.ones((4,2,2)))

#random
print(np.random.rand(4,2))
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(np.random.random_sample(a.shape))

print(np.random.randint(7, size=(3,3)))

print(np.identity(5))

