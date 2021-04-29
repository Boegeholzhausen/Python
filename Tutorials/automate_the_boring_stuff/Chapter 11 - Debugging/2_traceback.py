import traceback

try:
    raise Exception("ERROR!")
except:
    errorFile = open("errorInfo.txt", "w")
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print("in txt gepackt")