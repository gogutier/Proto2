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
                sleep(2)



    def conecta_BD(self):
        try:
            print("Iniciando conexión a BD")
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
            sleep(2)


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
            print("fecha último: " + str(MovPallets.objects.all().order_by('-TRANSACTIONINDEX')[0].EVENTDATETIME))

            respuesta=self.cargaDatos(ultim,cursor)#Acá es donde ejecuto la odbc

            for resp in respuesta:
                print("Respuesta encontrada:")
                print(resp[0])
                row=resp[0]
                datosextra=resp[1]

                #print(row)
                if (row!=None and len(row)>0):


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
                    dato10=str(row[10].upper())#form.cleaned_data["SOURCE"]
                    dato11=str(row[11].upper())#form.cleaned_data["DESTINATION"]
                    dato12=(row[12])#form.cleaned_data["EVENTDATETIME"]
                    #Acá proceso el dato12 para pasarlo a datetime y poder guardarlo en el modelo.
                    dato13=str(row[13])#form.cleaned_data["EVENTTIME"]
                    dato14=str(row[14])
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
                    o, created = MovPallets.objects.get_or_create(TRANSACTIONINDEX=dato0, LOADID=dato8)
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
                    o.OPERATORCODENAME=dato14
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
                    a, created = UbicPallet.objects.get_or_create(calle=dato11.upper())
                    a.save()
                    sleep(0.05)

                    #creo el pallet en caso de que no exista. Si ya existe le actualizo la ubicación.

                    c, created = Pallet.objects.get_or_create(tarja=dato8)
                    c.padron=dato3
                    c.ubic=dato11.upper()
                    c.ORDERID=dato4
                    #c.ubic2=UbicPallet.objects.filter(calle=dato11)[0]
                    ##Esto lo borro para ver si ahora revisa la fecha de creación cada vez que se mueve un pallet#### if datoFGLoad==1: #Aquí hay que arreglar el caso en que se mueve un pallet que todavía no está creado*ya está considerado, usa la fecha now() por defecto
                    c.fechacreac=datofechacreacionpallet

                    c.fechaultmov=dato12

                    if dato11=='PLL':
                        c.flagpll=True
                        c.fechapll=dato12
                    if dato11.upper()=='TRUCK':
                        c.flagcamion=True
                        c.fechacamion=dato12

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

                resultado="datos enviados"
                print("Datos guardados")
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


        flag0=9 #0 si voy a sacar el dato de MVLOAD o 1 si lo voy a sacar del Bill of Lading.
        respuesta=[]

        destinobpt=('PLL','PT10','AN1','AN2','AN3','AN4','AN5','AN6','AN7','AN8','AN9','B01','B02','B03','B04','B05','B06','B07','B08','B09','B10','B11','B12','B13','B14','B15','B16','C01','C02','C03','C04','C05','C06','C07','C08','C09','C10','C11','C12','C13','C14','C15','A01','A02','A03','A04','A05','A06','A07','A08','E01','E02','E03','E04','PA1','PA2','PA3', 'PTCAL','RP1','Truck', 'D01')
        destinotxt=""
        for dest in destinobpt:
            destinotxt+= "Destination='"+ dest +"'"+ " or "


        #Acá decido si voy a sacar el próximo transactionindex del MVLOAD o del BILLOFLADING.
        trmvload=99999999
        trbol=99999999
        #Obtengo el transactionindex del candidato de MVLOAD
        cursor.execute("SELECT TOP (1) [TRANSACTIONINDEX], [PLANTID] ,[WAREHOUSE],[INTERNALSPECID], [ORDERID], [PARTID], [OPERATIONNO], [UNITTYPE], [LOADID], [UNITNO],[SOURCE],[DESTINATION],[EVENTDATETIME],[EVENTTIME],[OPERATORCODENAME]  FROM [ctidb_transact].[dbo].[MVLOAD] where TRANSACTIONINDEX>'"+ str(ultimo) +"' AND ("+ destinotxt +"Destination='xassxsa') order by transactionindex asc ")
        try:
            row=cursor.fetchone()
            trmvload=int(row[0])
        except:
            trmvload=99999999

        #Obtengo el transactionindex del Billoflading
        cursor.execute("SELECT TOP (1) [TRANSACTIONINDEX],[ORDERID],[PARTID],[UNITID],[UNITQTY],[LOCATION] FROM [ctidb_transact].[dbo].[BILLOFLADINGLOAD] where TRANSACTIONINDEX>'"+ str(ultimo) +"' order by transactionindex asc")
        try:
            row=cursor.fetchone()
            trbol=int(row[0])
        except:
            trbol=99999999

        print("comparando "+ str(trmvload) + " y " + str(trbol) )

        if trmvload<99999999 or trbol<99999999:
            if trmvload<trbol:
                flag0=0
                print("el dato se sacará del MVLOAD")
            else:
                flag0=1
                print("el dato se sacará del BILLOFLADING")
        else:
            print("no se encontraron transacciones mayores ni en MVLOAD ni en BILLOFLADING")


        if flag0==0: #si es un dato que saco de la MVLOAD..

            print("el dato se sacará del MVLOAD")

            operation=0



            rowcount=0

            print("obteniendo el row1 del MVLOAD")
            #sleep(0.01)



            cursor.execute("SELECT TOP (1) [TRANSACTIONINDEX], [PLANTID] ,[WAREHOUSE],[INTERNALSPECID], [ORDERID], [PARTID], [OPERATIONNO], [UNITTYPE], [LOADID], [UNITNO],[SOURCE],[DESTINATION],[EVENTDATETIME],[EVENTTIME],[OPERATORCODENAME]  FROM [ctidb_transact].[dbo].[MVLOAD] where TRANSACTIONINDEX>'"+ str(ultimo) +"' AND ("+ destinotxt +"Destination='xassxsa') order by transactionindex asc ")


            #Aquí hay que ponerle un TRY probablemente
            row1=[]
            if len(cursor.fetchall())>0:
                try:
                    cursor.execute("SELECT TOP (1) [TRANSACTIONINDEX], [PLANTID] ,[WAREHOUSE],[INTERNALSPECID], [ORDERID], [PARTID], [OPERATIONNO], [UNITTYPE], [LOADID], [UNITNO],[SOURCE],[DESTINATION],[EVENTDATETIME],[EVENTTIME],[OPERATORCODENAME]  FROM [ctidb_transact].[dbo].[MVLOAD] where TRANSACTIONINDEX>'"+ str(ultimo) +"' AND ("+ destinotxt +"Destination='xassxsa') order by transactionindex asc ")

                    row1=cursor.fetchone()
                    print(row1[0])
                    operation=row1[6]
                    print("Obtenida row1 de MVLOAD!")
                except Exception as e:
                    print("error! :")
                    print(e)
                    print("Unexpected error:", sys.exc_info()[0])
                    print("error al hacer row1=cursor.fetchone()")


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
                    print("No se encontraron tarjas en FGLOAD para la loadID " + str(tarjax) )
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
                numberout=1
                if (str(row1[3])!="Default"):
                    print("el Padron "+str(row1[3]) +" no es Default")
                    cursor.execute( "SELECT TOP (1) [TRANSACTIONINDEX],[INTERNALSPECID],[PARTID],[ITEMWIDTH],[ITEMLENGTH],[ITEMDEPTH],[NUMBERIN],[NUMBEROUT] FROM [ctidb_transact].[dbo].[SPECS_INFO] where InternalspecID = '"+ str(row1[3]) + "' order by transactionindex desc")
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
                            cursor.execute("SELECT TOP (1) [TRANSACTIONINDEX],[INPUTWIDTH],[INPUTLENGTH],[NUMBEROUT],[NUMBERIN] FROM [ctidb_transact].[dbo].[CONVERTINGOPINFO] where transactionindex= '"+ str(transaction) +"'order by transactionindex desc")
                            row4=cursor.fetchone()
                            pesouni=0
                            ancho=row4[1]
                            alto=row4[2]
                            numberout=row4[3]
                            if numberout<=0:
                                numberout=1
                    except Exception as e:
                        print(e)
                        print("error al tomar ancho y alto y nomberout!")
                        print("Unexpected error:", sys.exc_info()[0])
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

                m2uni=ancho*alto/numberout
                m2pallet=m2uni*unidadespallet
                pesouni=0
                print("m2pallet")
                print(m2pallet)
                print("ancho")
                print(ancho)
                print("alto")
                print(alto)
                print("unidades")
                print(unidadespallet)
                #print("pesouni")
                #print(pesouni)
                #print("m2uni")
                #print(m2uni)
                flagFGLoad=0
                datosextra = [unidadespallet, kgpallet, m2pallet, alto, ancho, pesouni, m2uni, flagFGLoad, cliente, fechacreacionpallet, maqruta]
                print("obtención de último movimiento actualizado")
                print(str(row1[0])+" "+str(row1[4])+" "+str(row1[12]) + " de " + str(row1[10])+ " a " + str(row1[11]))
                print(" ")
                respuesta.append([row1,datosextra])



            else:
                print("row1 igual a cero!")
                row1=[]
                datosextra=[]
                respuesta.append([row1,datosextra])


        elif flag0==1:
            print("sacando dato del BILLOFLADING")
            cursor.execute("SELECT TOP (1000) [TRANSACTIONINDEX],[ORDERID],[PARTID],[UNITID],[UNITQTY],[LOCATION] FROM [ctidb_transact].[dbo].[BILLOFLADINGLOAD] where TRANSACTIONINDEX='"+ str(trbol) +"' order by transactionindex desc")
            row1bol=cursor.fetchall()
            print("dato extraido correctamente")
            #print(row1bol)
            respuesta=[]
            for row in row1bol:
                #print(row[0])
                # row1= [TRANSACTIONINDEX], [PLANTID] ,[WAREHOUSE],[INTERNALSPECID], [ORDERID], [PARTID], [OPERATIONNO], [UNITTYPE], [LOADID], [UNITNO],[SOURCE],[DESTINATION],[EVENTDATETIME],[EVENTTIME],[OPERATORCODENAME]
                print("saco 1 dato del billofladinginfo, que tenga el transactionindex y la misma orderid")
                cursor.execute("SELECT TOP (1) [TRANSACTIONINDEX],[BILLOFLADINGID],[SHIPDATETIME],[ORDERID],[SPECID],[TRAILERID] FROM [ctidb_transact].[dbo].[BILLOFLADINGINFO] where transactionindex='"+ str(trbol) +"' and orderid= '"+ str(row[1]) +"' order by transactionindex desc")
                rowaux=cursor.fetchone()
                #print("obtengo el padrón de esa tarja:")

                row1 =[ row[0],'800','wharehouse',rowaux[4], row[1], row[2],"1","UNITType",row[3],row[4],"vacio",row[5].upper(),rowaux[2],0,rowaux[5]]

                #print("ahora saco los datosextra asociados.")

                #print("supuesto: todo pallet que se cargará a camión ya fue creado anteriormente y está en la BD de django control.corrupac:8090")
                #datosextra = [unidadespallet, kgpallet, m2pallet, alto, ancho, pesouni, m2uni, flagFGLoad, cliente, fechacreacionpallet, maqruta]#
                print(str(row[3])+" "+str(row[1]))

                try:
                    c= Pallet.objects.get(tarja=str(row[3]))

                #    print("pallet encontrado")
                    datosextra = [c.unidades, c.kgpallet, c.m2pallet, c.alto, c.ancho, c.kguni, c.m2uni, 0, c.cliente, c.fechacreac, c.maqruta]
                    print("obtención de último movimiento actualizado")
                    print(str(row1[0])+" "+str(row1[4])+" "+str(row1[12]) + " de " + str(row1[10])+ " a " + str(row1[11]))
                    print(" ")
                except:
                    c= Pallet.objects.get_or_create(tarja=str(row[3]))
                    print("Error, pallet cargado a camión no pasó por registros efi previamente (cargaron un pallet muy antiguo por secretaría?)")
                    sleep(5)
                respuesta.append([row1,datosextra])

            return(respuesta)
            #por cada fila en el row le creo un row1 y un datoextra:

            #por cada transacción guardad en row1bol, debo generar un movpallet equivalente en Django", después mandarlas django para q las guerde (van a tener transactionindex repetidos).

        else:
            row1=[]
            datosextra=[]
            respuesta.append([row1,datosextra])

        return(respuesta)
