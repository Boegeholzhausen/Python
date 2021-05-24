import openpyxl
from tkinter import *
from tkinter.ttk import *
import os
import pandas as pd


os.chdir(r"C:\Python\Projects\FitnessTracker")

plan = {"1": "Übung_1",
        "2": "Übung_2",
        "3": "Übung_3",
        "4": "Übung_4",
        "5": "Übung_5",
        "6": "Übung_6",
        "7": "Übung_7"
}

def exer1(Übung):
    global dfset1
    global dfset2
    global dfset3
    global exer
    # open sheet easy
    workbook = openpyxl.load_workbook("Workout.xlsx")
    sheet = workbook[Übung]

    # Data import from Excel easy
    nrvalues = []
    start = 2
    for i in range(start, 1000):
        if sheet.cell(row=i, column=1).value != None:
            nrvalues.append(sheet.cell(row=i, column=1).value)
            start += 1

    set1 = []
    start = 2
    for i in range(start, 1000):
        if sheet.cell(row=i, column=3).value != None:
            set1.append(sheet.cell(row=i, column=3).value)
            start += 1

    set2 = []
    start = 2
    for i in range(start, 1000):
        if sheet.cell(row=i, column=4).value != None:
            set2.append(sheet.cell(row=i, column=4).value)
            start += 1 

    set3 = []
    start = 2
    for i in range(start, 1000):
        if sheet.cell(row=i, column=5).value != None:
            set3.append(sheet.cell(row=i, column=5).value)
            start += 1 

    # Aktuelle Übung        
    exer = sheet.cell(row=1, column=8).value

    # Data
    dfset1 = pd.DataFrame({'xvalues': nrvalues, 'yvalues': set1})
    dfset2 = pd.DataFrame({'xvalues': nrvalues, 'yvalues': set2})
    dfset3 = pd.DataFrame({'xvalues': nrvalues, 'yvalues': set3})

exer1("Übung_1")