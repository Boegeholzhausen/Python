import openpyxl
import os

os.chdir(r"C:\Python\automate_the_boring_stuff\Chapter 13 - Working with Excelsheets")

wb = openpyxl.Workbook()

print(wb.get_sheet_names())

sheet = wb.get_sheet_by_name("Sheet")
print(sheet)

sheet["A1"] = 42
sheet["A2"] = "penis"

print(sheet["A1"].value)

wb.save("text.xlsx")

