import os
import pdfplumber


def get_pdf_file():
    pdf_files = [f for f in os.listdir(".") if f.endswith(".pdf")]
    return pdf_files[0]


def read_pdf(file):
    # It'll return the text from the PDF file as one string
    with pdfplumber.open(file) as pdf:
        text_file = [page.extract_text() for page in pdf.pages]
    return text_file[0]
