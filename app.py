from datetime import datetime, date
import requests
import os
import mysql.connector
from PyPDF2 import PdfFileReader, PdfFileMerger
import time

# CONEXÃO DO MYSQL, INSIRA NAS VARIÁVEIS AS CREDENCIAIS

usuario = "root" # <------- COLOQUE AQUI O USUÁRIO DO MYSQL ----------------------------#
senha = "admin" # <------- COLOQUE AQUI A SENHA DO MYSQL ---------------------------#

zero = "0"

while True: # FAZER A APLICAÇÃO RODAR SOMENTE AS 20H00
    d = datetime.now()
    print(f"EXECUTANDO, AGUARDANDO 20:00, Hora atual: {zero * ( 2 - len( str( d.hour ) )) + str(d.hour)}:{zero * ( 2 - len( str( d.minute ) )) + str(d.minute)}:{zero * ( 2 - len( str( d.second ) )) + str(d.second)}")
    if d.hour == 22 and d.minute == 00: # <------- COLOQUE AQUI A HORA QUE DESEJA RODAR O SCRIPT

        print("INICIANDO APLICAÇÃO")

        ano = d.strftime("%Y")
        mes = d.strftime("%m")
        meses = ['','Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

        dia = d.strftime("%d") # STR
        diaExtenso = str(dia)

        if len(diaExtenso) == 1:
            diaExtenso = "0" + diaExtenso

        diaSemana = date(int(ano), int(mes), int(dia)).isocalendar()[2]

        cidadePDF = True
        exec1PDF = True
        exec2PDF = True

        def formatar(n):
            a = 4 - len(str(n))
            return str(a * '0') + str(n)

        # CONEXÃO MYSQL E CRIAÇÃO DO BANCO DE DADOS

        mydb = mysql.connector.connect(
        host="localhost",
        user=usuario,
        password=senha
        )

        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS API_a;")
        mycursor.execute("use API_a;")
        mycursor.execute("CREATE table IF NOT EXISTS associado( id_associado int not null primary key auto_increment, nome varchar(55), email varchar(256), genero varchar(10), cpf varchar(12), rg varchar(10), datanascimento varchar(10) );")
        mycursor.execute("Create table IF NOT EXISTS backoffice(id_back int not null primary key auto_increment, nome varchar(55));")
        mycursor.execute("Create table IF NOT EXISTS email( id_email int not null primary key auto_increment, fk_id_associado int, corpo text(19999), pagina varchar(999), dataenvio datetime(6), estado bool , envio bool);")
        mycursor.execute("ALTER TABLE email ADD FOREIGN KEY (fk_id_associado) REFERENCES associado(id_associado);")

        mydb = mysql.connector.connect(
        host="localhost",
        user=usuario,
        password=senha, 
        database="API_a"
        )

        mycursor = mydb.cursor()

        # CRIAÇÃO DA BASE DE DADOS

        base = open("base_de_dados.txt", "r", encoding = "utf8")

        for linha in base:
            if linha[0] != "#" and len(linha) > 3:
                mycursor.execute(linha)

        # REMOVER NOMES DUPLICADOS

        mycursor.execute("DELETE t1 FROM associado t1 INNER JOIN associado t2 WHERE t1.id_associado > t2.id_associado AND t1.nome = t2.nome AND t1.email = t2.email;")

        mydb.commit()

        # BAIXAR PDFS DE HOJE - DIARIO OFICIAL 

        if (diaSemana == 7 or diaSemana == 1): # Se for domingo ou segunda, não tem diário oficial
            print('Hoje não tem diário oficial')
            exit()

        for pag in range(1,9999):

            pagExtenso = formatar(pag)
            #print(pagExtenso)

            link1 = "http://diariooficial.imprensaoficial.com.br/doflash/prototipo/" + ano + "/" + meses[int(mes)] + "/" + diaExtenso + "/cidade/pdf/pg_" + pagExtenso + ".pdf"
            link2 = "http://diariooficial.imprensaoficial.com.br/doflash/prototipo/" + ano + "/" + meses[int(mes)] + "/" + diaExtenso + "/exec1/pdf/pg_" + pagExtenso + ".pdf"
            link3 = "http://diariooficial.imprensaoficial.com.br/doflash/prototipo/" + ano + "/" + meses[int(mes)] + "/" + diaExtenso + "/exec2/pdf/pg_" + pagExtenso + ".pdf" 

            if not cidadePDF and not exec1PDF and not exec2PDF:
                break
            
            #Checar se já existe os cadernos
            if os.path.exists(f".\paginas\Caderno_cidade_{diaExtenso}_{mes}.pdf"):
                cidadePDF = False
            if os.path.exists(f".\paginas\Caderno_exec1_{diaExtenso}_{mes}.pdf"):
                exec1PDF = False
            if os.path.exists(f".\paginas\Caderno_exec2_{diaExtenso}_{mes}.pdf"):
                exec2PDF = False

            if cidadePDF == True: # Baixar as páginas do caderno Cidade
                cidade = requests.get(link1)
                open("./paginas/cidade" + pagExtenso + ".pdf", "wb").write(cidade.content)
                f = open("./paginas/cidade" + pagExtenso + ".pdf", "r")
                if f.readline()[0:8] != "%PDF-1.4":
                    if pagExtenso == "0001":
                        print('Hoje não tem caderno Cidade')
                        cidadePDF = False
                    else:
                        print('Ultima página do caderno "Cidade": ', int(pagExtenso) - 1)
                    f.close()
                    if os.path.exists("./paginas/cidade" + pagExtenso + ".pdf"):
                        os.remove("./paginas/cidade" + pagExtenso + ".pdf")
                        cidadePDF = False

            if exec1PDF == True: #Baixar as páginas do caderno Executivo 1
                exec1 = requests.get(link2)
                open("./paginas/exec1" + pagExtenso + ".pdf", "wb").write(exec1.content)
                f = open("./paginas/exec1" + pagExtenso + ".pdf", "r")

                if f.readline()[0:8] != "%PDF-1.4":
                    if pagExtenso == "0001":
                        print("Hoje não tem caderno executivo 1")
                        exec1PDF = False
                    else:
                        print('Ultima página do caderno "Executivo 1": ', int(pagExtenso) - 1)
                    f.close()
                    if os.path.exists("./paginas/exec1" + pagExtenso + ".pdf"):
                        os.remove("./paginas/exec1" + pagExtenso + ".pdf")
                        exec1PDF = False

            if exec2PDF == True: # Baixar as páginas do caderno Executivo 2
                exec2 = requests.get(link3)
                open("./paginas/exec2" + pagExtenso + ".pdf", "wb").write(exec2.content)
                f = open("./paginas/exec2" + pagExtenso + ".pdf", "r")

                if f.readline()[0:8] != "%PDF-1.4":
                    if pagExtenso == "0001":
                        print("Hoje não tem caderno executivo 2")
                        exec2PDF = False
                    else:
                        print('Ultima página do caderno "Executivo 2": ', int(pagExtenso) - 1 )
                    f.close()
                    if os.path.exists("./paginas/exec2" + pagExtenso + ".pdf"):
                        os.remove("./paginas/exec2" + pagExtenso + ".pdf")
                        exec2PDF = False

        caminho = ".\paginas"

        pdfs = sorted(os.listdir(caminho))

        # CRIAÇÃO DOS CADERNOS UNINDO OS PDFS DAS PÁGINAS

        # CADERNO CIDADE
        if not os.path.exists(f".\paginas\Caderno_cidade_{diaExtenso}_{mes}.pdf"):
            pdf_files = [f for f in pdfs if f.startswith("cidade")]
            merger = PdfFileMerger()
            for nomeArquivo in pdf_files:
                merger.append(PdfFileReader(os.path.join(caminho, nomeArquivo), "rb"))
            merger.write(os.path.join(caminho, f"Caderno_cidade_{diaExtenso}_{mes}.pdf"))

        # CADENO EXECUTIVO 1
        if not os.path.exists(f".\paginas\Caderno_exec1_{diaExtenso}_{mes}.pdf"):
            pdf_files = [f for f in pdfs if f.startswith("exec1")]
            merger = PdfFileMerger()
            for nomeArquivo in pdf_files:
                merger.append(PdfFileReader(os.path.join(caminho, nomeArquivo), "rb"))
            merger.write(os.path.join(caminho, f"Caderno_exec1_{diaExtenso}_{mes}.pdf"))

        # CADERNO EXECUTIVO 2
        if not os.path.exists(f".\paginas\Caderno_exec2_{diaExtenso}_{mes}.pdf"):
            pdf_files = [f for f in pdfs if f.startswith("exec2")]
            merger = PdfFileMerger()
            for nomeArquivo in pdf_files:
                merger.append(PdfFileReader(os.path.join(caminho, nomeArquivo), "rb"))
            merger.write(os.path.join(caminho, f"Caderno_exec2_{diaExtenso}_{mes}.pdf"))

        #EXCLUIR PDFS DE PÁGINAS

        pdf_files = [f for f in pdfs if f.startswith("cidade") or f.startswith("exec1") or f.startswith("exec2")]
        for nomeArquivo in pdf_files:
            os.remove(os.path.join(caminho, nomeArquivo))

        mycursor.execute("SELECT id_associado, nome FROM associado")

        nomes = mycursor.fetchall()
        if nomes == []:
            print("Nenhum associado cadastrado")
            exit()
        #print(nomes)

        data = f'{ano}-{mes}-{diaExtenso}'

        # FAZER A BUSCA NO PDF CIDADE E ENVIAR PARA O BANCO DE DADOS

        reader = PdfFileReader(f'./paginas/Caderno_cidade_{diaExtenso}_{mes}.pdf')
        for i in range(reader.getNumPages()):
            pagina = reader.getPage(i)
            numpag = formatar(i + 1)
            conteudo = pagina.extractText()
            for paragrafo in conteudo.replace('"',"'").replace("  ", " ").split('\n'):
                for nome in nomes:
                    if nome[1].upper() in paragrafo.upper():

                        #print(paragrafo.upper().index(nome[1].upper()))
                        if len(paragrafo) > 2500:
                            dividido = paragrafo.upper().split(nome[1].upper(), 1)
                            if len(dividido[0]) > 1000:
                                paragrafofim += dividido[0][-1000:] + nome[1]
                            else:
                                paragrafofim += dividido[0] + nome[1]
                            if len(dividido[1]) > 1000:
                                paragrafofim += dividido[1][:1000]
                            else:
                                paragrafofim += dividido[1]
                        else:
                            paragrafofim = paragrafo

                        #print(f"len:{len(paragrafofim)} nome:{nome[1]}\n{paragrafofim}\n")

                        link1 = "http://diariooficial.imprensaoficial.com.br/doflash/prototipo/" + ano + "/" + meses[int(mes)] + "/" + diaExtenso + "/cidade/pdf/pg_" + str(numpag) + ".pdf"
                        mycursor.execute(f'INSERT INTO email VALUES ( 0, {nome[0]}, "{paragrafofim}", "{link1}", "{data}", 0, 0);')
                        paragrafofim = ""

        # FAZER A BUSCA NO PDF EXEC1 E ENVIAR PARA O BANCO DE DADOS

        reader = PdfFileReader(f'./paginas/Caderno_exec1_{diaExtenso}_{mes}.pdf')
        for i in range(reader.getNumPages()):
            pagina = reader.getPage(i)
            numpag = formatar(i + 1)
            conteudo = pagina.extractText()
            for paragrafo in conteudo.replace('"',"'").replace("  ", " ").split('\n'):
                for nome in nomes:
                    if nome[1].upper() in paragrafo.upper():

                        #print(paragrafo.upper().index(nome[1].upper()))
                        if len(paragrafo) > 2500:
                            dividido = paragrafo.upper().split(nome[1].upper(), 1)
                            if len(dividido[0]) > 1000:
                                paragrafofim += dividido[0][-1000:] + nome[1]
                            else:
                                paragrafofim += dividido[0] + nome[1]
                            if len(dividido[1]) > 1000:
                                paragrafofim += dividido[1][:1000]
                            else:
                                paragrafofim += dividido[1]
                        else:
                            paragrafofim = paragrafo

                        #print(f"len:{len(paragrafofim)} nome:{nome[1]}\n{paragrafofim}\n")

                        link2 = "http://diariooficial.imprensaoficial.com.br/doflash/prototipo/" + ano + "/" + meses[int(mes)] + "/" + diaExtenso + "/exec1/pdf/pg_" + str(numpag) + ".pdf"
                        mycursor.execute(f'INSERT INTO email VALUES (0,{nome[0]},"{paragrafofim}","{link2}", "{data}", 0, 0)')
                        paragrafofim = ""

        # FAZER A BUSCA NO PDF EXEC2 E ENVIAR PARA O BANCO DE DADOS

        reader = PdfFileReader(f'./paginas/Caderno_exec2_{diaExtenso}_{mes}.pdf')
        for i in range(reader.getNumPages()):
            pagina = reader.getPage(i)
            numpag = formatar(i + 1)
            conteudo = pagina.extractText()
            for paragrafo in conteudo.replace('"',"'").replace("  ", " ").split('\n'):
                for nome in nomes:
                    if nome[1].upper() in paragrafo.upper():

                        #print(paragrafo.upper().index(nome[1].upper()))
                        if len(paragrafo) > 2500:
                            dividido = paragrafo.upper().split(nome[1].upper(), 1)
                            if len(dividido[0]) > 1000:
                                paragrafofim += dividido[0][-1000:] + nome[1]
                            else:
                                paragrafofim += dividido[0] + nome[1]
                            if len(dividido[1]) > 1000:
                                paragrafofim += dividido[1][:1000]
                            else:
                                paragrafofim += dividido[1]
                        else:
                            paragrafofim = paragrafo

                        #print(f"len:{len(paragrafofim)} nome:{nome[1]}\n{paragrafofim}\n")

                        link3 = "http://diariooficial.imprensaoficial.com.br/doflash/prototipo/" + ano + "/" + meses[int(mes)] + "/" + diaExtenso + "/exec2/pdf/pg_" + str(numpag) + ".pdf"
                        mycursor.execute(f'INSERT INTO email VALUES (0,{nome[0]},"{paragrafofim}","{link3}", "{data}", 0, 0)')
                        paragrafofim = ""

        # EXCLUIR EMAILS REPETIDOS DO BANCO DE DADOS

        mydb.commit()

        mycursor.execute("DELETE t1 FROM email t1 INNER JOIN email t2 WHERE t1.id_email < t2.id_email AND t1.fk_id_associado = t2.fk_id_associado AND t1.corpo = t2.corpo AND t1.pagina = t2.pagina")

        mydb.commit() # :D

        print("FIM DA EXECUÇÃO!")

    else:
        time.sleep(30)