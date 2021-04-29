import numpy as np


#3d
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
print(b[0,1,:])

#replace
b[0,:,:] = [[9,9],[8,8]]#
print(b)

