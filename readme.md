# Project Title

This project is designed to extract specific data from a tax document provided by Hacienda in PDF format. ("Modelo 190")

## Project Structure

The project consists of several Python scripts:

- `definitive.py`: This is the main script that coordinates the extraction of data from the PDF file.
- `intro_func.py`: This script contains functions for reading the PDF file.
- `support_regex.py`: This script contains various regex patterns and functions to support data extraction.
- `output.py`: This script contains functions for writing the extracted data to an Excel file.

## Dependencies

The project also requires the following Python libraries:

- openpyxl
- pdfplumber

## Running the Scripts

The main script to run is `definitive.py`. This script extracts the data from the PDF file and writes it to an Excel file.
```sh
python definitive.py
```
