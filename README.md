**Archiving this project:** Apple has since released the ability to [export](https://support.apple.com/en-us/HT209489) Apple Credit Card transactions to [csv](https://docs.python.org/3/library/csv.html) and [ofx](https://en.wikipedia.org/wiki/Open_Financial_Exchange).

# appleCard to csv

I was frustrated that the Apple Credit Card Statement I get on a monthly basis wasn't being offered in a spreadsheet friendly or data processable way, so I made this script that tries to parse those pdf documents for a list of transactions, and exports them to csv file.

## Usage

* `$ python applecard_pdf_to_csv.py`
* `> Location of pdf: [exact_path_to/credit_card_statement.pdf]`
* Documents created successfully are saved to a local `_export/` directory.

## Notes

* Python Version: `3.8.0` using [pyenv](https://github.com/pyenv/pyenv)
* One of my main concerns was privacy, so this script does everything locally.  
