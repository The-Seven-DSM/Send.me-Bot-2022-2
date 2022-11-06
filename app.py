from datetime import datetime, date
import requests
import os
import mysql.connector
from PyPDF2 import PdfReader, PdfFileMerger
import time

# CONEXÃO DO MYSQL E CRIAÇÃO DO BANCO DE DADOS, INSIRA NAS VARIÁVEIS AS CREDENCIAIS

usuario = "root" # <------- COLOQUE AQUI O USUÁRIO DO MYSQL ----------------------------#
senha = "fatec" # <------- COLOQUE AQUI A SENHA DO MYSQL ---------------------------#
horario = "20:00" # <------- COLOQUE AQUI O HORÁRIO QUE DESEJA QUE O SCRIPT RODE ---------------------------#

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user=usuario,
    password=senha
    )
except:
    print("Erro ao conectar ao banco de dados, verifique as credenciais")
    exit()

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS API_a;")
mycursor.execute("use API_a;")
mycursor.execute("CREATE table IF NOT EXISTS associado( id_associado int not null primary key auto_increment, nome varchar(55), email varchar(256), genero varchar(10), cpf varchar(12), rg varchar(10), datanascimento varchar(10),escola varchar(256) );")
mycursor.execute("Create table IF NOT EXISTS backoffice(id_back int not null primary key auto_increment, nome varchar(55), senha varchar(30), email varchar(256) unique,cpf varchar(12),datanascimento varchar (10),telefone varchar(12));")
mycursor.execute("Create table IF NOT EXISTS email( id_email int not null primary key auto_increment, fk_id_associado int, corpo text(19999), pagina varchar(999), estado bool , envio bool);")
mycursor.execute("ALTER TABLE email ADD FOREIGN KEY (fk_id_associado) REFERENCES associado(id_associado) ON DELETE CASCADE;")

mydb = mysql.connector.connect(
host="localhost",
user=usuario,
password=senha, 
database="API_a"
)

mycursor = mydb.cursor()

caminho = ".\paginas"
zero = "0"
hora = horario.split(":")[0]
minuto = horario.split(":")[1]

while True: # FAZER A APLICAÇÃO RODAR SOMENTE AS 20H00
    d = datetime.now()
    print(f"EXECUTANDO, AGUARDANDO {hora}:{minuto}, Hora atual: {zero * ( 2 - len( str( d.hour ) )) + str(d.hour)}:{zero * ( 2 - len( str( d.minute ) )) + str(d.minute)}:{zero * ( 2 - len( str( d.second ) )) + str(d.second)}")

    if d.hour == int(hora) and d.minute == int(minuto):

        print("INICIANDO APLICAÇÃO")

        ano = d.strftime("%Y")
        mes = d.strftime("%m")
        meses = ['','Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

        dia = d.strftime("%d") # STR
        diaExtenso = str(dia)

        if len(diaExtenso) == 1:
            diaExtenso = "0" + diaExtenso

        diaSemana = date(int(ano), int(mes), int(dia)).isocalendar()[2]

        def formatar(n):
            a = 4 - len(str(n))
            return str(a * '0') + str(n)

        # CRIAÇÃO DA BASE DE DADOS

        base = open("base_de_dados.txt", "r", encoding = "utf8")
        
        for linha in base:
            if linha[0] != "#" and len(linha) > 3:
                mycursor.execute(linha)

        # REMOVER NOMES DUPLICADOS E BACKOFFICE DUPLICADOS

        mycursor.execute("DELETE t1 FROM backoffice t1 INNER JOIN backoffice t2 WHERE t1.id_back > t2.id_back AND t1.email = t2.email and t1.senha = t2.senha;")
        mycursor.execute("DELETE t1 FROM associado t1 INNER JOIN associado t2 WHERE t1.id_associado > t2.id_associado AND t1.nome = t2.nome AND t1.email = t2.email;")

        mydb.commit()

        if (diaSemana == 7 or diaSemana == 1): # Se for domingo ou segunda, não tem diário oficial
            print('Hoje não tem diário oficial')
            exit()

        # PEGAR TODOS OS NOMES E IDS DOS ASSOCIADOS

        mycursor.execute("SELECT id_associado, nome FROM associado")
        nomes = mycursor.fetchall()

        for caderno in ("cidade", "exec1", "exec2"):

            for pag in range(1,9999): # BAIXAR PDFS DE HOJE DOS 3 CADERNOS - DIARIO OFICIAL 

                TemCaderno = True

                if os.path.exists(f".\paginas\Caderno_{caderno}_{diaExtenso}_{mes}.pdf"):
                    break
                
                pagExtenso = formatar(pag)

                #print(f"Baixando página {pagExtenso} do caderno {caderno}")

                link = f"http://diariooficial.imprensaoficial.com.br/doflash/prototipo/{ano}/{meses[int(mes)]}/{diaExtenso}/{caderno}/pdf/pg_{pagExtenso}.pdf"

                pdf = requests.get(link)
                open(f"./paginas/{caderno}_{pagExtenso}.pdf", "wb").write(pdf.content)
                f = open(f"./paginas/{caderno}_{pagExtenso}.pdf", "r")
                if f.readline()[0:8] != "%PDF-1.4":
                    if pagExtenso == "0001":
                        print(f'Hoje não tem caderno {caderno}')
                        TemCaderno = False
                        break
                    else:
                        print(f'Ultima página do caderno "{caderno}": ', int(pagExtenso) - 1)
                    f.close()
                    if os.path.exists(f"./paginas/{caderno}_{pagExtenso}.pdf"):
                        os.remove(f"./paginas/{caderno}_{pagExtenso}.pdf")
                        break
            
            # CRIAÇÃO DOS CADERNOS UNINDO OS PDFS DAS PÁGINAS
            if TemCaderno:
                if not os.path.exists(f".\paginas\Caderno_{caderno}_{diaExtenso}_{mes}.pdf"):
                    pdfs = sorted(os.listdir(caminho))
                    pdf_files = [f for f in pdfs if f.startswith(caderno)]
                    merger = PdfFileMerger()
                    for nomeArquivo in pdf_files:
                        merger.append(PdfReader(os.path.join(caminho, nomeArquivo), "rb")) #AQUI DA ERRO
                    merger.write(os.path.join(caminho, f"Caderno_{caderno}_{diaExtenso}_{mes}.pdf"))
                    # LER OS PDFS E ENVIAR OS EMAILS
                    reader = PdfReader(f'./paginas/Caderno_{caderno}_{diaExtenso}_{mes}.pdf', "rb")
                    for i in range(reader.getNumPages()):
                        pagina = reader.getPage(i)
                        numpag = formatar(i + 1)
                        conteudo = pagina.extractText()
                        for paragrafo in conteudo.replace('"',"'").replace("  ", " ").split('\n'):
                            for nome in nomes:
                                if nome[1].upper() in paragrafo.upper(): # CODIGO DE ENVIO DE EMAIL
                                    paragrafofim = ""
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

                                    link = f"http://diariooficial.imprensaoficial.com.br/doflash/prototipo/{ano}/{meses[int(mes)]}/{diaExtenso}/{caderno}/pdf/pg_{numpag}.pdf"
                                    mycursor.execute(f'INSERT INTO email (id_email, fk_id_associado, corpo, pagina, estado, envio) VALUES (0, {nome[0]}, "{paragrafofim}", "{link}", 0, 0) ') 

        # EXCLUIR PDFS DAS PÁGINAS BAIXADAS
        pdfs = sorted(os.listdir(caminho))
        pdf_files = [f for f in pdfs if f.startswith("cidade") or f.startswith("exec1") or f.startswith("exec2")]
        for nomeArquivo in pdf_files:
            os.remove(os.path.join(caminho, nomeArquivo))

        # EXCLUIR EMAILS REPETIDOS DO BANCO DE DADOS

        mydb.commit()

        mycursor.execute("DELETE t1 FROM email t1 INNER JOIN email t2 WHERE t1.id_email < t2.id_email AND t1.fk_id_associado = t2.fk_id_associado AND t1.corpo = t2.corpo AND t1.pagina = t2.pagina")

        mydb.commit() # :D

        print("FIM DA EXECUÇÃO!")
        time.sleep(60)

    else:

        # time sleep da hora atual até as 20:00:00
        falta = datetime.combine(date.today(), datetime.strptime(f'{zero * ( 2 - len( str( hora ) )) + str(hora)}:{zero * ( 2 - len( str( minuto ) )) + str(minuto)}:00', '%H:%M:%S').time()) - d
        falta = falta.total_seconds()
        if falta < 0:
            falta = 86400 + (falta * -1)

        #segundos em horas e minutos
        horas = int(falta // 3600)
        minutos = int((falta % 3600) // 60)
        segundos = int(falta % 60)
        print(f'Faltam {horas} horas, {minutos} minutos e {segundos} segundos para a execução do programa.')
        time.sleep(falta + 1)