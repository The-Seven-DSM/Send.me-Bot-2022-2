#http://diariooficial.imprensaoficial.com.br/doflash/prototipo/2022/Setembro/03/cidade/pdf/pg_0001.pdf
from datetime import datetime
from re import X
import requests
import os
from PyPDF2 import PdfFileReader, PdfFileMerger
from pathlib import Path

d = datetime.now()

ano = d.strftime("%Y")
mes = d.strftime("%m")
diaExtenso = d.strftime("%d")
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
dia = str(diaExtenso)
if len(dia) == 1:
    dia = "0" + dia

#BAIXAR PDFS - DIARIO OFICIAL

for pag in range(1,133):

    if len(str(pag)) == 1:
        pagExtenso = '000' + str(pag)
    elif len(str(pag)) == 2:
        pagExtenso = '00' + str(pag)
    elif len(str(pag)) == 3:
        pagExtenso = '0' + str(pag)
    else:
        pagExtenso = str(pag)
    
    print(pagExtenso)

    link1 = f"http://diariooficial.imprensaoficial.com.br/doflash/prototipo/{ano}/{meses[mes]}/{dia}/cidade/pdf/pg_{pagExtenso}.pdf"
    link2 = f"http://diariooficial.imprensaoficial.com.br/doflash/prototipo/{ano}/{meses[mes]}/{dia}/exec1/pdf/pg_{pagExtenso}.pdf"
    link3 = f"http://diariooficial.imprensaoficial.com.br/doflash/prototipo/{ano}/{meses[mes]}/{dia}/exec2/pdf/pg_{pagExtenso}.pdf"

    if (d.strftime("%w") == 0 or d.strftime("%w") == 1):
        print('Hoje não tem diário oficial')
    else:
        response = requests.get(link1)
        open("./paginas/python" + pagExtenso + ".pdf", "wb").write(response.content)
        f = open("./paginas/python" + pagExtenso + ".pdf", "r")

        if f.readline()[0:8] != "%PDF-1.4":
            if pagExtenso == "0001":
                print("Hoje não tem diário oficial")
            else:
                print('Ultima página: ',pagExtenso)
            f.close()
            if os.path.exists("./paginas/python" + pagExtenso + ".pdf"):
                os.remove("./paginas/python" + pagExtenso + ".pdf")
            break

#UNIR PDF CIDADE

caminho = ".\paginas"

pdfs = sorted(os.listdir(caminho))

pdf_files = [f for f in pdfs if f.endswith("pdf")]
merger = PdfFileMerger()

for nomeArquivo in pdf_files:
    merger.append(PdfFileReader(os.path.join(caminho, nomeArquivo), "rb"))

merger.write(os.path.join(caminho, f"cidade_{diaExtenso}_{mes}.pdf"))

LER PDF CIDADE

reader = PdfFileReader(f'./paginas/cidade_{diaExtenso}_{mes}.pdf')

for i in range(reader.getNumPages()):
    pagina = reader.getPage(i)
    conteudo = pagina.extractText()
    for x in conteudo.split('\n'):
        if 'JOSE DE' in x:
            print(f'\nNome "José de" nesse parágrafo da página: {i+1} \n', x)

# TRANSFORMA EM TXT -

# with Path('teste.txt').open(mode = 'w', encoding='utf-8') as output_file:
#     output_file.write(conteudo)

# RETORNAR JSON