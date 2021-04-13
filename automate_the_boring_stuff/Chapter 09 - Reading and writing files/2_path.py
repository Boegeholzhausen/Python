import os

path = r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff"

print(os.sep)
print(os.path.join("c:", "User"))
print("current dir is: " + os.getcwd())

print(os.path.abspath("1_input.py"))

print("\n")
# print(os.path.isabs("C:\\1_input.py"))

print("\nyour path rel is: \n" + os.path.relpath(r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff\Chapter 08 - Input Validation\1_input.py", r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff"))

print("\nis this your working path? \n" + str(os.path.isabs(r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff\Chapter 08 - Input Validation\1_input.py")))

print("\nthis is your Foldername: \n" + os.path.dirname(r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff\Chapter 08 - Input Validation\1_input.py"))

print("\nyour last file is: \n" + os.path.basename(r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff\Chapter 08 - Input Validation\1_input.py"))

print(os.path.exists(r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff\Chapter 08 - Input Validation\1_input.py"))

print("Your file \"" + str(os.path.basename(r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff\Chapter 08 - Input Validation\1_input.py")) + "\" is " + str(os.path.getsize(r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff\Chapter 08 - Input Validation\1_input.py")) + " bits big.")