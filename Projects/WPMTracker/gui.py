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



# chance directory
os.chdir(r"C:\Python\Projects\WPMTracker")


# GUI
root = tk.Tk()
root.title("WPM Tracker")
background = "#97D5FF"
root.resizable(False, False)

canvas = tk.Canvas(root, width=480, height= 800, bg=background)
canvas.grid(columnspan=2, rowspan=12)



## Graphs
def wpm():
    # open sheet easy
    workbook = openpyxl.load_workbook("WPM.xlsx")
    sheet = workbook["WPM"]

    # Data import from Excel easy
    nrvalues = []
    start = 2
    for i in range(start, 1000):
        if sheet.cell(row=i, column=1).value != None:
            nrvalues.append(sheet.cell(row=i, column=1).value)
            start += 1

    wpmvalues = []
    start = 2
    for i in range(start, 1000):
        if sheet.cell(row=i, column=3).value != None:
            wpmvalues.append(sheet.cell(row=i, column=3).value)
            start += 1

    # Data
    dfwpm=pd.DataFrame({'xvalues': nrvalues, 'yvalues': wpmvalues})

    # Plot WPM
    plt.style.use("seaborn")
    plt.figure(figsize=(23,5))
    plt.rcParams["figure.figsize"]
    plt.plot('xvalues', 'yvalues', color="#2F78BB", linewidth=3, label='WPM Tracker (WPM)', data=dfwpm)
    plt.title("WPM Tracker (WPM)")
    plt.xlabel("Nr.")
    plt.ylabel("WPM")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def acc():
    # open sheet easy
    workbook = openpyxl.load_workbook("WPM.xlsx")
    sheet = workbook["WPM"]

    # Data import from Excel easy
    nrvalues = []
    start = 2
    for i in range(start, 1000):
        if sheet.cell(row=i, column=1).value != None:
            nrvalues.append(sheet.cell(row=i, column=1).value)
            start += 1


    accvalues = []
    newacc = []
    start = 2
    for i in range(start, 1000):
        if sheet.cell(row=i, column=4).value != None:
            accvalues.append(sheet.cell(row=i, column=4).value)
            start += 1
            word = accvalues[i-2]
            newacc.append(float(word))

    # Data
    dfacc=pd.DataFrame({'xvalues': nrvalues, 'yvalues': newacc})

    # Plot Acc
    plt.style.use("seaborn")
    plt.figure(figsize=(23,5))
    plt.rcParams["figure.figsize"]
    plt.plot('xvalues', 'yvalues', color="#2F78BB", linewidth=3, label='WPM Tracker (Accuracy)', data=dfacc)
    plt.title("WPM Tracker (Accuracy)")
    plt.xlabel("Nr.")
    plt.ylabel("%")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def hits():
    # open sheet easy
    workbook = openpyxl.load_workbook("WPM.xlsx")
    sheet = workbook["WPM"]

    # Data import from Excel easy
    nrvalues = []
    start = 2
    for i in range(start, 1000):
        if sheet.cell(row=i, column=1).value != None:
            nrvalues.append(sheet.cell(row=i, column=1).value)
            start += 1

    hitsvalues = []
    start = 2
    for i in range(start, 1000):
        if sheet.cell(row=i, column=5).value != None:
            hitsvalues.append(sheet.cell(row=i, column=5).value)
            start += 1

    # Data
    dfhits=pd.DataFrame({'xvalues': nrvalues, 'yvalues': hitsvalues})

    # Plot Tastenanschläge
    plt.style.use("seaborn")
    plt.figure(figsize=(23,5))
    plt.rcParams["figure.figsize"]
    plt.plot('xvalues', 'yvalues', color="#2F78BB", linewidth=3, label='WPM Tracker (Tastenanschläge)', data=dfhits)
    plt.title("WPM Tracker (Tastenanschläge)")
    plt.xlabel("Nr.")
    plt.ylabel("Tastenanschläge")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def hwpm():
    # open sheet hard
    hworkbook = openpyxl.load_workbook("hWPM.xlsx")
    hsheet = hworkbook["WPM"]

    hnrvalues = []
    start = 2
    for i in range(start, 1000):
        if hsheet.cell(row=i, column=1).value != None:
            hnrvalues.append(hsheet.cell(row=i, column=1).value)
            start += 1

    # Data import from Excel hard
    hwpmvalues = []
    start = 2
    for i in range(start, 1000):
        if hsheet.cell(row=i, column=3).value != None:
            hwpmvalues.append(hsheet.cell(row=i, column=3).value)
            start += 1

    # Data
    dfhwpm=pd.DataFrame({'xvalues': hnrvalues, 'yvalues': hwpmvalues})
    

    # Plot WPM [hard]
    plt.style.use("seaborn")
    plt.figure(figsize=(23,5))
    plt.rcParams["figure.figsize"]
    plt.plot('xvalues', 'yvalues', color="#2F78BB", linewidth=3, label='WPM Tracker (WPM) [Hard]', data=dfhwpm)
    plt.title("WPM Tracker (WPM) [Hard]")
    plt.xlabel("Nr.")
    plt.ylabel("WPM")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def hacc():
    # open sheet hard
    hworkbook = openpyxl.load_workbook("hWPM.xlsx")
    hsheet = hworkbook["WPM"]

    hnrvalues = []
    start = 2
    for i in range(start, 1000):
        if hsheet.cell(row=i, column=1).value != None:
            hnrvalues.append(hsheet.cell(row=i, column=1).value)
            start += 1

    # Data import from Excel hard
    haccvalues = []
    hnewacc = []
    start = 2
    for i in range(start, 1000):
        if hsheet.cell(row=i, column=4).value != None:
            haccvalues.append(hsheet.cell(row=i, column=4).value)
            start += 1
            word = haccvalues[i-2]
            hnewacc.append(float(word))

    # Data
    dfhacc=pd.DataFrame({'xvalues': hnrvalues, 'yvalues': hnewacc})

    # Plot Acc [hard]
    plt.style.use("seaborn")
    plt.figure(figsize=(23,5))
    plt.rcParams["figure.figsize"]
    plt.plot('xvalues', 'yvalues', color="#2F78BB", linewidth=3, label='WPM Tracker (Accuracy) [Hard]', data=dfhacc)
    plt.title("WPM Tracker (Accuracy) [Hard]")
    plt.xlabel("Nr.")
    plt.ylabel("%")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def hhits():
    # open sheet hard
    hworkbook = openpyxl.load_workbook("hWPM.xlsx")
    hsheet = hworkbook["WPM"]

    hnrvalues = []
    start = 2
    for i in range(start, 1000):
        if hsheet.cell(row=i, column=1).value != None:
            hnrvalues.append(hsheet.cell(row=i, column=1).value)
            start += 1

    # Data import from Excel hard
    hhitsvalues = []
    start = 2
    for i in range(start, 1000):
        if hsheet.cell(row=i, column=5).value != None:
            hhitsvalues.append(hsheet.cell(row=i, column=5).value)
            start += 1

    # Data
    dfhhits=pd.DataFrame({'xvalues': hnrvalues, 'yvalues': hhitsvalues})
    

    # Plot Tastenanschläge [hard]
    plt.style.use("seaborn")
    plt.figure(figsize=(23,5))
    plt.rcParams["figure.figsize"]
    plt.plot('xvalues', 'yvalues', color="#2F78BB", linewidth=3, label='WPM Tracker (Tastenanschläge) [Hard]', data=dfhhits)
    plt.title("WPM Tracker (Tastenanschläge) [Hard]")
    plt.xlabel("Nr.")
    plt.ylabel("Tastenanschläge")
    plt.grid(True)
    plt.tight_layout()
    plt.show()



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
btnw = 16
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
wpm_btn = tk.Button(root, text = "WPM", command=lambda:wpm())
wpm_btn.grid(column=0, row=7)
wpm_btn.config(bg="#85C98B", fg="#181926", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

acc_btn = tk.Button(root, text = "Accuracy", command=lambda:acc())
acc_btn.grid(column=0, row=8)
acc_btn.config(bg="#85C98B", fg="#181926", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

hits_btn = tk.Button(root, text = "Tastenanschläge", command=lambda:hits())
hits_btn.grid(column=0, row=9)
hits_btn.config(bg="#85C98B", fg="#181926", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

hwpm_btn = tk.Button(root, text = "WPM", command=lambda:hwpm())
hwpm_btn.grid(column=1, row=7)
hwpm_btn.config(bg="#FF5050", fg="#181926", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

hacc_btn = tk.Button(root, text = "Accuracy", command=lambda:hacc())
hacc_btn.grid(column=1, row=8)
hacc_btn.config(bg="#FF5050", fg="#181926", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

hhits_btn = tk.Button(root, text = "Tastenanschläge", command=lambda:hhits())
hhits_btn.grid(column=1, row=9)
hhits_btn.config(bg="#FF5050", fg="#181926", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

root.mainloop()