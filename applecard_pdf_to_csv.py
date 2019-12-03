# -*- coding: utf-8 -*-
# Imports
import PyPDF2

# Import AppleCard pdf statement
applecard_pdf = open(input("Location of pdf: "), 'rb')
ac_obj = PyPDF2.PdfFileReader(applecard_pdf)
ac_total_pages = ac_obj.numPages

print("Number of pages: {pages}".format(pages=ac_total_pages))

# Convert pdf statement to readable text

for page in range(ac_total_pages):
  print("PAGE NUMBER: {page_num}".format(page_num=page))
  page_text = ac_obj.getPage(page).extractText()
  print(page_text)
  print("\n")

applecard_pdf.close()

# Grab relevant data from text

# Translate text information for csv format

# export as csv
