import re
import pyperclip
import xlsxwriter
import datetime
import time
from datetime import time
from datetime import date

def getValues(copy):

    # copy = pyperclip.paste()
    # copy = '''
    # 94 WPM
    # (Wörter pro Minute)
    # Top 20 %
    # Tastenanschläge	(468 | 28) 496
    # Genauigkeit	93.41%
    # Korrekte Wörter	86
    # Falsche Wörter	5
    # '''

    wpm = re.compile(r'(\d|\d\d|\d\d\d) WPM')
    allwpm = wpm.findall(copy)

    hits = re.compile(r'(\d|\d\d|\d\d\d) \|')
    allhits = hits.findall(copy)

    failed = re.compile(r'(\d|\d\d|\d\d\d)\)')
    allfailed = failed.findall(copy)

    totalhits = int(allhits[0]) + int(allfailed[0])

    acc = re.compile(r'(\d\d.\d\d)\%')
    allacc = acc.findall(copy)

    right = re.compile(r'Korrekte Wörter	(.*)')
    allright = right.findall(copy)

    wrong = re.compile(r'Falsche Wörter	(.*)')
    allwrong = wrong.findall(copy)

    print(f"""
    WPM: {allwpm[0]}
    Tastenanschläge: {totalhits} ({allhits[0]}|{allfailed[0]})
    Genauigkeit: {allacc[0]}%
    Korrekte Wörter: {allright[0]}
    Falsche Wörter: {allwrong[0]}
    """)
    
    values = [allwpm[0], totalhits, allhits[0], allfailed[0], allacc[0], allright[0], allwrong[0]]
    print(values)


getValues(pyperclip.paste())

# text = '''
# 94 WPM
# (Wörter pro Minute)
# Top 20 %
# Tastenanschläge	(468 | 28) 496
# Genauigkeit	93.41%
# Korrekte Wörter	86
# Falsche Wörter	5
# '''
# getValues(text)


# excel
outWorkbook = xlsxwriter.Workbook("WPM.xlsx")
outSheet = outWorkbook.add_worksheet()


now = datetime.datetime.now()
print(now.strftime("%d.%m.%Y %H:%M:%S"))

names = [now.strftime("%d.%m.%Y %H:%M:%S")]
values = [70, 82, 71]

outSheet.write("B1", "WPM")
outSheet.write("C1", "Tastenanschläge")
outSheet.write("D1", "davon richtig")
outSheet.write("E1", "davon falsch")
outSheet.write("F1", "Genauigkeit")
outSheet.write("G1", "Korrekte Wörter")
outSheet.write("H1", "Falsche Wörter")

for item in range(len(names)):
    outSheet.write(item+1, 0, names[item])
    outSheet.write(item+1, 1, values[item])

outWorkbook.close()