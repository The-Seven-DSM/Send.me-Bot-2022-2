#http://diariooficial.imprensaoficial.com.br/doflash/prototipo/2022/Setembro/03/cidade/pdf/pg_0001.pdf
from datetime import datetime
from re import X
import requests
import os
import mysql.connector
from PyPDF2 import PdfFileReader, PdfFileMerger
from pathlib import Path

d = datetime.now()

ano = d.strftime("%Y")
mes = d.strftime("%m")
diaExtenso = '10'#d.strftime("%d") # STR
meses = ['','Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
dia = str(diaExtenso)
if len(dia) == 1:
    dia = "0" + dia

cidadePDF = True
exec1PDF = True
exec2PDF = True

# CONEXÃO MYSQL

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="fatec"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS API_a;")
mycursor.execute("use API_a;")
mycursor.execute("CREATE table IF NOT EXISTS associado( id_associado int not null primary key auto_increment, nome varchar(55), email varchar(256), sexo varchar(10));")
mycursor.execute("Create table IF NOT EXISTS backoffice(id_back int not null primary key auto_increment, nome varchar(55));")
mycursor.execute("Create table IF NOT EXISTS email( id_email int not null primary key auto_increment, fk_id_associado int, assunto varchar(999), corpo varchar(7999), dataenvio datetime(6), estado bool );")
mycursor.execute("ALTER TABLE email ADD FOREIGN KEY (fk_id_associado) REFERENCES associado(id_associado);")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="fatec",
  database="API_a"
)

#BAIXAR PDFS - DIARIO OFICIAL

# for pag in range(1,999):

#     if len(str(pag)) == 1:
#         pagExtenso = '000' + str(pag)
#     elif len(str(pag)) == 2:
#         pagExtenso = '00' + str(pag)
#     elif len(str(pag)) == 3:
#         pagExtenso = '0' + str(pag)
#     else:
#         pagExtenso = str(pag)

#     link1 = "http://diariooficial.imprensaoficial.com.br/doflash/prototipo/" + ano + "/" + meses[int(mes)] + "/" + dia + "/cidade/pdf/pg_" + pagExtenso + ".pdf"
#     link2 = "http://diariooficial.imprensaoficial.com.br/doflash/prototipo/" + ano + "/" + meses[int(mes)] + "/" + dia + "/exec1/pdf/pg_" + pagExtenso + ".pdf"
#     link3 = "http://diariooficial.imprensaoficial.com.br/doflash/prototipo/" + ano + "/" + meses[int(mes)] + "/" + dia + "/exec2/pdf/pg_" + pagExtenso + ".pdf"

#     if (d.strftime("%w") == 0 or d.strftime("%w") == 1):
#         print('Hoje não tem diário oficial')
#     else:
#         if not cidadePDF and not exec1PDF and not exec2PDF:
#             break
#         print(pagExtenso)
#         if cidadePDF == True:
#             cidade = requests.get(link1)
#             open("./paginas/cidade" + pagExtenso + ".pdf", "wb").write(cidade.content)
#             f = open("./paginas/cidade" + pagExtenso + ".pdf", "r")
#             if f.readline()[0:8] != "%PDF-1.4":
#                 if pagExtenso == "0001":
#                     print("Hoje não tem diário oficial")
#                 else:
#                     print('Ultima página do caderno "Cidade": ', int(pagExtenso) - 1)
#                 f.close()
#                 if os.path.exists("./paginas/cidade" + pagExtenso + ".pdf"):
#                     os.remove("./paginas/cidade" + pagExtenso + ".pdf")
#                     cidadePDF = False
#         if exec1PDF == True:
#             exec1 = requests.get(link2)
#             open("./paginas/exec1" + pagExtenso + ".pdf", "wb").write(exec1.content)
#             f = open("./paginas/exec1" + pagExtenso + ".pdf", "r")

#             if f.readline()[0:8] != "%PDF-1.4":
#                 if pagExtenso == "0001":
#                     print("Hoje não tem diário oficial")
#                 else:
#                     print('Ultima página do caderno "Executivo 1": ', int(pagExtenso) - 1)
#                 f.close()
#                 if os.path.exists("./paginas/exec1" + pagExtenso + ".pdf"):
#                     os.remove("./paginas/exec1" + pagExtenso + ".pdf")
#                     exec1PDF = False
#         if exec2PDF == True:
#             exec2 = requests.get(link3)
#             open("./paginas/exec2" + pagExtenso + ".pdf", "wb").write(exec2.content)
#             f = open("./paginas/exec2" + pagExtenso + ".pdf", "r")

#             if f.readline()[0:8] != "%PDF-1.4":
#                 if pagExtenso == "0001":
#                     print("Hoje não tem diário oficial do executivo 2")
#                 else:
#                     print('Ultima página do caderno "Executivo 2": ', int(pagExtenso) - 1 )
#                 f.close()
#                 if os.path.exists("./paginas/exec2" + pagExtenso + ".pdf"):
#                     os.remove("./paginas/exec2" + pagExtenso + ".pdf")
#                     exec2PDF = False

#UNIR PDFS

caminho = ".\paginas"

pdfs = sorted(os.listdir(caminho))

# #CIDADE
# pdf_files = [f for f in pdfs if f.startswith("cidade")]
# merger = PdfFileMerger()
# for nomeArquivo in pdf_files:
#     merger.append(PdfFileReader(os.path.join(caminho, nomeArquivo), "rb"))
# merger.write(os.path.join(caminho, f"Caderno_cidade_{diaExtenso}_{mes}.pdf"))

# #EXEC1
# pdf_files = [f for f in pdfs if f.startswith("exec1")]
# merger = PdfFileMerger()
# for nomeArquivo in pdf_files:
#     merger.append(PdfFileReader(os.path.join(caminho, nomeArquivo), "rb"))
# merger.write(os.path.join(caminho, f"Caderno_exec1_{diaExtenso}_{mes}.pdf"))

# #EXEC2
# pdf_files = [f for f in pdfs if f.startswith("exec2")]
# merger = PdfFileMerger()
# for nomeArquivo in pdf_files:
#     merger.append(PdfFileReader(os.path.join(caminho, nomeArquivo), "rb"))
# merger.write(os.path.join(caminho, f"Caderno_exec2_{diaExtenso}_{mes}.pdf"))

nome = "JOÃO PEDRO"
txt = ''

#LER PDF CIDADE

reader = PdfFileReader(f'./paginas/Caderno_cidade_{diaExtenso}_{mes}.pdf')

for i in range(reader.getNumPages()):
    pagina = reader.getPage(i)
    conteudo = pagina.extractText()
    for x in conteudo.split('\n'):
        if nome in x:
            txt += f'\nCaderno: Cidade\n Nome: "{nome}"\n Página: {i+1} \nParágrafo: {x}\n'
            print(f'\nCaderno: Cidade\n Nome: "{nome}"\n Página: {i+1} \nParágrafo: {x}\n')

#LER PDF EXECUTIVO 1

reader = PdfFileReader(f'./paginas/Caderno_exec1_{diaExtenso}_{mes}.pdf')

for i in range(reader.getNumPages()):
    pagina = reader.getPage(i)
    conteudo = pagina.extractText()
    for x in conteudo.split('\n'):
        if nome in x:
            txt += f'\nCaderno: Executivo 1\n Nome: "{nome}"\n Página: {i+1} \nParágrafo: {x}\n'
            print(f'\nCaderno: Executivo 1\n Nome: "{nome}"\n Página: {i+1} \nParágrafo: {x}\n')

#LER PDF EXECUTIVO 2

reader = PdfFileReader(f'./paginas/Caderno_exec2_{diaExtenso}_{mes}.pdf')

for i in range(reader.getNumPages()):
    pagina = reader.getPage(i)
    conteudo = pagina.extractText()
    for x in conteudo.split('\n'):
        if nome in x:
            txt += f'\nCaderno: Executivo 2\n Nome: "{nome}"\n Página: {i+1} \nParágrafo: {x}\n'
            print(f'\nCaderno: Executivo 2\n Nome: "{nome}"\n Página: {i+1} \nParágrafo: {x}\n')

# TRANSFORMA EM TXT -

with Path(f'{nome}_{diaExtenso}_{mes}.txt').open(mode = 'w', encoding='utf-8') as output_file:
    output_file.write(txt)

# RETORNAR JSON

print("\nACABOU\n")