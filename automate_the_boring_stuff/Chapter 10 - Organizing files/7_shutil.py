import shutil
import os

helloFile = open(r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff\Chapter 09 - Reading and writing files\move.txt", "w")
helloFile.close()

#  shutil.copy(r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff\Chapter 09 - Reading and writing files\wasgeht.txt", r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff\Chapter 10 - Organizing files")
shutil.move(r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff\Chapter 09 - Reading and writing files\move.txt", r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff\Chapter 10 - Organizing files")
