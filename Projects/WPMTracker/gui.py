import tkinter as tk
import os, time, re, datetime
import webbrowser
import pyperclip
import matplotlib.pyplot as plt
import openpyxl
import numpy as np
import pandas as pd
import pyautogui
from datetime import date
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from openpyxl import Workbook
from openpyxl.styles.borders import Border, Side
from openpyxl.styles import Color, PatternFill, Font, Border, Alignment, colors
from openpyxl.cell import Cell
import funcs.make_test as mt
import funcs.fill_excel as fe
import funcs.open_excel as oe
import funcs.copy_value as cv
import funcs.graph as gr


# chance directory
os.chdir(r"C:\Python\Projects\WPMTracker")


# GUI
root = tk.Tk()
root.title("WPM Tracker")

#root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file=r"C:\Python\Projects\WPMTracker\icons\window_icon1"))
root.iconphoto(False, tk.PhotoImage(file=r"C:\Python\Projects\WPMTracker\icons\window_icon.png"))
#root.iconbitmap(r"C:\Python\Projects\WPMTracker\icons\window_icon.ico")

background = "#97D5FF"
root.resizable(False, False)
root.geometry("+-600+250")


canvas = tk.Canvas(root, width=460, height= 800, bg=background)
canvas.grid(columnspan=2, rowspan=12)


# Values Kopieren, Werte finden und in Excel passend speichern [easy]
def getValues():
    # Kopiere Values von der Seite
    cv.copy()
    # In Excel eintragen
    fe.fill_excel_easy()

# Values Kopieren, Werte finden und in Excel passend speichern [hard]
def gethValues():
    # Kopiere Values von der Seite
    cv.copy()
    # In Excel eintragen
    fe.fill_excel_hard()


## TK Window
# heights & widths
btnh = 1
btnw = 18
btnfontsize = 14
txtfontsize = 18

# logo
logo = Image.open(r"C:\Python\Projects\WPMTracker\icons\logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(root, image=logo, borderwidth=2)
logo_label.image = logo
logo_label.grid(columnspan=3, column=0, row=0)

# Instuction 1
instructions2 = tk.Label(root, text="Make the Test")
instructions2.grid(columnspan=2, column=0, row=1)
instructions2.config(bg=background, font=("Calibri bold", txtfontsize))

test_icon = Image.open(r"C:\Python\Projects\WPMTracker\icons\test_icon.png")
test_icon = ImageTk.PhotoImage(test_icon)
test_icon_label = tk.Label(root, image=test_icon, bg = background)
test_icon_label.image = test_icon
test_icon_label.grid(columnspan=1, column=1, row=1)

# Button easy & hard speed
speed_btn = tk.Button(root, text="Easy Test", command=lambda:mt.open_browser())  # command=lambda:func()
speed_btn.grid(column=0, row=2)
speed_btn.config(bg="#0A4A1B", fg="white", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

hspeed_btn = tk.Button(root, text="Hard Test", command=lambda:mt.open_browser_hard())  # command=lambda:func()
hspeed_btn.grid(column=1, row=2)
hspeed_btn.config(bg="#920000", fg="white", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

# Button Ergebniss einlesen
result_btn = tk.Button(root, text="Copy Results", command=lambda:getValues())  # command=lambda:func()
result_btn.grid(column=0, row=3)
result_btn.config(bg="#0A4A1B", fg="white", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

hresult_btn = tk.Button(root, text="Copy Results", command=lambda:gethValues())  # command=lambda:func()
hresult_btn.grid(column=1, row=3)
hresult_btn.config(bg="#920000", fg="white", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

# Instuction 2
instructions2= tk.Label(root, text="Open Excel Files")
instructions2.grid(columnspan=3, column=0, row=4)
instructions2.config(bg=background, font=("Calibri bold", txtfontsize))

# Excel_Icon
excel_icon = Image.open(r"C:\Python\Projects\WPMTracker\icons\excel_icon.png")
excel_icon = ImageTk.PhotoImage(excel_icon)
excel_icon_label = tk.Label(root, image=excel_icon, bg = background)
excel_icon_label.image = excel_icon
excel_icon_label.grid(columnspan=1, column=1, row=4)

# Button easy & hard excel
easy_btn = tk.Button(root, text="Easy", command=lambda:oe.open_easy())  # command=lambda:func()
easy_btn.grid(column=0, row=5)
easy_btn.config(bg="#0A4A1B", fg="white", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=4)

hard_btn = tk.Button(root, text="Hard", command=lambda:oe.open_hard())  # command=lambda:func()
hard_btn.grid(column=1, row=5)
hard_btn.config(bg="#920000", fg="white", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=4)

# Instuction 3
instructions3 = tk.Label(root, text="Open Graphs")
instructions3.grid(columnspan=2, column=0, row=6)
instructions3.config(bg=background, font=("Calibri bold", txtfontsize))

# Graph_Icon
graph_icon = Image.open(r"C:\Python\Projects\WPMTracker\icons\graph_icon.png")
graph_icon = ImageTk.PhotoImage(graph_icon)
graph_icon_label = tk.Label(root, image=graph_icon, bg = background)
graph_icon_label.image = graph_icon
graph_icon_label.grid(columnspan=1, column=1, row=6)

# #16465E darkblue
# Button easy&hard graph
wpm_btn = tk.Button(root, text = "WPM", command=lambda:gr.wpm())
wpm_btn.grid(column=0, row=7)
wpm_btn.config(bg="#85C98B", fg="#181926", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

acc_btn = tk.Button(root, text = "Accuracy", command=lambda:gr.acc())
acc_btn.grid(column=0, row=8)
acc_btn.config(bg="#85C98B", fg="#181926", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

hits_btn = tk.Button(root, text = "Tastenanschläge", command=lambda:gr.hits())
hits_btn.grid(column=0, row=9)
hits_btn.config(bg="#85C98B", fg="#181926", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

hwpm_btn = tk.Button(root, text = "WPM", command=lambda:gr.hwpm())
hwpm_btn.grid(column=1, row=7)
hwpm_btn.config(bg="#FF5050", fg="#181926", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

hacc_btn = tk.Button(root, text = "Accuracy", command=lambda:gr.hacc())
hacc_btn.grid(column=1, row=8)
hacc_btn.config(bg="#FF5050", fg="#181926", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

hhits_btn = tk.Button(root, text = "Tastenanschläge", command=lambda:gr.hhits())
hhits_btn.grid(column=1, row=9)
hhits_btn.config(bg="#FF5050", fg="#181926", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

root.mainloop()