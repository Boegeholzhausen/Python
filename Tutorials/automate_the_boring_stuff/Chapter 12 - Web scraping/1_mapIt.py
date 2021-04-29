import webbrowser, sys, pyperclip

sys.argv # ["mapIt.py", "870", ...]

# Chef if command line arguments wer passed
if len(sys.argv) > 1:
    # ["mapIt.py", "870", ...] --> join zusammenfügen
    address = " ".join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.de/maps/place/Address
webbrowser.open("https://www.google.de/maps/place/" + address)

