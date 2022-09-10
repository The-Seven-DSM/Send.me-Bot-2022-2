from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path
import re

reader = PdfFileReader('./paginas/python0001.pdf')

page = reader.getPage(0)
page_content = page.extractText()
print(page_content)

with Path('lista_txt.txt').open(mode = 'w') as output_file:
    text = ''
    for page in reader.pages:
        text += page.extractText()
    output_file.write(text)

cade_pag = []

for page in reader.pages:
    pag_num = page['/']
    pag_txt = page.extractText()

    if 'programa' in pag_txt:
        cade_pag.append(pag_num)
print(cade_pag)

# PEGA TEXTO ESPECIFICO

input_pdf = PdfFileReader('lista.pdf')

pdf_writer = PdfFileWriter()


for page in cade_pag:
    pag_obj = input_pdf.getPage(page)
    pdf_writer.addPage(pag_obj)

pag_sentence = []

for page in reader.pages:
    pag_num = page['/']
    pag_txt = page.extractText()

    if 'CLAUDIA' in pag_txt:
        re.split('\.|\? |\!')
        pag_sentence.append(pag_num)