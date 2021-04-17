import os

helloFile = open(r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff\Chapter 09 - Reading and writing files\hello.txt", "w") # erstellt neuen Text in "Write Mode"
print(helloFile.write("PENIS")) # hinzugefügt und anzahl an zeichen printen

helloFile = open(r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff\Chapter 09 - Reading and writing files\hello.txt")
print(helloFile.read())
helloFile.close()

helloFile = open(r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff\Chapter 09 - Reading and writing files\hello.txt")
print(helloFile.readlines())
helloFile.close()

baconFile = open(r"Chapter 09 - Reading and writing files\bacon.txt", "w") #
baconFile.write("Bacon is not a vegetable.")
baconFile.close()

print(os.getcwd())

baconFile = open(r"Chapter 09 - Reading and writing files\wasgeht.txt", "a")
baconFile.write("\n\nBacon is delicious.")
baconFile.close()