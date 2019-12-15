# -*- coding: utf-8 -*-
# Imports
import PyPDF2

# Import AppleCard pdf statement
applecard_pdf = open(input("Location of pdf: "), 'rb')
ac_obj = PyPDF2.PdfFileReader(applecard_pdf)
ac_total_pages = ac_obj.numPages

print("Number of pages: {pages}".format(pages=ac_total_pages))

# Convert pdf statement to readable text
transation_tables = []
for page in range(ac_total_pages):
  page_text = ac_obj.getPage(page).extractText()
  page_items = page_text.splitlines()

  if "Transactions" in page_items:
    start_first_row = page_items.index("Transactions") + 5

    transation_tables.extend(page_items[start_first_row:])

applecard_pdf.close()

# Grab relevant data from text

# Translate text information for csv format

# export as csv
