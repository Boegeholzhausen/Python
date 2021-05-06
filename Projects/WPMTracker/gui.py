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


# chance directory
os.chdir(r"C:\Python\Projects\WPMTracker")


# GUI
root = tk.Tk()
root.title("WPM Tracker")
background = "#8FC8E5"
canvas = tk.Canvas(root, width=480, height= 800, bg=background)
canvas.grid(columnspan=2, rowspan=12)


# Funktionen
# Excel Öffnen
def easy():
    
    pyautogui.keyDown("winleft")
    pyautogui.press("r")
    pyautogui.keyUp("winleft")
    time.sleep(0.05)
    pyautogui.typewrite("wpm.xlsx", interval=0.01)
    pyautogui.press("enter")

def hard():
    pyautogui.keyDown("winleft")
    pyautogui.press("r")
    pyautogui.keyUp("winleft")
    time.sleep(0.05)
    pyautogui.typewrite("hwpm.xlsx", interval=0.01)
    pyautogui.press("enter")


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


# Test machen
def speed():
    webbrowser.open("https://10fastfingers.com/typing-test/german")


def hspeed():
    webbrowser.open("https://10fastfingers.com/advanced-typing-test/german")


def getValues():
    # Kopiere Values von der Seite
    pyautogui.moveTo(950, 750)
    time.sleep(0.5)
    pyautogui.drag(-295, -250, duration=0.5, button="left")
    pyautogui.keyDown("ctrl")
    pyautogui.press("c")
    pyautogui.keyUp("ctrl")

    # Path wählen und Excelfile öffnen
    os.chdir(r"C:\Python\Projects\WPMTracker")
    workbook = openpyxl.load_workbook("WPM.xlsx")
    sheet = workbook["WPM"]
    # nach Values suchen
    # pyperclip.copy("""79 WPM
    # (Wörter pro Minute)
    # Tastenanschläge	(393 | 29) 422
    # Genauigkeit	89.12%
    # Korrekte Wörter	75
    # Falsche Wörter	5""")
    text = pyperclip.paste()
    
    wpm = re.compile(r'(\d|\d\d|\d\d\d) WPM')
    allwpm = wpm.findall(text)
    
    hits = re.compile(r'(\d|\d\d|\d\d\d) \|')
    allhits = hits.findall(text)
    
    failed = re.compile(r'(\d|\d\d|\d\d\d)\)')
    allfailed = failed.findall(text)
    
    totalhits = int(allhits[0]) + int(allfailed[0])
    
    acc = re.compile(r'(\d\d.\d|\d\d.\d\d)\%')
    allacc = acc.findall(text)
    # print(allacc.sub(r'Agent \1****', 'Agent ALice gave the secret documents to Agent Bob.'))
    
    right = re.compile(r'Korrekte Wörter	(.*)')
    allright = right.findall(text)
    
    wrong = re.compile(r'Falsche Wörter	(.*)')
    allwrong = wrong.findall(text)
    
    
    # Values ausgeben (optional)
    print(f"""
    WPM: {allwpm[0]}
    Tastenanschläge: {totalhits} ({allhits[0]}|{allfailed[0]})
    Genauigkeit: {allacc[0]}%
    Korrekte Wörter: {allright[0]}
    Falsche Wörter: {allwrong[0]}
    """)
    
    
    # aktuelle Zeit festlegen
    now = datetime.datetime.now()
    print(now.strftime("%d.%m.%Y %H:%M:%S"))
    
    
    # Farben & Border
    
    red = PatternFill(start_color='DD5151', end_color='DD5151', fill_type='solid')
    
    green = PatternFill(start_color='A9D08E', end_color='A9D08E', fill_type='solid')
    
    blue = PatternFill(start_color='9BC2E6', end_color='9BC2E6', fill_type='solid')
    
    grey = PatternFill(start_color='D0CECE', end_color='D0CECE', fill_type='solid')
    
    lightgrey = PatternFill(start_color='D9D9D9', end_color='D9D9D9', fill_type='solid')
    
    white = PatternFill(start_color='FFFFFF', end_color='FFFFFF', fill_type='solid')
                       
    rightbot = Border(right=Side(style='thick'), bottom=Side(style='thin'))
    
    fontb = Font(name='Calibri', size=11, bold=True, italic=False, vertAlign=None, underline='none', strike=False, color='FF000000')
    font = Font(name='Calibri', size=11, bold=False, italic=False, vertAlign=None, underline='none', strike=False, color='FF000000')
    
    # Überprüfen, wo letzte gefüllte Zeile ist, die dann mit Werten füllen
    start = 2
    for i in range(start, 100000000):
        if sheet.cell(row=i, column=1).value == None:
            sheet.cell(row=i, column=1).alignment = Alignment(horizontal='left')
            sheet.cell(row=i, column=1).font = font
            sheet.cell(row=i, column=1).fill = white
            sheet.cell(row=i, column=1).border = rightbot
            sheet.cell(row=i, column=1).value = i-1
    
            sheet.cell(row=i, column=2).font = font
            sheet.cell(row=i, column=2).fill = lightgrey
            sheet.cell(row=i, column=2).border = rightbot
            sheet.cell(row=i, column=2).value = now
    
            sheet.cell(row=i, column=3).alignment = Alignment(horizontal='center')
            sheet.cell(row=i, column=3).font = fontb
            sheet.cell(row=i, column=3).fill = blue
            sheet.cell(row=i, column=3).border = rightbot
            sheet.cell(row=i, column=3).value = int(allwpm[0])
    
            # sheet.cell(row=i, column=4).style = "Percent"
            sheet.cell(row=i, column=4).alignment = Alignment(horizontal='center')
            sheet.cell(row=i, column=4).font = font
            sheet.cell(row=i, column=4).fill = lightgrey
            sheet.cell(row=i, column=4).border = rightbot
            sheet.cell(row=i, column=4).value = allacc[0] 
    
            sheet.cell(row=i, column=5).alignment = Alignment(horizontal='center')
            sheet.cell(row=i, column=5).font = font
            sheet.cell(row=i, column=5).fill = grey
            sheet.cell(row=i, column=5).border = rightbot
            sheet.cell(row=i, column=5).value = totalhits
    
            sheet.cell(row=i, column=6).alignment = Alignment(horizontal='center')
            sheet.cell(row=i, column=6).font = font
            sheet.cell(row=i, column=6).fill = green
            sheet.cell(row=i, column=6).border = rightbot
            sheet.cell(row=i, column=6).value = int(allhits[0])
    
            sheet.cell(row=i, column=7).alignment = Alignment(horizontal='center')
            sheet.cell(row=i, column=7).font = font
            sheet.cell(row=i, column=7).fill = red
            sheet.cell(row=i, column=7).border = rightbot
            sheet.cell(row=i, column=7).value = int(allfailed[0])
    
            sheet.cell(row=i, column=8).alignment = Alignment(horizontal='center')
            sheet.cell(row=i, column=8).font = font
            sheet.cell(row=i, column=8).fill = green
            sheet.cell(row=i, column=8).border = rightbot
            sheet.cell(row=i, column=8).value = int(allright[0])
    
            sheet.cell(row=i, column=9).alignment = Alignment(horizontal='center')
            sheet.cell(row=i, column=9).font = font
            sheet.cell(row=i, column=9).fill = red
            sheet.cell(row=i, column=9).border = rightbot
            sheet.cell(row=i, column=9).value = int(allwrong[0])
            break
        else:
            start += 1
    
    workbook.save("WPM.xlsx")


def gethValues():
    # Kopiere Values von der Seite
    pyautogui.moveTo(950, 750)
    time.sleep(0.5)
    pyautogui.drag(-295, -250, duration=0.5, button="left")
    pyautogui.keyDown("ctrl")
    pyautogui.press("c")
    pyautogui.keyUp("ctrl")

    # Path wählen und Excelfile öffnen
    os.chdir(r"C:\Python\Projects\WPMTracker")
    workbook = openpyxl.load_workbook("hWPM.xlsx")
    sheet = workbook["WPM"]

    # nach Values suchen
    # pyperclip.copy("""79 WPM
    # (Wörter pro Minute)
    # Tastenanschläge	(393 | 29) 422
    # Genauigkeit	89.12%
    # Korrekte Wörter	75
    # Falsche Wörter	5""")
    text = pyperclip.paste()

    wpm = re.compile(r'(\d|\d\d|\d\d\d) WPM')
    allwpm = wpm.findall(text)

    hits = re.compile(r'(\d|\d\d|\d\d\d) \|')
    allhits = hits.findall(text)

    failed = re.compile(r'(\d|\d\d|\d\d\d)\)')
    allfailed = failed.findall(text)

    totalhits = int(allhits[0]) + int(allfailed[0])

    acc = re.compile(r'(\d\d.\d|\d\d.\d\d)\%')
    allacc = acc.findall(text)
    # print(allacc.sub(r'Agent \1****', 'Agent ALice gave the secret documents to Agent Bob.'))

    right = re.compile(r'Korrekte Wörter	(.*)')
    allright = right.findall(text)

    wrong = re.compile(r'Falsche Wörter	(.*)')
    allwrong = wrong.findall(text)


    # Values ausgeben (optional)
    print(f"""
    WPM: {allwpm[0]}
    Tastenanschläge: {totalhits} ({allhits[0]}|{allfailed[0]})
    Genauigkeit: {allacc[0]}%
    Korrekte Wörter: {allright[0]}
    Falsche Wörter: {allwrong[0]}
    """)


    # aktuelle Zeit festlegen
    now = datetime.datetime.now()
    print(now.strftime("%d.%m.%Y %H:%M:%S"))


    # Farben & Border

    red = PatternFill(start_color='DD5151', end_color='DD5151', fill_type='solid')

    green = PatternFill(start_color='A9D08E', end_color='A9D08E', fill_type='solid')

    blue = PatternFill(start_color='9BC2E6', end_color='9BC2E6', fill_type='solid')

    grey = PatternFill(start_color='D0CECE', end_color='D0CECE', fill_type='solid')

    lightgrey = PatternFill(start_color='D9D9D9', end_color='D9D9D9', fill_type='solid')

    white = PatternFill(start_color='FFFFFF', end_color='FFFFFF', fill_type='solid')

    rightbot = Border(right=Side(style='thick'), bottom=Side(style='thin'))

    fontb = Font(name='Calibri', size=11, bold=True, italic=False, vertAlign=None, underline='none', strike=False, color='FF000000')
    font = Font(name='Calibri', size=11, bold=False, italic=False, vertAlign=None, underline='none', strike=False, color='FF000000')


    # Überprüfen, wo letzte gefüllte Zeile ist, die dann mit Werten füllen
    start = 2
    for i in range(start, 100000000):
        if sheet.cell(row=i, column=1).value == None:
            sheet.cell(row=i, column=1).alignment = Alignment(horizontal='left')
            sheet.cell(row=i, column=1).font = font
            sheet.cell(row=i, column=1).fill = white
            sheet.cell(row=i, column=1).border = rightbot
            sheet.cell(row=i, column=1).value = i-1

            sheet.cell(row=i, column=2).font = font
            sheet.cell(row=i, column=2).fill = lightgrey
            sheet.cell(row=i, column=2).border = rightbot
            sheet.cell(row=i, column=2).value = now

            sheet.cell(row=i, column=3).alignment = Alignment(horizontal='center')
            sheet.cell(row=i, column=3).font = fontb
            sheet.cell(row=i, column=3).fill = blue
            sheet.cell(row=i, column=3).border = rightbot
            sheet.cell(row=i, column=3).value = int(allwpm[0])

            # sheet.cell(row=i, column=4).style = "Percent"
            sheet.cell(row=i, column=4).alignment = Alignment(horizontal='center')
            sheet.cell(row=i, column=4).font = font
            sheet.cell(row=i, column=4).fill = lightgrey
            sheet.cell(row=i, column=4).border = rightbot
            sheet.cell(row=i, column=4).value = allacc[0] 

            sheet.cell(row=i, column=5).alignment = Alignment(horizontal='center')
            sheet.cell(row=i, column=5).font = font
            sheet.cell(row=i, column=5).fill = grey
            sheet.cell(row=i, column=5).border = rightbot
            sheet.cell(row=i, column=5).value = totalhits

            sheet.cell(row=i, column=6).alignment = Alignment(horizontal='center')
            sheet.cell(row=i, column=6).font = font
            sheet.cell(row=i, column=6).fill = green
            sheet.cell(row=i, column=6).border = rightbot
            sheet.cell(row=i, column=6).value = int(allhits[0])

            sheet.cell(row=i, column=7).alignment = Alignment(horizontal='center')
            sheet.cell(row=i, column=7).font = font
            sheet.cell(row=i, column=7).fill = red
            sheet.cell(row=i, column=7).border = rightbot
            sheet.cell(row=i, column=7).value = int(allfailed[0])

            sheet.cell(row=i, column=8).alignment = Alignment(horizontal='center')
            sheet.cell(row=i, column=8).font = font
            sheet.cell(row=i, column=8).fill = green
            sheet.cell(row=i, column=8).border = rightbot
            sheet.cell(row=i, column=8).value = int(allright[0])

            sheet.cell(row=i, column=9).alignment = Alignment(horizontal='center')
            sheet.cell(row=i, column=9).font = font
            sheet.cell(row=i, column=9).fill = red
            sheet.cell(row=i, column=9).border = rightbot
            sheet.cell(row=i, column=9).value = int(allwrong[0])
            break
        else:
            start += 1

    workbook.save("hWPM.xlsx")


# heights & widths
btnh = 1
btnw = 15
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
instructions2.config(bg="#8FC8E5", font=("Calibri bold", txtfontsize))

test_icon = Image.open(r"C:\Python\Projects\WPMTracker\icons\test_icon.png")
test_icon = ImageTk.PhotoImage(test_icon)
test_icon_label = tk.Label(root, image=test_icon, bg = background)
test_icon_label.image = test_icon
test_icon_label.grid(columnspan=1, column=1, row=1)


# Button easy & hard speed
speed_btn = tk.Button(root, text="Easy Test", command=lambda:speed())  # command=lambda:func()
speed_btn.grid(column=0, row=2)
speed_btn.config(bg="#0A4A1B", fg="white", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=5)

hspeed_btn = tk.Button(root, text="Hard Test", command=lambda:hspeed())  # command=lambda:func()
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
instructions2.config(bg="#8FC8E5", font=("Calibri bold", txtfontsize))

excel_icon = Image.open(r"C:\Python\Projects\WPMTracker\icons\excel_icon.png")
excel_icon = ImageTk.PhotoImage(excel_icon)
excel_icon_label = tk.Label(root, image=excel_icon, bg = background)
excel_icon_label.image = excel_icon
excel_icon_label.grid(columnspan=1, column=1, row=4)


# Button easy & hard excel
easy_btn = tk.Button(root, text="Easy", command=lambda:easy())  # command=lambda:func()
easy_btn.grid(column=0, row=5)
easy_btn.config(bg="#0A4A1B", fg="white", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=4)

hard_btn = tk.Button(root, text="Hard", command=lambda:hard())  # command=lambda:func()
hard_btn.grid(column=1, row=5)
hard_btn.config(bg="#920000", fg="white", font=("Calibri bold", btnfontsize), height=btnh, width=btnw, borderwidth=4)



# Instuction 3
instructions3 = tk.Label(root, text="Open Graphs")
instructions3.grid(columnspan=2, column=0, row=6)
instructions3.config(bg="#8FC8E5", font=("Calibri bold", txtfontsize))


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