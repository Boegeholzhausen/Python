# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import * 
from tkinter.ttk import *
  
# creates a Tk() object
root = Tk()
  
# sets the geometry of main 
# root window
root.geometry("200x200")
  
  
# function to open a new window 
# on a button click
def open_records():
      
    # Toplevel object which will 
    # be treated as a new window
    records = Toplevel(root)
  
    # sets the title of the
    # Toplevel widget
    records.title("New Window")
  
    # sets the geometry of toplevel
    records.geometry("200x200")
  
    # A Label widget to show in toplevel
    Label(records, 
          text ="This is a new window").pack()
  
  
label = Label(root, 
              text ="This is the main window")
  
label.pack(pady = 10)
  
# a button widget which will open a 
# new window on button click
btn = Button(root, 
             text ="Click to open a new window", 
             command = open_records)
btn.pack(pady = 10)
  
# mainloop, runs infinitely
mainloop()