# -*- coding: utf-8 -*-
# Imports
import PyPDF2

print("Start: Apple Card Statements to CSV")
print("-----------------------------------")

# Import AppleCard pdf statement
pdf_document = open(input("Location of pdf: "), 'rb')
pdf_object = PyPDF2.PdfFileReader(pdf_document)
total_pages = pdf_object.numPages

print("PDF document imported: {pdf_doc}".format(pdf_doc=pdf_document.name))
print("Total pages: {total}".format(total=total_pages))

# Convert pdf statement to readable text
pages_with_transactions = []
transactions_list = []
for page in range(total_pages):
  page_text = pdf_object.getPage(page).extractText()
  page_items = page_text.splitlines()
  page_numbering = "Page {page} /{total_pages}".format(page=page + 1, total_pages=total_pages)
  start_first_row = None
  end_last_row = None

  # Grab relevant data from text
  if "Transactions" in page_items:
    start_first_row = page_items.index("Transactions") + 5

  if page_numbering in page_items:
    end_last_row = page_items.index(page_numbering)

  if start_first_row and end_last_row:
    pages_with_transactions.append(page_numbering)
    transactions_list.extend(page_items[start_first_row:end_last_row])

print("Pages with transacrions: {filtered}".format(filtered=len(pages_with_transactions)))
pdf_document.close()

# Translate text information for csv format

# export as csv
