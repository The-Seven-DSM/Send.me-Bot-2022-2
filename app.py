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


senha = "admin" # <------- COLOQUE AQUI A SENHA DO MYSQL #


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
mycursor.execute("Create table IF NOT EXISTS email( id_email int not null primary key auto_increment, fk_id_associado int, corpo text(19999), pagina varchar(999), dataenvio datetime(6), estado bool , envio bool);")
mycursor.execute("ALTER TABLE email ADD FOREIGN KEY (fk_id_associado) REFERENCES associado(id_associado);")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=senha, 
  database="API_a"
)

mycursor = mydb.cursor()

#   CRIAÇÃO DA BASE DE DADOS COM PROFESSORES DA FATEC

mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "ADRIANA BEZERRA DA SILVA", "ADRIANABEZERRA@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "ADRIANA DA SILVA JACINTO", "ADRIANADA@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "AGLIBERTO DO SOCORRO CHAGAS", "AGLIBERTODO@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "ALFRED MAKOTO KABAYAMA", "ALFREDMAKOTO@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "ANA CECÍLIA RODRIGUES MEDEIROS", "ANACECÍLIA@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "ANA MARIA PEREIRA", "ANAMARIA@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "ANDRÉ HASSESSIAN", "ANDRÉHASSESSIAN@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "ANTONIO WELLINGTON SALES RIOS", "ANTONIOWELLINGTON@GMAIL.COM", "MASCULINO");')     
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "ANTÔNIO EGYDIO SÃO TIAGO GRAÇA", "ANTÔNIOEGYDIO@GMAIL.COM", "MASCULINO");')        
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "ARLEY FERREIRA DE SOUZA", "ARLEYFERREIRA@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "BRUNO PERUCHI TREVISAN", "BRUNOPERUCHI@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "CARLOS AUGUSTO LOMBARDI GARCIA", "CARLOSAUGUSTO@GMAIL.COM", "MASCULINO");')        
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "CARLOS EDUARDO BASTOS", "CARLOSEDUARDO@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "CARLOS LINEU DE FARIA E ALVES", "CARLOSLINEU@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "CELSO DE OLIVEIRA", "CELSODE@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "CLÁUDIO ETELVINO DE LIMA", "CLÁUDIOETELVINO@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "CÁSSIA CRISTINA BORDINI CINTRA", "CÁSSIACRISTINA@GMAIL.COM", "FEMININO");')        
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "CÍCERO SOARES DA SILVA", "CÍCEROSOARES@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "DANIELLE CRISTINA DE MORAIS AMORIM", "DANIELLECRISTINA@GMAIL.COM", "FEMININO");')  
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "DAWILMAR GUIMARÃES DE ARAÚJO", "DAWILMARGUIMARÃES@GMAIL.COM", "MASCULINO");')      
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "DERCY FÉLIX DA SILVA", "DERCYFÉLIX@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "DIOGO BRANQUINHO RAMOS", "DIOGOBRANQUINHO@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "EDMAR DE QUEIRÓZ FIGUEIREDO", "EDMARDE@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "EDUARDO CLEMENTE DE MEDEIROS", "EDUARDOCLEMENTE@GMAIL.COM", "MASCULINO");')        
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "EDUARDO SAKAUE", "EDUARDOSAKAUE@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "EDUARDO DE CASTRO FAUSTINO COELHO", "EDUARDODE@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "ELIANE PENHA MERGULHÃO DIAS", "ELIANEPENHA@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "EMANUEL MINEDA CARNEIRO", "EMANUELMINEDA@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "FABIANA ELOISA PASSADOR", "FABIANAELOISA@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "FABIANO SABHA WALCZAK", "FABIANOSABHA@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "FABRÍCIO GALENDE MARQUES DE CARVALHO", "FABRÍCIOGALENDE@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "FELIX ARLINDO STROTTMANN", "FELIXARLINDO@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "FERNANDO MASANORI ASHIKAGA", "FERNANDOMASANORI@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "FÁBIO JOSÉ SANTOS DE OLIVEIRA", "FÁBIOJOSÉ@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "GERALDO JOSÉ LOMBARDI DE SOUZA", "GERALDOJOSÉ@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "GERSON CARLOS FAVALLI", "GERSONCARLOS@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "GERSON DA PENHA NETO", "GERSONDA@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "GIULIANO ARAÚJO BERTOTI", "GIULIANOARAÚJO@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "GUARACI LIMA DE MORAIS", "GUARACILIMA@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "HEIDE HELOISE BERNARDI", "HEIDEHELOISE@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "HERCULANO CAMARGO ORTIZ", "HERCULANOCAMARGO@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "HUDSON ALBERTO BODE", "HUDSONALBERTO@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "JEAN CARLOS LOURENÇO COSTA", "JEANCARLOS@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "JOARES LIDOVINO DOS REIS", "JOARESLIDOVINO@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "JORGE TADAO MATSUSHIMA", "JORGETADAO@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "JOSÉ JAÉTIS ROSÁRIO", "JOSÉJAÉTIS@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "JOSÉ WALMIR GONÇALVES DUQUE", "JOSÉWALMIR@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "JULIANA FORIN PASQUINI MARTINEZ", "JULIANAFORIN@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "KLEBER GELLI", "KLEBERGELLI@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "LEÔNIDAS LOPES DE MELO", "LEÔNIDASLOPES@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "LISE VIRGÍNIA VIEIRA DE AZEVEDO", "LISEVIRGÍNIA@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "LUCAS GIOVANETTI", "LUCASGIOVANETTI@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "LUCAS GONÇALVES NADALETE", "LUCASGONÇALVES@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "LUIZ ALBERTO NOLASCO FONSECA", "LUIZALBERTO@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "LUIZ ANTÔNIO TOZI", "LUIZANTÔNIO@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "MANOEL ROMAN FILHO", "MANOELROMAN@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "MARCOS ALLAN FERREIRA GONÇALVES", "MARCOSALLAN@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "MARCOS DA SILVA E SOUZA", "MARCOSDA@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "MARCUS VINÍCIUS DO NASCIMENTO", "MARCUSVINÍCIUS@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "MARIA GORETI LOPES CEPINHO", "MARIAGORETI@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "MARIA SUELENA SANTIAGO", "MARIASUELENA@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "MARLUCE GAVIÃO SACRAMENTO DIAS", "MARLUCEGAVIÃO@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "NANCI DE OLIVEIRA", "NANCIDE@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "NEWTON EIZO YAMADA", "NEWTONEIZO@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "NILO CASTRO DOS SANTOS", "NILOCASTRO@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "NILO JERÔNIMO VIEIRA", "NILOJERÔNIMO@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "REINALDO FAGUNDES DOS SANTOS", "REINALDOFAGUNDES@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "REINALDO GEN ICHIRO ARAKAKI", "REINALDOGEN@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "REINALDO VIVEIROS CARRARO", "REINALDOVIVEIROS@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "RENATA CRISTIANE FUSVERK DA SILVA", "RENATACRISTIANE@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "RENATO GALVÃO DA SILVEIRA MUSSI", "RENATOGALVÃO@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "RISLEIDE LÚCIA DOS SANTOS", "RISLEIDELÚCIA@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "RITA DE CÁSSIA MENDONÇA SALES CONTINI", "RITADE@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "RODRIGO ELIAS PEREIRA", "RODRIGOELIAS@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "ROQUE ANTÔNIO DE MOURA", "ROQUEANTÔNIO@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "RUBENS BARRETO DA SILVA", "RUBENSBARRETO@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "SANTIAGO MARTIN LUGONES", "SANTIAGOMARTIN@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "SANZARA NHIAAIA JARDIM COSTA HASSMANN", "SANZARANHIAAIA@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "TERESINHA DE FÁTIMA NOGUEIRA", "TERESINHADE@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "TIAGO CRISTOFER AGUZZOLI COLOMBO", "TIAGOCRISTOFER@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "VERA LUCIA MONTEIRO", "VERALUCIA@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "VIVIANE RIBEIRO DE SIQUEIRA", "VIVIANERIBEIRO@GMAIL.COM", "FEMININO");')

# 10 NOMES DO CADERNO CIDADE DO DIA 13/09/2022

mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "RENATA RODRIGUES INÁCIO ELEUTÉRIO", "RENATARODRIGUES@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "ANA MARILIA DUMONT FERREIRA", "ANAFERREIRA@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "SILVIA REGINA DA ROSA VIDIGAL", "SILVIAVIDIGAL@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "GUSTAVO DO NASCIMENTO MENDES", "GUSTAVOMENDES@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "AMANDA SANTANA DOS SANTOS", "AMANDASANTOS@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "CINTIA FERREIRA LOUREIRO", "CINTIALOUREIRO@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "NUCCIA JULIA DI PRIOLO", "NUCCIAPRIOLO@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "MARCELO MEDEIROS CARVALHO", "MARCELOCARVALHO@GMAIL.COM", "MASCULINO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "LIZABETH MESSIAS VIANA TELES", "LIZABETHTELES@GMAIL.COM", "FEMININO");')
mycursor.execute('INSERT INTO ASSOCIADO VALUES (0, "ANA MARIA SOUZA DA COSTA", "ANACOSTA@GMAIL.COM", "FEMININO");')

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

# 15 NOMES DO CADERNO CIDADE DO DIA 17/09/2022

mycursor.execute("INSERT INTO associado VALUES (0, 'MARTA VIDEIRA', 'martavideira@gmail.com', 'Feminino');")
mycursor.execute("INSERT INTO associado VALUES (0, 'DENNET DE LIMA', 'dennetlima@gmail.com', 'Feminino');")
mycursor.execute("INSERT INTO associado VALUES (0, 'JOSE CARLOS DA SILVA', 'josesilva@gmail.com', 'Masculino');")
mycursor.execute("INSERT INTO associado VALUES (0, 'MEIRE LOPES TRAJAI', 'meiretrajai@gmail.com', 'Feminino');")
mycursor.execute("INSERT INTO associado VALUES (0, 'ERINELZA FONTES DE SOUZA', 'erinelzasouza@gmail.com', 'Feminino');")
mycursor.execute("INSERT INTO associado VALUES (0, 'FLÁVIO PEREIRA DOS SANTOS', 'fláviosantos@gmail.com', 'Masculino');")
mycursor.execute("INSERT INTO associado VALUES (0, 'ASSIS MARTINI DOS SANTOS', 'assissantos@gmail.com', 'Masculino');")
mycursor.execute("INSERT INTO associado VALUES (0, 'ROBERTO FIRMINO ALVES', 'robertoalves@gmail.com', 'Masculino');")
mycursor.execute("INSERT INTO associado VALUES (0, 'APARECIDA COLETA', 'aparecidacoleta@gmail.com', 'Feminino');")
mycursor.execute("INSERT INTO associado VALUES (0, 'ALEIDE ALVES DE OLIVEIRA', 'aleideoliveira@gmail.com', 'Feminino');")
mycursor.execute("INSERT INTO associado VALUES (0, 'ANTONIO JOSE PINTO CORREA', 'antoniopinto@gmail.com', 'Masculino');")
mycursor.execute("INSERT INTO associado VALUES (0, 'LEIDIMAR PONCHIO DA COSTA', 'leidimarcosta@gmail.com', 'Masculino');")
mycursor.execute("INSERT INTO associado VALUES (0, 'MARIA DE FATIMA CONSALES', 'mariaconsales@gmail.com', 'Masculino');")
mycursor.execute("INSERT INTO associado VALUES (0, 'SERGIO DONATO CIPRESSO', 'sergiocipresso@gmail.com','Masculino');")
mycursor.execute("INSERT INTO associado VALUES (0, 'ANNA MARIA MICELI','annamiceli','Feminino');")




# REMOVER NOMES DUPLICADOS

mycursor.execute("DELETE t1 FROM associado t1 INNER JOIN associado t2  WHERE t1.id_associado > t2.id_associado AND t1.nome = t2.nome;")

mydb.commit()

# BAIXAR PDFS DE HOJE - DIARIO OFICIAL 

if (diaSemana == 7 or diaSemana == 1): # Se for domingo ou segunda, não tem diário oficial
    print('Hoje não tem diário oficial')
    exit()

for pag in range(1,9999):

    pagExtenso = formatar(pag)

    link1 = "http://diariooficial.imprensaoficial.com.br/doflash/prototipo/" + ano + "/" + meses[int(mes)] + "/" + diaExtenso + "/cidade/pdf/pg_" + pagExtenso + ".pdf"
    link2 = "http://diariooficial.imprensaoficial.com.br/doflash/prototipo/" + ano + "/" + meses[int(mes)] + "/" + diaExtenso + "/exec1/pdf/pg_" + pagExtenso + ".pdf"
    link3 = "http://diariooficial.imprensaoficial.com.br/doflash/prototipo/" + ano + "/" + meses[int(mes)] + "/" + diaExtenso + "/exec2/pdf/pg_" + pagExtenso + ".pdf" 


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
                mycursor.execute(f'INSERT INTO email VALUES ( 0, {nome[0]}, "{paragrafo}", "{link1}", "{data}", 0, 0);')

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
                mycursor.execute(f'INSERT INTO email VALUES (0,{nome[0]},"{paragrafo}","{link2}", "{data}", 0, 0)')

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
                mycursor.execute(f'INSERT INTO email VALUES (0,{nome[0]},"{paragrafo}","{link3}", "{data}", 0, 0)')

mydb.commit() # :D

# TRANSFORMAR EM TXT -

# with Path(f'_{diaExtenso}_{mes}.txt').open(mode = 'w', encoding='utf-8') as output_file:
#     output_file.write(txt)

print("ACABOU")

#print(datetime.now().strftime("%M:%S")) #Mostrar o horário de término de execução do script
