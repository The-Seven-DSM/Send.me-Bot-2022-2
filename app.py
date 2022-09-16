from datetime import datetime, date
import requests
import os
import mysql.connector

#print(datetime.now().strftime("%M:%S")) #Mostrar o horário que começa a execução do script

from PyPDF2 import PdfFileReader, PdfFileMerger
from pathlib import Path

d = datetime.now()

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


senha = "tuca123" # <------- COLOQUE AQUI A SENHA DO MYSQL #


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=senha
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS API_a;")
mycursor.execute("use API_a;")
mycursor.execute("CREATE table IF NOT EXISTS associado( id_associado int not null primary key auto_increment, nome varchar(55), email varchar(256), sexo varchar(10));")
mycursor.execute("Create table IF NOT EXISTS backoffice(id_back int not null primary key auto_increment, nome varchar(55));")
mycursor.execute("Create table IF NOT EXISTS email( id_email int not null primary key auto_increment, fk_id_associado int, corpo text(19999), pagina varchar(999), dataenvio datetime(6), estado bool );")
mycursor.execute("ALTER TABLE email ADD FOREIGN KEY (fk_id_associado) REFERENCES associado(id_associado);")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=senha, 
  database="API_a"
)

mycursor = mydb.cursor()

#   CRIAÇÃO DA BASE DE DADOS COM PROFESSORES DA FATEC

mycursor.execute("SELECT count(*) FROM associado;")
associados = mycursor.fetchall()
#print(associados[0][0])
if associados[0][0] == 0:
    mycursor.execute('INSERT INTO associado VALUES (0, "Adriana Bezerra da Silva", "adrianabezerra@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Adriana da Silva Jacinto", "adrianada@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Agliberto do Socorro Chagas", "aglibertodo@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Alfred Makoto Kabayama", "alfredmakoto@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Ana Cecília Rodrigues Medeiros", "anacecília@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Ana Maria Pereira", "anamaria@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "André Hassessian", "andréhassessian@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Antonio Wellington Sales Rios", "antoniowellington@gmail.com", "Masculino");')   
    mycursor.execute('INSERT INTO associado VALUES (0, "Antônio Egydio São Tiago Graça", "antônioegydio@gmail.com", "Masculino");')      
    mycursor.execute('INSERT INTO associado VALUES (0, "Arley Ferreira de Souza", "arleyferreira@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Bruno Peruchi Trevisan", "brunoperuchi@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Carlos Augusto Lombardi Garcia", "carlosaugusto@gmail.com", "Masculino");')      
    mycursor.execute('INSERT INTO associado VALUES (0, "Carlos Eduardo Bastos", "carloseduardo@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Carlos Lineu de Faria e Alves", "carloslineu@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Celso de Oliveira", "celsode@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Cláudio Etelvino de Lima", "cláudioetelvino@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Cássia Cristina Bordini Cintra", "cássiacristina@gmail.com", "Feminino");')      
    mycursor.execute('INSERT INTO associado VALUES (0, "Cícero Soares da Silva", "cícerosoares@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Danielle Cristina de Morais Amorim", "daniellecristina@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Dawilmar Guimarães de Araújo", "dawilmarguimarães@gmail.com", "Masculino");')    
    mycursor.execute('INSERT INTO associado VALUES (0, "Dercy Félix da Silva", "dercyfélix@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Diogo Branquinho Ramos", "diogobranquinho@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Edmar de Queiróz Figueiredo", "edmarde@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Eduardo Clemente de Medeiros", "eduardoclemente@gmail.com", "Masculino");')      
    mycursor.execute('INSERT INTO associado VALUES (0, "Eduardo Sakaue", "eduardosakaue@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Eduardo de Castro Faustino Coelho", "eduardode@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Eliane Penha Mergulhão Dias", "elianepenha@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Emanuel Mineda Carneiro", "emanuelmineda@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Fabiana Eloisa Passador", "fabianaeloisa@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Fabiano Sabha Walczak", "fabianosabha@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Fabrício Galende Marques de Carvalho", "fabríciogalende@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Felix Arlindo Strottmann", "felixarlindo@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Fernando Masanori Ashikaga", "fernandomasanori@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Fábio José Santos de Oliveira", "fábiojosé@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Geraldo José Lombardi de Souza", "geraldojosé@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Gerson Carlos Favalli", "gersoncarlos@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Gerson da Penha Neto", "gersonda@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Giuliano Araújo Bertoti", "giulianoaraújo@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Guaraci Lima de Morais", "guaracilima@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Heide Heloise Bernardi", "heideheloise@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Herculano Camargo Ortiz", "herculanocamargo@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Hudson Alberto Bode", "hudsonalberto@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Jean Carlos Lourenço Costa", "jeancarlos@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Joares Lidovino dos Reis", "joareslidovino@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Jorge Tadao Matsushima", "jorgetadao@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "José Jaétis Rosário", "joséjaétis@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "José Walmir Gonçalves Duque", "joséwalmir@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Juliana Forin Pasquini Martinez", "julianaforin@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Kleber Gelli", "klebergelli@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Leônidas Lopes de Melo", "leônidaslopes@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Lise Virgínia Vieira de Azevedo", "lisevirgínia@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Lucas Giovanetti", "lucasgiovanetti@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Lucas Gonçalves Nadalete", "lucasgonçalves@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Luiz Alberto Nolasco Fonseca", "luizalberto@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Luiz Antônio Tozi", "luizantônio@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Manoel Roman Filho", "manoelroman@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Marcos Allan Ferreira Gonçalves", "marcosallan@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Marcos da Silva e Souza", "marcosda@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Marcus Vinícius do Nascimento", "marcusvinícius@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Maria Goreti Lopes Cepinho", "mariagoreti@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Maria Suelena Santiago", "mariasuelena@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Marluce Gavião Sacramento Dias", "marlucegavião@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Nanci de Oliveira", "nancide@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Newton Eizo Yamada", "newtoneizo@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Nilo Castro dos Santos", "nilocastro@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Nilo Jerônimo Vieira", "nilojerônimo@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Reinaldo Fagundes dos Santos", "reinaldofagundes@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Reinaldo Gen Ichiro Arakaki", "reinaldogen@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Reinaldo Viveiros Carraro", "reinaldoviveiros@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Renata Cristiane Fusverk da Silva", "renatacristiane@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Renato Galvão da Silveira Mussi", "renatogalvão@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Risleide Lúcia dos Santos", "risleidelúcia@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Rita de Cássia Mendonça Sales Contini", "ritade@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Rodrigo Elias Pereira", "rodrigoelias@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Roque Antônio de Moura", "roqueantônio@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Rubens Barreto da Silva", "rubensbarreto@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Santiago Martin Lugones", "santiagomartin@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Sanzara Nhiaaia Jardim Costa Hassmann", "sanzaranhiaaia@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Teresinha de Fátima Nogueira", "teresinhade@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Tiago Cristofer Aguzzoli Colombo", "tiagocristofer@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Vera Lucia Monteiro", "veralucia@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Viviane Ribeiro de Siqueira", "vivianeribeiro@gmail.com", "Feminino");')

    # 10 NOMES DO CADERNO CIDADE DO DIA 13/09/2022

    mycursor.execute('INSERT INTO associado VALUES (0, "Renata Rodrigues Inácio Eleutério", "renatarodrigues@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Ana Marilia Dumont Ferreira", "anaferreira@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Silvia Regina da Rosa Vidigal", "silviavidigal@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Gustavo do Nascimento Mendes", "gustavomendes@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Amanda Santana dos Santos", "amandasantos@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Cintia Ferreira Loureiro", "cintialoureiro@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "Nuccia Julia Di Priolo", "nucciapriolo@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "MARCELO MEDEIROS CARVALHO", "marcelocarvalho@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "LIZABETH MESSIAS VIANA TELES", "lizabethteles@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "ANA MARIA SOUZA DA COSTA", "anacosta@gmail.com", "Feminino");')

    # 10 NOMES DO CADERNO EXECUTIVO 2 DO DIA 14/09/2022

    mycursor.execute('INSERT INTO associado VALUES (0, "ANA RODRIGUES DE FREITAS", "anafreitas@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "JOSÉ GERALDO POLON", "josepolon@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "EDUARDO APARECIDO SANCHES", "eduardosanches@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "MONICA SANDOVAL", "monicasandoval@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "LUCIANA SCALOPPE DE ALCANTARA", "lucianaalcantara@gmail.com", "Feminino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "CARLOS ALBERTO GONÇALVES DA SILVA", "carlossilva@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "LAÉRCIO AGOSTINHO FERREIRA", "laercioferreira@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "VICTOR ROSSI MONTEIRO", "victormonteiro@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "CARLOS MARCEL FLORIANO E SILVA", "carlossilva@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "EDINILSON DE SOUZA SIMAO", "edinilsonsimao@gmail.com", "Masculino");')
    mycursor.execute('INSERT INTO associado VALUES (0, "RAFAEL LUIZ CARVALHO CORREA", "rafaelcorrea@gmail.com", "Masculino");')

    # 10 NOMES DO CADERNO CIDADE DO DIA 15/09/2022

    mycursor.execute("INSERT INTO associado VALUES (0, 'RAPHAEL CAETANO DA SILVA', 'raphaelsilva@gmail.com', 'Masculino');")
    mycursor.execute("INSERT INTO associado VALUES (0, 'RAPHAEL CARLOS DE ARAÚJO', 'raphaelaraújo@gmail.com', 'Masculino');")
    mycursor.execute("INSERT INTO associado VALUES (0, 'RAPHAEL ESPIRITO SANTO SALES', 'raphaelsales@gmail.com', 'Masculino');")
    mycursor.execute("INSERT INTO associado VALUES (0, 'RAPHAEL HENRIQUE PIRES SOUSA', 'raphaelsousa@gmail.com', 'Masculino');")
    mycursor.execute("INSERT INTO associado VALUES (0, 'DHYEGO VINICIUS DE MORAES SANTOS', 'dhyegosantos@gmail.com', 'Masculino');")
    mycursor.execute("INSERT INTO associado VALUES (0, 'DIAN SENAS VIEIRA', 'dianvieira@gmail.com', 'Masculino');")
    mycursor.execute("INSERT INTO associado VALUES (0, 'DIANNA DE LURDES MACEDO MACHADO', 'diannamachado@gmail.com', 'Feminino');")
    mycursor.execute("INSERT INTO associado VALUES (0, 'DIANNE DOS SANTOS PAULINO', 'diannepaulino@gmail.com', 'Feminino');")
    mycursor.execute("INSERT INTO associado VALUES (0, 'DIEFFERSON DOS SANTOS', 'dieffersonsantos@gmail.com', 'Masculino');")
    mycursor.execute("INSERT INTO associado VALUES (0, 'FELIPE DE ARAUJO SILVA', 'felipesilva@gmail.com', 'Masculino');")

    # 10 NOMES DO CADERNO CIDADE DO DIA 16/09/2022

    mycursor.execute("INSERT INTO associado VALUES (0, 'MOHAMAD ALI KADRI', 'mohamadkadri@gmail.com', 'Masculino');")
    mycursor.execute("INSERT INTO associado VALUES (0, 'DANIELLE RODRIGUES GARCIA BERCARIO', 'daniellebercario@gmail.com', 'Feminino');")
    mycursor.execute("INSERT INTO associado VALUES (0, 'MARCELO ANTONIO RIBEIRO', 'marceloribeiro@gmail.com', 'Masculino');")
    mycursor.execute("INSERT INTO associado VALUES (0, 'MAYARA CARDIA', 'mayaracardia@gmail.com', 'Feminino');")
    mycursor.execute("INSERT INTO associado VALUES (0, 'CELESTE DA CRUZ GONCALVES REGO', 'celesterego@gmail.com', 'Feminino');")
    mycursor.execute("INSERT INTO associado VALUES (0, 'MARIA LUCIA PRATA', 'mariaprata@gmail.com', 'Feminino');")
    mycursor.execute("INSERT INTO associado VALUES (0, 'JOAO MARQUES ALEGRIA', 'joaoalegria@gmail.com', 'Masculino');")
    mycursor.execute("INSERT INTO associado VALUES (0, 'PRISCILA FRIVOLI FRANCISCO MARQUES', 'priscilamarques@gmail.com', 'Feminino');")
    mycursor.execute("INSERT INTO associado VALUES (0, 'GIANES CRISTINA RUIZ SIMOES', 'gianessimoes@gmail.com', 'Feminino');")
    mycursor.execute("INSERT INTO associado VALUES (0, 'ANA CAROLINA DE SA GASPAR', 'anagaspar@gmail.com', 'Feminino');")

mydb.commit()

# BAIXAR PDFS DE HOJE - DIARIO OFICIAL 

for pag in range(1,9999):

    pagExtenso = formatar(pag)

    link1 = "http://diariooficial.imprensaoficial.com.br/doflash/prototipo/" + ano + "/" + meses[int(mes)] + "/" + diaExtenso + "/cidade/pdf/pg_" + pagExtenso + ".pdf"
    link2 = "http://diariooficial.imprensaoficial.com.br/doflash/prototipo/" + ano + "/" + meses[int(mes)] + "/" + diaExtenso + "/exec1/pdf/pg_" + pagExtenso + ".pdf"
    link3 = "http://diariooficial.imprensaoficial.com.br/doflash/prototipo/" + ano + "/" + meses[int(mes)] + "/" + diaExtenso + "/exec2/pdf/pg_" + pagExtenso + ".pdf"

    if (diaSemana == 7 or diaSemana == 1): # Se for domingo ou segunda, não tem diário oficial
        print('Hoje não tem diário oficial')
        exit() 

    else:
        if not cidadePDF and not exec1PDF and not exec2PDF:
            break
        #print(pagExtenso)

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

# CIDADE
pdf_files = [f for f in pdfs if f.startswith("cidade")]
merger = PdfFileMerger()
for nomeArquivo in pdf_files:
    merger.append(PdfFileReader(os.path.join(caminho, nomeArquivo), "rb"))
merger.write(os.path.join(caminho, f"Caderno_cidade_{diaExtenso}_{mes}.pdf"))

# EXEC1
pdf_files = [f for f in pdfs if f.startswith("exec1")]
merger = PdfFileMerger()
for nomeArquivo in pdf_files:
    merger.append(PdfFileReader(os.path.join(caminho, nomeArquivo), "rb"))
merger.write(os.path.join(caminho, f"Caderno_exec1_{diaExtenso}_{mes}.pdf"))

# EXEC2
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
txt = ''


# FAZER A BUSCA NO PDF CIDADE E ENVIAR PARA O BANCO DE DADOS

reader = PdfFileReader(f'./paginas/Caderno_cidade_{diaExtenso}_{mes}.pdf')
data = f'{ano}-{mes}-{diaExtenso}'

nomeTeste = 'Marcela'
txt = ''

for i in range(reader.getNumPages()):
    pagina = reader.getPage(i)
    numpag = formatar(i + 1)
    conteudo = pagina.extractText()
    for paragrafo in conteudo.replace('"',"'").split('\n'):
        for nome in nomes:
            if nome[1].upper() in paragrafo.upper():
                link1 = "http://diariooficial.imprensaoficial.com.br/doflash/prototipo/" + ano + "/" + meses[int(mes)] + "/" + diaExtenso + "/cidade/pdf/pg_" + str(numpag) + ".pdf"
                #print(f'INSERT INTO email VALUES (0,{nome[0]},"{paragrafo}","{link1}","{data}",0);')
                #txt += f"Página: Cidade\nPágina: {numpag}\nLink:{link1}\nParágrafo: {paragrafo}"
                mycursor.execute(f'INSERT INTO email VALUES ( 0, {nome[0]}, "{paragrafo}", "{link1}", "{data}", 0);')

# FAZER A BUSCA NO PDF EXEC1 E ENVIAR PARA O BANCO DE DADOS

reader = PdfFileReader(f'./paginas/Caderno_exec1_{diaExtenso}_{mes}.pdf')

for i in range(reader.getNumPages()):
    pagina = reader.getPage(i)
    numpag = formatar(i + 1)
    conteudo = pagina.extractText()
    for paragrafo in conteudo.replace('"',"'").split('\n'):
        for nome in nomes:
            if nome[1].upper() in paragrafo.upper():
                link2 = "http://diariooficial.imprensaoficial.com.br/doflash/prototipo/" + ano + "/" + meses[int(mes)] + "/" + diaExtenso + "/exec1/pdf/pg_" + str(numpag) + ".pdf"
                #txt += f"Página: Executivo 1\nPágina: {numpag}\nLink:{link2}\nParágrafo: {paragrafo}"
                mycursor.execute(f'INSERT INTO email VALUES (0,{nome[0]},"{paragrafo}","{link2}", "{data}", 0)')

# FAZER A BUSCA NO PDF EXEC2 E ENVIAR PARA O BANCO DE DADOS

reader = PdfFileReader(f'./paginas/Caderno_exec2_{diaExtenso}_{mes}.pdf')

for i in range(reader.getNumPages()):
    pagina = reader.getPage(i)
    numpag = formatar(i + 1)
    conteudo = pagina.extractText()
    for paragrafo in conteudo.replace('"',"'").split('\n'):
        for nome in nomes:
            if nome[1].upper() in paragrafo.upper():
                link3 = "http://diariooficial.imprensaoficial.com.br/doflash/prototipo/" + ano + "/" + meses[int(mes)] + "/" + diaExtenso + "/exec2/pdf/pg_" + str(numpag) + ".pdf"
                #txt += f"Página: Executivo 2\nPágina: {numpag}\nLink:{link3}\nParágrafo: {paragrafo}"
                mycursor.execute(f'INSERT INTO email VALUES (0,{nome[0]},"{paragrafo}","{link3}", "{data}", 0)')

mydb.commit() # :D

# TRANSFORMAR EM TXT -

# with Path(f'_{diaExtenso}_{mes}.txt').open(mode = 'w', encoding='utf-8') as output_file:
#     output_file.write(txt)

print("ACABOU")

#print(datetime.now().strftime("%M:%S")) #Mostrar o horário de término de execução do script
