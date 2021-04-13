import os

folders = os.listdir(r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff")
print(folders)

totalSize = 0
for filename in os.listdir(r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff"):
    if os.path.isfile(os.path.join(r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff")):
        continue
    totalSize += os.path.getsize(os.path.join(r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff", filename))
print(totalSize)