# appleCard to csv

I was frustrated that the Apple Credit Card Statement I get on a monthly basis wasn't being offered in a spreadsheet friendly or data processable way, so I made this script that tries to parse those pdf documents for a list of transactions, and exports them to csv file.

## Usage

* `$ python applecard_pdf_to_csv.py`
* `> Location of pdf: [exact_path_to/credit_card_statement.pdf]`
* Documents created successfully are saved to a local `_export/` directory.

## Notes

* Python Version: `3.8.0` using [pyenv](https://github.com/pyenv/pyenv)
* One of my main concerns was privacy, so this script uses only built in python libraries, and all the data processing/parsing is done locally.  
