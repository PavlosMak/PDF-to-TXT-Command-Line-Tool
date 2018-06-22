import PyPDF2
import sys
import os

dir_to_file = sys.argv[1]
dir_to_create = sys.argv[2]
filename = sys.argv[3]

protected = False

try:
    password = sys.argv[4]
    protected = True
except:
    pass

os.chdir(dir_to_create)

pdf_file = open(dir_to_file,"rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

if protected == True:
    pdf_reader.decrypt(password)

pages = pdf_reader.numPages

if filename[-4:] != ".txt":
    filename = filename + ".txt"

f = open(filename,'w')

for i in range(pages):
    page = pdf_reader.getPage(i)
    page = page.extractText()
    f.write(page)

f.close()
