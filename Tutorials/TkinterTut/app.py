import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile


root = tk.Tk()

canvas = tk.Canvas(root, width=600, height= 300)
canvas.grid(columnspan=3, rowspan=3)


#logo
logo = Image.open(r"C:\Python\Tutorials\TkinterTut\logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=0, row=0)

#instuction
instructions= tk.Label(root, text="Easy or Hard WPM Records?", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

def open_file():
    browse_text.set("loading...")
    # file = askopenfile(parent=root, mode="rb", title="Choose a file", filetype=["*.pdf"])
    # if file == True:
    #     print("file was successfuly loaded")
    text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
    text_box.insert(1.0, "hallo")
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=1, row=3)

    browse_text.set("Browse")


#browsbutton
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)  # command=lambda:func()
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)


canvas = tk.Canvas(root, width=600, height= 250)
canvas.grid(columnspan=3)

root.mainloop()