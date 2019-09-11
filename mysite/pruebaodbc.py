from __future__ import print_function
import mechanicalsoup
import argparse
from getpass import getpass
from time import time, sleep
import pyodbc


print("hola")
def webscrap_mov():

    print("conectando a browser")
    browser = mechanicalsoup.StatefulBrowser(
        soup_config={'features': 'lxml'},
        raise_on_404=True,
        user_agent='MyBot/0.1: mysite.example.com/bot_info',
    )
    # Uncomment for a more verbose output:
    # browser.set_verbose(2)

    print("entrando a página")
    browser.open("https://gogutier.pythonanywhere.com/carga_mov_pallets/")
    #browser.open("http://127.0.0.1:8000/carga_mov_pallets/")
    #browser.follow_link("login")
    #print(browser.get_current_page())
    browser.select_form()
    #browser.select_form('formMain')
    print("obteniendo el transactionindex más nuevo..")
    page = browser.get_current_page()
    messages = page.find(id="ultimo")
    print(messages.text)
    row, datosextra=cargaDatos(messages.text)
    print(row)

    if (row!=None and len(row)>0):

        print("escribiendo datos de transacción en página")
        browser["TRANSACTIONINDEX"] = str(row[0])#args.username
        browser["PLANTID"] = str(row[1])#args.username
        browser["WAREHOUSE"] = str(row[2])#args.username
        browser["INTERNALSPECID"] = str(row[3])#args.username
        browser["ORDERID"] = str(row[4])#args.username
        browser["PARTID"] = str(row[5])#args.username
        browser["OPERATIONNO"] = str(row[6])#args.username
        browser["UNITTYPE"] = str(row[7])#args.username
        browser["LOADID"] = str(row[8])#args.username
        browser["UNITNO"] = str(row[9])#args.username
        browser["SOURCE"] = str(row[10])#args.username
        browser["DESTINATION"] = str(row[11])#args.username
        browser["EVENTDATETIME"] = (row[12])#args.username
        #print((row[12]))
        browser["EVENTTIME"] = str(row[13])#args.username
        browser["unidadespallet"] = datosextra[0]
        browser["kgpallet"] = datosextra[1]
        browser["m2pallet"] = datosextra[2]
        browser["alto"] = datosextra[3]
        browser["ancho"] = datosextra[4]
        browser["kguni"] = datosextra[5]
        browser["m2uni"] = datosextra[6]



    ##browser["password"] = "plant"#args.password
        print("submiteando")
        resp = browser.submit_selected()

        # Uncomment to launch a web browser on the current page:
        #browser.launch_browser()

        #print(browser.open("http://interlink.corrupac.cl"))

        #>>> browser.follow_link("forms") #sigue el link que tenga la palabra indicada
        #<Response [200]>
        #>>> browser.get_url()
    resultado=[]

    return(resultado)


def cargaDatos(ultimo):
    print("conectándose a DB..")
    flag=0

    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=192.168.8.41;'
                              'UID=cti;'
                              'PWD=ctidb;'
                              'Database=ctidb_transact;')
                              #'Trusted_Connection=yes;')
                              #DSN=QadNet;UID=CGCOM;HOST=192.168.8.7;PORT=7120;DB=cstprod;

        cursor = conn.cursor()
        flag=1
        print("Conectado a DB :D")

    except:
        print("Error al conectarse a la DB!!")
        flag=0
        #cursor.execute('SELECT TOP (10) [TRANSACTIONINDEX], [PLANTID]  FROM [ctidb_transact].[dbo].[CONVERTPROD]')
    if flag==1:

        print("iniciando consulta")

        #consulto los datos del último pallet que se movió menor al máximo transactionindex

        cursor.execute("SELECT TOP (1) [TRANSACTIONINDEX], [PLANTID] ,[WAREHOUSE],[INTERNALSPECID], [ORDERID], [PARTID], [OPERATIONNO], [UNITTYPE], [LOADID], [UNITNO],[SOURCE],[DESTINATION],[EVENTDATETIME],[EVENTTIME]  FROM [ctidb_transact].[dbo].[MVLOAD] where TRANSACTIONINDEX>"+ ultimo +" AND DESTINATION <> 'PLL' order by transactionindex asc ")



        #print("consulta exitosa")
        #print(cursor[0])
        #return(cursor[0])

        try:
            row1=cursor.fetchone()
            print(row1[8])


            cursor.execute("SELECT TOP (1) [TRANSACTIONINDEX], [WORKCENTERID], [ORDERID], [LOADID], [UNITNO], [TOTALLOADQTY], [STACKCOUNT], [LOADSIZE], [REPRINTINDICATOR], [INTERNALSPECID] FROM [ctidb_transact].[dbo].[FGLOAD] where loadid= '"+ str(row1[8]) +"' order by TRANSACTIONINDEX desc")
            #De aquí quiero el número de unidades
            #tomo el valor de ese transactionindex para obtener el número de unidades por pallet
            #for row in cursor:
            #    print(row)
            row2=cursor.fetchone()
            unidadespallet=row2[5]
            print("unidades pallet")
            print(unidadespallet)



            #acá saco las dimensiones del pallet según el útimo specID subido para ese padrón
            cursor.execute( "SELECT TOP (1) [TRANSACTIONINDEX],[INTERNALSPECID],[PARTID],[ITEMWIDTH],[ITEMLENGTH],[ITEMDEPTH],[GRADEID],[FLUTE],[SPECIALINSTR],[NUMBEROUT],[NUMBERIN],[ITEMWEIGHT] FROM [ctidb_transact].[dbo].[SPECS_INFO] where InternalspecID = '"+ str(row1[3]) + "' order by transactionindex desc")

            row3=cursor.fetchone()

            #Ahora busco las medidas: de ese padrón (asociada a la última orden que tenga el padrón nomás.)
            ancho=row3[3]
            alto=row3[4]
            pesouni=row3[11]


            kgpallet= pesouni* unidadespallet

            print("kgpallet")
            print(kgpallet)

            m2uni=ancho*alto/1000000

            m2pallet= m2uni*unidadespallet
            print("m2pallet")
            print(m2pallet)


            print("ancho")
            print(ancho)
            print("alto")
            print(alto)
            print("unidades")
            print(unidadespallet)
            print("pesouni")
            print(pesouni)
            print("m2uni")
            print(m2uni)


            datosextra = [unidadespallet, kgpallet, m2pallet, alto, ancho, pesouni, m2uni]
        except:
            row1=[]
            datosextra=[]

        return(row1, datosextra)







    else:
        print("Oh, a ocurrido un error!")

while True:
    webscrap_mov()

    sleep(1)
