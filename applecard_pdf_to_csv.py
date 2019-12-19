# -*- coding: utf-8 -*-
# Imports
import PyPDF2
import csv
import logging
from datetime import datetime
from os import path

logging.basicConfig(level=logging.INFO, format="%(message)s")

logging.info("Start: Apple Card Statements to CSV")
logging.info("-----------------------------------")

# Import AppleCard pdf statement
pdf_document = open(input("Location of pdf: "), 'rb')
pdf_object = PyPDF2.PdfFileReader(pdf_document)
total_pages = pdf_object.numPages

logging.info("PDF document imported: {pdf_doc}".format(pdf_doc=pdf_document.name))
logging.info("Total pages: {total}".format(total=total_pages))

# Convert pdf statement to readable text
pages_with_transactions = []
filtered_data_list = []
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
    filtered_data_list.extend(page_items[start_first_row:end_last_row])

logging.info("Pages with transactions: {filtered}".format(filtered=len(pages_with_transactions)))
pdf_document.close()

# Translate text information for csv-able format
def divide_chunks(input_list):
  for item in range(0, len(input_list), 5):
    yield input_list[item:item + 5]

transactions_list = list(divide_chunks(filtered_data_list))

# export as csv

logging.info("Saving CSV document of transactions...")

csv_file_name = "applecard-expenses-{date}.csv".format(date=datetime.now().strftime("%Y-%m-%d-%H%M%S%f"))
csv_path = "_export/" + csv_file_name
with open(csv_path, mode='w') as csv_file:
  csv_writer = csv.writer(csv_file)

  csv_writer.writerow(['Date', 'Description', 'DC Percentage', 'DC Value', 'Amount'])
  csv_writer.writerows(transactions_list)

if path.exists(csv_path):
  logging.info("CSV document saved to: {csv_path}".format(csv_path=csv_path))
else:
  logging.error("There was an issue saving the CSV document.")
  logging.error("Check the `export/` directory to verify no document was created, and try again.")
