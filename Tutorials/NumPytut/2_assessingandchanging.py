import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

#GetSpecific element [row , col] (start by 0)
print(a[1, 5]) #or a[1,-2]
print(a[1, :]) #ganze row
print(a[:, 2]) #ganze col

#[startindex:endindex:stepsize]
print(a[0, 1:6:2])

#changingValues
a[1,5] = 20
print(a)

a[:,2] = 5
print(a)

a[:,2] = [5,0]
print(a)