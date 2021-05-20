import openpyxl
from tkinter import *
from tkinter.ttk import *
import os

os.chdir(r"C:\Python\Projects\WPMTracker")


def wpm():
    # open sheet easy
    workbook = openpyxl.load_workbook("WPM.xlsx")
    sheet = workbook["WPM"]

    # Data import from Excel easy
    global wpmvalues
    wpmvalues = []

    start = 2
    for i in range(start, 100000):
        if sheet.cell(row=i, column=3).value != None:
            wpmvalues.append(sheet.cell(row=i, column=3).value)
            start += 1
wpm()
maxwpm = max(wpmvalues)

def hwpm():
    # open sheet easy
    workbook = openpyxl.load_workbook("hWPM.xlsx")
    sheet = workbook["WPM"]

    # Data import from Excel easy
    global hwpmvalues
    hwpmvalues = []

    start = 2
    for i in range(start, 100000):
        if sheet.cell(row=i, column=3).value != None:
            hwpmvalues.append(sheet.cell(row=i, column=3).value)
            start += 1
hwpm()
maxhwpm = max(hwpmvalues)

def acc():
    # open sheet easy
    workbook = openpyxl.load_workbook("WPM.xlsx")
    sheet = workbook["WPM"]

    # Data import from Excel easy
    global accvalues
    accvalues = []

    start = 2
    for i in range(start, 100000):
        if sheet.cell(row=i, column=4).value != None:
            accvalues.append(sheet.cell(row=i, column=4).value)
            start += 1
acc()
maxacc = max(accvalues)


def hacc():
    # open sheet easy
    workbook = openpyxl.load_workbook("hWPM.xlsx")
    sheet = workbook["WPM"]

    # Data import from Excel easy
    global haccvalues
    haccvalues = []

    start = 2
    for i in range(start, 100000):
        if sheet.cell(row=i, column=4).value != None:
            haccvalues.append(sheet.cell(row=i, column=4).value)
            start += 1
hacc()
maxhacc = max(haccvalues)


def hits():
    # open sheet easy
    workbook = openpyxl.load_workbook("WPM.xlsx")
    sheet = workbook["WPM"]

    # Data import from Excel easy
    global hitsvalues
    hitsvalues = []

    start = 2
    for i in range(start, 100000):
        if sheet.cell(row=i, column=5).value != None:
            hitsvalues.append(sheet.cell(row=i, column=5).value)
            start += 1
hits()
maxhits = max(hitsvalues)


def hhits():
    # open sheet easy
    workbook = openpyxl.load_workbook("hWPM.xlsx")
    sheet = workbook["WPM"]

    # Data import from Excel easy
    global hhitsvalues
    hhitsvalues = []

    start = 2
    for i in range(start, 100000):
        if sheet.cell(row=i, column=5).value != None:
            hhitsvalues.append(sheet.cell(row=i, column=5).value)
            start += 1
hhits()
maxhhits = max(hhitsvalues)