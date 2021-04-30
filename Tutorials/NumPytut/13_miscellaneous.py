import numpy as np

filedata = np.genfromtxt(r"C:\Python\Tutorials\NumPytut\data.txt", delimiter= ",")

filedata = filedata.astype("int32")
print(filedata)

print("\n")

print(filedata > 50) # gibt true false aus

print("\n")

fd = filedata[filedata > 50] # nimmt values > 50 an
print(fd)

print(np.all(filedata > 50, axis=0))

print(((filedata > 50) & (filedata < 100))) # ~ not [!=]