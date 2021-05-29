from tkinter import *

root = Tk()

counter = 5
def myclick(output):
    global counter
    myLabel  = Label(root, text=output, width= 50)
    myLabel.pack()
    counter += 1

myButton = Button(root, text="enter", command=lambda: myclick(counter))
myButton.pack()

root.mainloop()