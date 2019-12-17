from __future__ import print_function
from django.core.management.base import BaseCommand, CommandError
from blog.models import MovPallets as MovPallets
from blog.models import UbicPallet as UbicPallet
from blog.models import Pallet as Pallet
import mechanicalsoup
import argparse
from getpass import getpass
from time import time, sleep

from datetime import datetime, timedelta
from time import time, sleep
import pyodbc
import sys

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)
        poll_id="hola"
    def handle(self, *args, **options):

        while True:
            try:

                #sleep(0.5)
                cursor= self.conecta_BD()
                sleep(0.5)
                #browser= self.inicia_browser()

                auxok=1
                while auxok==1:
                    auxok=self.webscrap_mov(cursor)#browser,cursor)
                    sleep(0.1)


            except Exception as e:
                print(e)
                print("Unexpected error:", sys.exc_info()[0])
                print("error en conexión a datos :( (a DB o a sitio web))")
                sleep(0.2)



    def conecta_BD(self):
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
            print("Unexpected error:", sys.exc_info()[0])
            print("error al conectar con DB :(")

    def inicia_browser(self):

            print("conectando a browser")
            browser = mechanicalsoup.StatefulBrowser(
                soup_config={'features': 'lxml'},
                raise_on_404=True,
                user_agent='MyBot/0.1: mysite.example.com/bot_info',
            )

            #Ojo que esto antes estaba en el webscrap_mov. Lo puse aquí para ver si funciona más rápido
            print("entrando a página")
            #browser.open("https://gogutier.pythonanywhere.com/carga_mov_pallets/")
            browser.open("http://127.0.0.1:8000/carga_mov_pallets/") #esto creo que ya no sirve
            #browser.open("http://192.168.7.32:8080/carga_mov_pallets/")

            return(browser)
            # Uncomment for a more verbose output:
            # browser.set_verbose(2)



    #print("hola")
    def webscrap_mov(self,cursor):#(self, browser, cursor):
        #acá trato de entrar a la página sin tener que iniciar el browser todo el tiempo.
        if 1:#try:
            #print("entrando a página")
            #browser.open("https://gogutier.pythonanywhere.com/carga_mov_pallets/")
            #browser.open("http://127.0.0.1:8000/carga_mov_pallets/")
            #browser.follow_link("login")
            #print(browser.get_current_page())
            ###browser.select_form()
            #browser.select_form('formMain')
            #print("obteniendo el transactionindex más nuevo..")
            ####page = browser.get_current_page()
            ####messages = page.find(id="ultimo")
            ultim=str(MovPallets.objects.all().order_by('-TRANSACTIONINDEX')[0].TRANSACTIONINDEX)
            print("útlimo TrIndex:"+ ultim)


            row, datosextra=self.cargaDatos(ultim,cursor)#Acá es donde ejecuto la odbc
            #print(row)
            if (row!=None and len(row)>0):

                '''
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
                '''
                ###ESTO Es lo que antes pasaba en el views.py cuando se submiteaba un nuevo pallet.
                dato0=str(row[0])#args.username#form.cleaned_data["TRANSACTIONINDEX"]
                dato1=str(row[1])#args.username#form.cleaned_data["PLANTID"]
                dato2=str(row[2])#form.cleaned_data["WAREHOUSE"]
                dato3=str(row[3])#form.cleaned_data["INTERNALSPECID"]
                dato4=str(row[4])#form.cleaned_data["ORDERID"]
                dato5=str(row[5])#form.cleaned_data["PARTID"]
                dato6=str(row[6])#form.cleaned_data["OPERATIONNO"]
                dato7=str(row[7])#form.cleaned_data["UNITTYPE"]
                dato8=str(row[8])#form.cleaned_data["LOADID"]
                dato9=str(row[9])#form.cleaned_data["UNITNO"]
                dato10=str(row[10])#form.cleaned_data["SOURCE"]
                dato11=str(row[11])#form.cleaned_data["DESTINATION"]
                dato12=(row[12])#form.cleaned_data["EVENTDATETIME"]
                #Acá proceso el dato12 para pasarlo a datetime y poder guardarlo en el modelo.
                dato13=str(row[13])#form.cleaned_data["EVENTTIME"]
                datounidadespallet=datosextra[0]#form.cleaned_data["unidadespallet"]
                datokgpallet=datosextra[1]#form.cleaned_data["kgpallet"]
                datom2pallet=datosextra[2]#form.cleaned_data["m2pallet"]
                datoalto=datosextra[3]#form.cleaned_data["alto"]
                datoancho=datosextra[4]#form.cleaned_data["ancho"]
                datokguni=datosextra[5]#form.cleaned_data["kguni"]
                datom2uni=datosextra[6]#form.cleaned_data["m2uni"]
                datoFGLoad=datosextra[7]#form.cleaned_data["esFGLoad"]
                datocliente=datosextra[8]#form.cleaned_data["esFGLoad"]
                datofechacreacionpallet=datosextra[9]#form.cleaned_data["esFGLoad"]
                datomaqruta=datosextra[10]#form.cleaned_data["esFGLoad"]

                #Ojo aquí si cambia algún dato en un transactionindex lo va a duplicar?
                o, created = MovPallets.objects.get_or_create(TRANSACTIONINDEX=dato0)
                o.PLANTID=dato1
                o.WAREHOUSE=dato2
                o.INTERNALSPECID=dato3
                o.ORDERID=dato4
                o.PARTID=dato5
                o.OPERATIONNO=dato6
                o.UNITTYPE=dato7
                o.LOADID=dato8
                o.UNITNO=dato9
                o.SOURCE=dato10
                o.DESTINATION=dato11
                o.EVENTDATETIME=dato12
                o.EVENTTIME=dato13
                o.unidadespallet=datounidadespallet
                o.kgpallet=datokgpallet
                o.m2pallet=datom2pallet
                o.alto=datoalto
                o.ancho=datoancho
                o.kguni=datokguni
                o.m2uni=datom2uni
                o.esFGLoad=datoFGLoad

                o.save()
                sleep(0.05)

                #creo la ubicación de inventario en caso de que no exista.
                a, created = UbicPallet.objects.get_or_create(calle=dato11)
                a.save()
                sleep(0.05)

                #creo el pallet en caso de que no exista. Si ya existe le actualizo la ubicación.

                c, created = Pallet.objects.get_or_create(tarja=dato8)
                c.padron=dato3
                c.ubic=dato11
                c.ORDERID=dato4
                #c.ubic2=UbicPallet.objects.filter(calle=dato11)[0]
                ##Esto lo borro para ver si ahora revisa la fecha de creación cada vez que se mueve un pallet#### if datoFGLoad==1: #Aquí hay que arreglar el caso en que se mueve un pallet que todavía no está creado*ya está considerado, usa la fecha now() por defecto
                c.fechacreac=datofechacreacionpallet
                c.ancho=datoancho
                c.alto=datoalto
                c.unidades=datounidadespallet
                c.cliente=datocliente
                c.maqruta=datomaqruta
                c.m2uni=datom2uni
                c.kguni=datokguni
                c.m2pallet=datom2pallet
                c.kgpallet=datokgpallet
                c.save()
                sleep(0.06)

                #form = MovPalletForm()#Esto se pone si quieres que después de submitear, los valores que pusiste en los form se borren

                #form = MovPalletForm()


            #return redirect ('res_inventario')









            resultado="dato enviado"
            print("Dato guardado")
            return(1)

        else:#except Exception as e:
            print(e)
            print("Unexpected error:", sys.exc_info()[0])
            print("Desconectado de página o no hay movimientos nuevos qué capturar")
            sleep(10)
            return(0)





    def cargaDatos(self, ultimo, cursor):
        print("cargo datos de pallets que se han movido en BPT")
        print("conectándose a DB para encontrar el transactionindex siguiente a " + str(ultimo))


        flag0=0

        if flag0==0: #si es un dato que saco de la MVLOAD..

            operation=0

            destinobpt=('PLL','PT10','AN1','AN2','AN3','AN4','AN5','AN6','AN7','AN8','AN9','B01','B02','B03')
            destinotxt=""
            for dest in destinobpt:
                destinotxt+= "Destination='"+ dest +"'"+ " or "

            try:
                print("obteniendo el row1 del MVLOAD")
                #sleep(0.01)


                cursor.execute("SELECT TOP (1) [TRANSACTIONINDEX], [PLANTID] ,[WAREHOUSE],[INTERNALSPECID], [ORDERID], [PARTID], [OPERATIONNO], [UNITTYPE], [LOADID], [UNITNO],[SOURCE],[DESTINATION],[EVENTDATETIME],[EVENTTIME]  FROM [ctidb_transact].[dbo].[MVLOAD] where TRANSACTIONINDEX>'"+ str(ultimo) +"' AND ("+ destinotxt +"Destination='xassxsa') order by transactionindex asc ")

                #Aquí hay que ponerle un TRY probablemente
                try:
                    row1=cursor.fetchone()

                    print(row1[0])
                    operation=row1[6]
                    print("Obtenida row1 de MVLOAD!")

                except:
                    print("error al hacer row1=cursor.fetchone()")
                #print(row1)
                #compara el transactionidex de fgload vs el de MVLOAD

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
        try:

            print("Tarja: "+row1[8])
            tarjax=row1[8]
            orderidx=row1[4]
            #id=row1[4]

            print ("iniciando segunda consulta")
            #sleep(0.01)
            print("saco el FGLOAD de esa Tarja")
            cursor.execute("SELECT TOP (1) [TRANSACTIONINDEX], [WORKCENTERID], [ORDERID], [LOADID], [UNITNO], [TOTALLOADQTY], [STACKCOUNT], [LOADSIZE], [REPRINTINDICATOR], [INTERNALSPECID] FROM [ctidb_transact].[dbo].[FGLOAD] where loadid= '"+ str(tarjax) +"' order by TRANSACTIONINDEX desc")
            print("segunda consulta satisfactoria")
            #De aquí quiero el número de unidades
            #tomo el valor de ese transactionindex para obtener el número de unidades por pallet
            #for row in cursor:
            #    print(row)
            row2=cursor.fetchone()
            if row2:
                print(row2)
                unidadespallet=row2[5]
            else:
                print("No se encontraron tarjas en FGLOAD para la loadID " + str(trajax) )
                unidadespallet=500

            print("Saco la fecha de creación de ese pallet. (EL FGLOAD más antguo que tenga ese pallet)")
            cursor.execute("SELECT TOP (1) [TRANSACTIONINDEX], [ORDERID], [LOADID], [EventDateTime] FROM [ctidb_transact].[dbo].[FGLOAD] where loadid= '"+ str(tarjax) +"' order by TRANSACTIONINDEX asc")
            row2B=cursor.fetchone()
            if row2B:
                print(row2B)
                fechacreacionpallet=row2B[3]
                print("fecha de creacióm obtenida!")
            else:
                print("No se encontraron tarjas en FGLOAD para la loadID " + str(row1[8]) )
                fechacreacionpallet=datetime.now()
            #print("unidades pallet")

            print("Obtengo el cliente en la tabla ORDERS_INFO para el ID: " + str(orderidx))
            cursor.execute("SELECT TOP (1) [TRANSACTIONINDEX] ,[ORDERID],[INTERNALSPECID],[CUSTOMERNAME] FROM [ctidb_transact].[dbo].[ORDERS_INFO]  where ORDERID ='"+ str(orderidx) +"' order by TRANSACTIONINDEX desc")#**** Si aquí le pongo el DESC mejora? creo que si (lo cambié en el local pero no en el servidor productivo)

            TI_Orders_Info=1000
            row2C=cursor.fetchone()
            if row2C:

                cliente=row2C[3]
                print("cliente obtenido!")
                print(row2C[3])
                TI_Orders_Info=row2C[0]

            else:
                print("No se encontraron tarjas en CONVERTIONOPINFO para la orderid " + str(orderidx) )
                cliente="vacío"

            if row2C:
                print("Obtengo la máquina en ruta de tabla ORDERS_INFO para el Transactionindex: " + str(TI_Orders_Info))
                cursor.execute("SELECT TOP (1) [TRANSACTIONINDEX],[WORKCENTERID],[ROUTINGNO],[OPERATIONNO],[NUMBEROUT],[NUMBERIN] FROM [ctidb_transact].[dbo].[CONVERTINGOPINFO] where Transactionindex='"+ str(TI_Orders_Info) +"' order by TRANSACTIONINDEX desc")

                row2D=cursor.fetchone()
                if row2D:

                    maqruta=row2D[1]
                    print("maqruta obtenido!")
                    print(row2D[1])

                else:
                    print("No se encontraron tarjas en ORDERS_INFO para el Transactionindex " + str(TI_Orders_Info) )
                    maqruta="vacío"
            else:
                maqruta="vacío"
                #print("unidades pallet")
                #print("unidades pallet")
                #print(unidadespallet)


            #acá saco las dimensiones del pallet según el útimo specID subido para ese padrón###
            # Ojo! Esto lo uso para sacar el transaction index inicial con el que se alimentó la orden a EFI, con eso saco las dimensiones de placa de la siguiente consulta. Éstas dimensiones son de la caja.
            print("iniciando tercera consulta por el padron " + str(row1[3]) )
            #sleep(0.01)

            if (str(row1[3])!="Default"):
                print("el Padron "+str(row1[3]) +" no es Default")
                cursor.execute( "SELECT TOP (1) [TRANSACTIONINDEX],[INTERNALSPECID],[PARTID],[ITEMWIDTH],[ITEMLENGTH],[ITEMDEPTH] FROM [ctidb_transact].[dbo].[SPECS_INFO] where InternalspecID = '"+ str(row1[3]) + "' order by transactionindex desc")
                row3=cursor.fetchone()
                transaction=row3[0]

                print("transaction: " + str(transaction))
                #print(transaction)

                print("inciando cuarta consulta")
                #sleep(0.01)
                try:
                    #OJOOOOO, aquí tengo que asegurarme de consultar el ancho y alto de la CAJA en caso de que el operationno sea distinto de cero.
                    if operation==0:
                        print("operation number es 0 placas")
                        cursor.execute("SELECT TOP (1) [TRANSACTIONINDEX], [BLANKWIDTH],[BLANKLENGTH] FROM [ctidb_transact].[dbo].[CORRUGATOROPINFO] where transactionindex= '"+ str(transaction) +"'order by transactionindex desc")
                        row4=cursor.fetchone()
                        #Ahora busco las medidas: de ese padrón (asociada a la última orden que tenga el padrón nomás.)
                        ancho=row4[1]
                        alto=row4[2]
                        pesouni=0
                    else:
                        print("operation number es mayor a cero (cajas)")

                        ancho=int(row3[3])/1000
                        alto=int(row3[4])/1000
                        pesouni=0
                except:
                    ancho=0
                    alto=0
                    pesouni=0

            else:
                print("el ID sí es default")
                row4=[0,0,0,0]
                ancho=0
                alto=0
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
            flagFGLoad=0
            datosextra = [unidadespallet, kgpallet, m2pallet, alto, ancho, pesouni, m2uni, flagFGLoad, cliente, fechacreacionpallet, maqruta]
            print("obtención de último movimiento actualizada")
            print(str(row1[0])+" "+str(row1[4])+" "+str(row1[12]) + " de " + str(row1[10])+ " a " + str(row1[11]))
        except Exception as e:
            print(e)
            print("error al tomar rows!")
            print("Unexpected error:", sys.exc_info()[0])
            #print("Unexpected error:", sys.exc_info()[0])
            sleep(1)
            row1=[]
            datosextra=[]
        return(row1, datosextra)
