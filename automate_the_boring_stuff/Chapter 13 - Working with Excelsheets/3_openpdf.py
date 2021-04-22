import PyPDF2
import os

os.chdir(r"C:\Python\automate_the_boring_stuff\Chapter 13 - Working with Excelsheets")
pdfFile = open("meetingminutes1.pdf", "rb")
reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)
page = reader.getPage(0)
print(page)
print(page.extractText())

# alle PDF Seiten lesen
# for pageNum in range(reader.numPages):
#     print(reader.getPage(pageNum).extractText())

