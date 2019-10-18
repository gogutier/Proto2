from __future__ import print_function
import mechanicalsoup
import argparse
from getpass import getpass
from time import time, sleep
from datetime import datetime
import pyodbc
import sys


def conecta_BD():
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=192.168.8.41;'
                              'UID=cti;'
                              'PWD=ctidb;'
                              'Database=ctidb_transact;')
                              #'Trusted_Connection=yes;')
                              #DSN=QadNet;UID=CGCOM;HOST=192.168.8.7;PORT=7120;DB=cstprod;

        cursor = conn.cursor()
        print("Conectado a DB :D")
        return(cursor)

    except Exception as e:
        print(e)
        print("error al conectar con DB :(")

def inicia_browser():

        print("conectando a browser")
        browser = mechanicalsoup.StatefulBrowser(
            soup_config={'features': 'lxml'},
            raise_on_404=True,
            user_agent='MyBot/0.1: mysite.example.com/bot_info',
        )

        #Ojo que esto antes estaba en el webscrap_mov. Lo puse aquí para ver si funciona más rápido
        print("entrando a página")
        browser.open("https://gogutier.pythonanywhere.com/carga_mov_pallets/")
        #browser.open("http://127.0.0.1:8000/carga_mov_pallets/")

        return(browser)
        # Uncomment for a more verbose output:
        # browser.set_verbose(2)



#print("hola")
def webscrap_mov(browser, cursor):
    #acá trato de entrar a la página sin tener que iniciar el browser todo el tiempo.
    if 1:

        #print("entrando a página")
        #browser.open("https://gogutier.pythonanywhere.com/carga_mov_pallets/")


        #browser.open("http://127.0.0.1:8000/carga_mov_pallets/")
        #browser.follow_link("login")
        #print(browser.get_current_page())
        browser.select_form()
        #browser.select_form('formMain')
        #print("obteniendo el transactionindex más nuevo..")
        page = browser.get_current_page()
        messages = page.find(id="ultimo")
        print("útlimo:"+ messages.text)
        row, datosextra=cargaDatos(messages.text,cursor)#Acá es donde ejecuto la odbc
        #print(row)
        if (row!=None and len(row)>0):
            #print("escribiendo datos de transacción en página")
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
            browser["esFGLoad"] = datosextra[7]


        ##browser["password"] = "plant"#args.password
            #print("submiteando")
            resp = browser.submit_selected()
                # Uncomment to launch a web browser on the current page:
            #browser.launch_browser()
                #print(browser.open("http://interlink.corrupac.cl"))
                #>>> browser.follow_link("forms") #sigue el link que tenga la palabra indicada
            #<Response [200]>
            #>>> browser.get_url()
        resultado="dato enviado"
        return(resultado)

    else: #except Exception as e:
        #print(e)
        #print("Desconectado de página :(")
        sleep(0.2)





def cargaDatos(ultimo, cursor):
    #print("conectándose a DB..")



    flagFGLoad=0
    #print("iniciando consulta")
    #print("supuesto: tabla MVLOAD y FGLOAD no comparten transactionindexes")
    #consulto los datos del último pallet que se movió menor al máximo transactionindex
    # Tb filtro por sólos los que son pallets de corrugado = OPERATIONNO = 0
    #Primero reviso si hay transactioninxes mayores a "ultimo" en la tabla FGLOAD. Si hay, simulo un movimiento de MVload a la ubicación #CORR_UPPER_Stacker o CORR_LOWER_Stacker.
    #OJOO: Primero tengo que comparar cuál es el transaction ID más próximo al actual "último" que aparecen en el MVLOAD y el FGLOAD, después quedarme con el menor entre esos 2.
    flag0=0
    #sleep(0.01)
    cursor.execute("SELECT TOP (1) [TRANSACTIONINDEX],[PLANTID],[WORKCENTERID],[INTERNALSPECID],[ORDERID],[PARTID],[OPERATIONNO],[LOADID],[UNITNO],[TOTALLOADQTY],[EventDateTime],[EVENTTIME],[STEPNO],[WASTEDQUANTITY] FROM [ctidb_transact].[dbo].[FGLOAD] where operationno=0 and TRANSACTIONINDEX>"+ ultimo +"  order by transactionindex asc")
    row0=cursor.fetchone()
    #print("row0 FGLOAD:")
    #print(row0)
    if row0!=None:
        try:
            row0datetime=row0[10][:11]

            row0time=row0[11]
            #print(row0datetime)
            #print(row0time)
            row0datetime= row0datetime + row0time[0] + row0time[1] + ":" + row0time[2] + row0time[3] + ":" + row0time[4]+ row0time[5]
            row0datetime= datetime.strptime(row0datetime, '%d-%m-%Y %H:%M:%S')
        except:
            row0datetime=datetime.now()
            row0time='0'
        #print(row0datetime)
        workcenter=row0[2]
        destino=""
        if workcenter=="CORR_U":
            destino="CORR_UPPER_Stacker"
        elif workcenter=="CORR_L":
            destino="CORR_LOWER_Stacker"
        else:
            destino="ZPICADO"



        row1=[row0[0], row0[1], "0", row0[3], row0[4], row0[5], row0[6], 0, row0[7], row0[8], "CORR" , destino, row0datetime, row0[11]]
        #sleep(0.01)
        cursor.execute("SELECT TOP (1) [TRANSACTIONINDEX], [PLANTID] ,[WAREHOUSE],[INTERNALSPECID], [ORDERID], [PARTID], [OPERATIONNO], [UNITTYPE], [LOADID], [UNITNO],[SOURCE],[DESTINATION],[EVENTDATETIME],[EVENTTIME]  FROM [ctidb_transact].[dbo].[MVLOAD] where TRANSACTIONINDEX>"+ ultimo +" AND DESTINATION <> 'PLL' AND DESTINATION <> 'XTCY' AND DESTINATION <> 'XFFG' AND DESTINATION <> 'XFFW' AND DESTINATION <> 'XDRO' AND DESTINATION <> 'XHCR' AND DESTINATION <> 'XWRD' AND OPERATIONNO = 0 order by transactionindex asc ")



        try:
            rowaux=cursor.fetchone()
        except:
            print("error al hacer rowaux=cursor.fetchone()")
        #print(rowaux)

        TIFGLOAD=0
        TIMVLOAD=0


        TIFGLOAD=row0[0]
        if rowaux!= None:
            TIMVLOAD=rowaux[0]
        else:
            TIMVLOAD=999999999999

        if row0[3] != "Default":
            if TIFGLOAD<TIMVLOAD:
                flag0=1
                flagFGLoad=1
                #print("obtenida row1 de FGLOAD!")
                #print(row1)
        else:
            flag0=0



    if flag0==0:
        try:
            #print("obteniendo el row1 del MVLOAD")
            #sleep(0.01)
            cursor.execute("SELECT TOP (1) [TRANSACTIONINDEX], [PLANTID] ,[WAREHOUSE],[INTERNALSPECID], [ORDERID], [PARTID], [OPERATIONNO], [UNITTYPE], [LOADID], [UNITNO],[SOURCE],[DESTINATION],[EVENTDATETIME],[EVENTTIME]  FROM [ctidb_transact].[dbo].[MVLOAD] where TRANSACTIONINDEX>"+ ultimo +" AND DESTINATION <> 'PLL' AND DESTINATION <> 'XTCY' AND DESTINATION <> 'XFFG' AND DESTINATION <> 'XFFW' AND DESTINATION <> 'XDRO' AND DESTINATION <> 'XHCR' AND DESTINATION <> 'XWRD' AND OPERATIONNO = 0 order by transactionindex asc ")
            #Aquí hay que ponerle un TRY probablemente
            try:
                row1=cursor.fetchone()
            except:
                print("error al hacer row1=cursor.fetchone()")
            #print(row1)
            #compara el transactionidex de fgload vs el de MVLOAD
            #print("Obtenida row1 de MVLOAD!")
            #print(row1)
        except Exception as e:
            print(e)
            print("error!")
            print("Unexpected error:", sys.exc_info()[0])
            sleep(1)
            row1=[]
            datosextra=[]



    #print("consulta exitosa")
    #print(cursor[0])
    #return(cursor[0])
    if 1:

        #print("Tarja:")
        #print(row1[8])
        #id=row1[4]

        #print ("iniciando segunda consulta")
        #sleep(0.01)
        cursor.execute("SELECT TOP (1) [TRANSACTIONINDEX], [WORKCENTERID], [ORDERID], [LOADID], [UNITNO], [TOTALLOADQTY], [STACKCOUNT], [LOADSIZE], [REPRINTINDICATOR], [INTERNALSPECID] FROM [ctidb_transact].[dbo].[FGLOAD] where loadid= '"+ str(row1[8]) +"' order by TRANSACTIONINDEX desc")
        #De aquí quiero el número de unidades
        #tomo el valor de ese transactionindex para obtener el número de unidades por pallet
        #for row in cursor:
        #    print(row)
        row2=cursor.fetchone()
        if row2:
            print(row2)
            unidadespallet=row2[5]
        else:
            print("No se encontraron tarjas en FGLOAD para la loadID " + str(row1[8]) )
            unidadespallet=500
        #print("unidades pallet")
        #print(unidadespallet)


        #acá saco las dimensiones del pallet según el útimo specID subido para ese padrón###
        # Ojo! Esto lo uso para sacar el transaction index inicial con el que se alimentó la orden a EFI, con eso saco las dimensiones de placa de la siguiente consulta. Éstas dimensiones son de la caja.
        #print("iniciando tercera consulta por el id " + str(row1[3]) )
        #sleep(0.01)
        cursor.execute( "SELECT TOP (1) [TRANSACTIONINDEX],[INTERNALSPECID],[PARTID],[ITEMWIDTH],[ITEMLENGTH],[ITEMDEPTH] FROM [ctidb_transact].[dbo].[SPECS_INFO] where InternalspecID = '"+ str(row1[3]) + "' order by transactionindex desc")
        row3=cursor.fetchone()
        transaction=row3[0]
        #print("transaction")
        #print(transaction)

        #print("inciando cuarta consulta")
        #sleep(0.01)
        cursor.execute("SELECT TOP (1) [TRANSACTIONINDEX], [BLANKWIDTH],[BLANKLENGTH] FROM [ctidb_transact].[dbo].[CORRUGATOROPINFO] where transactionindex= '"+ str(transaction) +"'order by transactionindex desc")
        row4=cursor.fetchone()
        #Ahora busco las medidas: de ese padrón (asociada a la última orden que tenga el padrón nomás.)
        ancho=row4[1]
        alto=row4[2]
        pesouni=0

        kgpallet= pesouni* unidadespallet
        #print("tarja")
        #print(row1[8])
        #print("ID")
        #print(id)
        #print("kgpallet")
        #print(kgpallet)

        m2uni=ancho*alto
        m2pallet= m2uni*unidadespallet
        #print("m2pallet")
        #print(m2pallet)


        #print("ancho")
        #print(ancho)
        #print("alto")
        #print(alto)
        #print("unidades")
        #print(unidadespallet)
        #print("pesouni")
        #print(pesouni)
        #print("m2uni")
        #print(m2uni)
        datosextra = [unidadespallet, kgpallet, m2pallet, alto, ancho, pesouni, m2uni, flagFGLoad]
        print(str(row1[0])+" "+str(row1[4])+" "+str(row1[12]) + " " + str(row1[11]))
    else:#except Exception as e:
        #print(e)
        print("error al tomar row1!")
        #print("Unexpected error:", sys.exc_info()[0])
        sleep(1)
        row1=[]
        datosextra=[]
    return(row1, datosextra)





while True:
    try:

        sleep(0.5)
        cursor= conecta_BD()
        sleep(0.5)
        browser= inicia_browser()

    except Exception as e:
        print(e)
        print("error en conexión a datos :( (a DB o a sitio web))")
        sleep(0.2)
    if 1:
        while True:
            webscrap_mov(browser,cursor)

    else: #except Exception as e:
        #print(e)
        print("error consulta de datos :(")
        sleep(0.5)
