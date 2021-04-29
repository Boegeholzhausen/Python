import os

for folder, subfolders, files in os.walk(r"C:\PythonCommands\Test"):
    print("Folder "+ folder)
    print("Subfolder in " + folder + " are: " + str(subfolders))
    print("file " + str(files) + "in Subfolder in " + folder + " are: " + str(subfolders))


# for file in files:
#     if file.endswith(".py") # prüfen welche 
#         shutil.copy(os.join(folder, file), os.join(folder, file + ".txt") # .py zu .txt machen