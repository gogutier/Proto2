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
    #browser.follow_link("login")
    #print(browser.get_current_page())
    browser.select_form()
    #browser.select_form('formMain')
    print("obteniendo el transactionindex más nuevo..")
    page = browser.get_current_page()
    messages = page.find(id="ultimo")
    print(messages.text)
    row=cargaDatos(messages.text)
    print(row)

    if (row!=None):
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
        print((row[12]))
        browser["EVENTTIME"] = str(row[13])#args.username


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

        cursor.execute('SELECT TOP (1) [TRANSACTIONINDEX],[PLANTID] ,[WAREHOUSE],[INTERNALSPECID], [ORDERID], [PARTID], [OPERATIONNO], [UNITTYPE], [LOADID], [UNITNO],[SOURCE],[DESTINATION],[EVENTDATETIME],[EVENTTIME]  FROM [ctidb_transact].[dbo].[MVLOAD] where TRANSACTIONINDEX>'+ ultimo +' order by transactionindex asc ')

        print("consulta exitosa")
        print(cursor)

        for row in cursor:

                return(row)

                    #print(str(row[0]))
                    #webscrap_mov(row)







    else:
        print("Oh, a ocurrido un error!")

while True:
    webscrap_mov()

    sleep(2)
