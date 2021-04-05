import re

# def ask_for_input():
#     copy = input("copy & paste your record")
#     return copy

def searchforvalues():
    
    #copy = input("Copy & Paste the record?")
    copy = """72 WPM (Wörter pro Minute) Tastenanschläge (358 | 49) 407 Genauigkeit	85.04% Korrekte Wörter 67 Falsche Wörter 7"""

    wpm = re.compile(r'(\d|\d\d|\d\d\d) WPM')
    allwpm = wpm.findall(copy)

    hits = re.compile(r'(\d|\d\d|\d\d\d) \|')
    allhits = hits.findall(copy)

    failed = re.compile(r'(\d|\d\d|\d\d\d)\)')
    allfailed = failed.findall(copy)

    totalhits = int(allhits[0]) + int(allfailed[0])

    acc = re.compile(r'(\d\d.\d\d)\%')
    allacc = acc.findall(copy)
    
    print(f"""
    WPM: {allwpm[0]}
    Tastenanschläge: {totalhits} ({allhits[0]}|{allfailed[0]})
    Genauigkeit: {allacc[0]}%""")

searchforvalues()

