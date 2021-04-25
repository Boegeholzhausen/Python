import matplotlib.pyplot as plt
import openpyxl
import pandas as pd
import os


# open sheet 
os.chdir(r"C:\Python\WPMTracker")
workbook = openpyxl.load_workbook("WPM.xlsx")
sheet = workbook["WPM"]

# Data import from Excel
nrvalues = []
start = 2
for i in range(start, 1000):
    if sheet.cell(row=i, column=1).value != None:
        nrvalues.append(sheet.cell(row=i, column=1).value)
        start += 1

wpmvalues = []
start2 = 2
for i in range(start2, 1000):
    if sheet.cell(row=i, column=3).value != None:
        wpmvalues.append(sheet.cell(row=i, column=3).value)
        start += 1

# Data
df=pd.DataFrame({'xvalues': nrvalues, 'yvalues': wpmvalues})

# Plot
plt.style.use("seaborn")
plt.figure(figsize=(24,8))
plt.rcParams["figure.figsize"]
plt.plot('xvalues', 'yvalues', color="#2F78BB", linewidth=3, label='WPM Tracker', data=df)
plt.title("WPM Tracker")
plt.xlabel("Nr.")
plt.ylabel("WPM")
plt.grid(True)
plt.tight_layout()
plt.show()