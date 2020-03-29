from django.core.management.base import BaseCommand, CommandError
from blog.models import OrdenCorrplan as OrdenCorrplan
from blog.models import FotoCorrplan as FotoCorrplan
from blog.models import FotoProgCorr as FotoProgCorr
from blog.models import FiltroEntradaWIP as FiltroEntradaWIP
from blog.models import FiltroSalidaWIP as FiltroSalidaWIP
from blog.models import FiltroMovInternoWIP as FiltroMovInternoWIP
from blog.models import Datos_Proy_WIP as Datos_Proy_WIP
from blog.models import DatosWIP_Prog as DatosWIP_Prog
#from blog.models import Datos_INV_WIP as Datos_INV_WIP
from blog.models import MovPallets as MovPallets
from blog.models import Datos_KPI_Semanal as Datos_KPI_Semanal
from blog.models import Datos_KPI_OPGRUA as Datos_KPI_OPGRUA
from blog.models import Datos_MovPallets as Datos_MovPallets
from blog.models import Datos_MovPallets_B as Datos_MovPallets_B
from blog.models import Datos_MovPallets_C as Datos_MovPallets_C
from blog.models import Foto_Datos_MovPallets as Foto_Datos_MovPallets
from blog.models import IDProgCorr as IDProgCorr
from blog.models import Pallet as Pallet
from blog.models import Cartones as Cartones
from blog.models import Maquinas as Maquinas
from blog.models import ConsumoRollos as ConsumoRollos
from blog.models import Foto_ConsumoRollos as Foto_ConsumoRollos
from blog.models import UbicPallet as UbicPallet
from blog.models import FiltroEntradaWIP as FiltroEntradaWIP
from blog.models import FiltroSalidaWIP as FiltroSalidaWIP
from blog.models import Foto_Datos_Inv_WIP as Foto_Datos_Inv_WIP
from blog.models import Datos_Inv_WIP as Datos_Inv_WIP

from django.db.models import Q
import webscrap3
import pruebaodbcconvertprod

from django.utils import timezone
from datetime import datetime, timedelta
from time import time, sleep







class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)
        poll_id="hola"

    def update_datos_wip(self):

        print("iniciando cálculo de inventario en WIP")
        datosWIP={
        "C01":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
        "C02":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
        "C03":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
        "C04":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
        "C05":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
        "C06":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
        "C07":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
        "C08":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
        "C09":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
        "C10":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
        "C11":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
        "C12":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
        "C13":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
        "B01":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
        "B02":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":13,"al3":44},
        "B03":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
        "B04":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
        "B05":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
        "B06":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
        "B07":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
        "B08":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
        "B09":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
        "B10":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
        "B11":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
        "B12":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
        "B13":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
        "B14":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
        "B15":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
        "E01":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
        "E02":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
        "E03":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
        "E04":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
        "A01":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
        "A02":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
        "A03":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
        "A04":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
        "A05":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
        "A06":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
        "A07":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
        "PLL":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":5,"al2":10,"al3":20},
        #"RP1":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":5,"al2":10,"al3":20},
        "PTCAL":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":5,"al2":10,"al3":20},
        "D01":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":5,"al2":10,"al3":20}
        }

        m2totalINV=0
        npalletstotalINV=0

        m2totalCORR=0
        npalletstotalCORR=0

        filtromovinternoqs=Q()

        for calle in datosWIP.keys():

            datosWIP[str(calle )]['cuenta']= Pallet.objects.filter(ubic__iexact=str(calle)).count()
            datosWIP[str(calle)]['indice']= UbicPallet.objects.get(calle__iexact=str(calle)).pk

            filtromovinternoqs = filtromovinternoqs | Q(DESTINATION=str(calle))

            try:
                datosWIP[str(calle)]['dias']= (datetime.now()-(Pallet.objects.filter(ubic__iexact=str(calle)).earliest('fechacreac').fechacreac.replace(tzinfo=None))).days#- datetime.now()))

            except Exception as e:
                print(e)
                datosWIP[str(calle)]['dias']=0
                print("error no se encontraron días de antiguedad en calle " + str(calle) )
                sleep(10)

            #print(str(calle))
            #print("fecha creación:")
            #print(datosWIP[str(calle)]['dias'])

            if (calle == "CORR_LOWER_Stacker" or calle == "CORR_UPPER_Stacker"):
                npalletstotalCORR=npalletstotalCORR+datosWIP[str(calle)]['cuenta']
            else:

                npalletstotalINV=npalletstotalINV+datosWIP[str(calle)]['cuenta']

            m2aux=0
            for pallet in Pallet.objects.filter(ubic__iexact=str(calle)):
                m2aux= m2aux+pallet.m2pallet
                if (calle == "CORR_LOWER_Stacker" or calle == "CORR_UPPER_Stacker"):
                    m2totalCORR=m2totalCORR+pallet.m2pallet
                else:

                    m2totalINV=m2totalINV+pallet.m2pallet

            datosWIP[str(calle)]['m2tot']=m2aux




        filtroentrada=[]
        filtro=MovPallets.objects.filter(Q(DESTINATION="PLL") | Q(DESTINATION="PT10")).exclude( Q(SOURCE="PLL") | Q(SOURCE="PT10")).order_by('-TRANSACTIONINDEX')[:3]

        # referencia: datetime.strptime(datoprocesado[1][colFecha], "%d-%m-%Y %H:%M")

        for mov in filtro:
            #movimiento=[tarja, destino, hora]
            movimiento=[mov.LOADID, mov.ORDERID, mov.SOURCE, mov.DESTINATION, mov.EVENTDATETIME.strftime("%d-%m-%y %H:%M:%S")]
            filtroentrada.append(movimiento)

        #print(filtroentrada)
        filtrosalida=[]
        filtro2=MovPallets.objects.filter(Q(DESTINATION="Truck") | Q(DESTINATION="AN1") | Q(DESTINATION="AN2")| Q(DESTINATION="AN3")| Q(DESTINATION="AN4")| Q(DESTINATION="AN5") | Q(DESTINATION="AN6")| Q(DESTINATION="AN7") | Q(DESTINATION="AN8")| Q(DESTINATION="AN9")| Q(DESTINATION="PTCAL")).order_by('-TRANSACTIONINDEX')[:3]

        for mov in filtro2:
            #movimiento=[tarja, destino, hora]
            movimiento=[mov.LOADID, mov.ORDERID, mov.SOURCE, mov.DESTINATION, mov.EVENTDATETIME.strftime("%d-%m-%y %H:%M:%S")]
            filtrosalida.append(movimiento)

        filtromovinterno=[]
        filtro3=MovPallets.objects.filter(filtromovinternoqs).exclude(DESTINATION="PLL").order_by('-TRANSACTIONINDEX')[:3]
        print("hola")
        for mov in filtro3:
            print("hola")
            movimiento=[mov.LOADID, mov.ORDERID, mov.SOURCE, mov.DESTINATION, mov.EVENTDATETIME.strftime("%d-%m-%y %H:%M:%S")]
            filtromovinterno.append(movimiento)


        print(filtroentrada)
        print(filtromovinterno)
        print(filtrosalida)

        print("Pasando objetos, creando una nueva foto de invetario: ")



        foto, created =Foto_Datos_Inv_WIP.objects.get_or_create(fecha_foto=datetime.now())
        foto.m2totalINV = m2totalINV
        foto.save()
        #Borrar los antiguos..

        #filtroentrada:

        for mov in filtroentrada:

            dato, created =FiltroEntradaWIP.objects.get_or_create(programa=foto, LOADID=mov[0], ORDERID=mov[1], SOURCE=mov[2], DESTINATION=mov[3], EVENTDATETIME=mov[4])
            dato.save()

        for mov in filtrosalida:

            dato, created =FiltroSalidaWIP.objects.get_or_create(programa=foto, LOADID=mov[0], ORDERID=mov[1], SOURCE=mov[2], DESTINATION=mov[3], EVENTDATETIME=mov[4])
            dato.save()

        for mov in filtromovinterno:

            dato, created =FiltroMovInternoWIP.objects.get_or_create(programa=foto, LOADID=mov[0], ORDERID=mov[1], SOURCE=mov[2], DESTINATION=mov[3], EVENTDATETIME=mov[4])
            dato.save()


        #sectores:
        for calle in datosWIP.keys():

            dato, created =Datos_Inv_WIP.objects.get_or_create(programa=foto, sector=str(calle), cuenta=datosWIP[str(calle)]['cuenta'], m2tot=datosWIP[str(calle)]['m2tot'], indice=datosWIP[str(calle)]['indice'], dias=datosWIP[str(calle)]['dias'], al1=datosWIP[str(calle)]['al1'], al2=datosWIP[str(calle)]['al2'], al3=datosWIP[str(calle)]['al3'])
            dato.save()

        print("borrando la foto de inventario anteior")
        instance=Foto_Datos_Inv_WIP.objects.filter(fecha_foto__lt=foto.fecha_foto)
        instance.delete()



        print("Enviando datos inventario")

    def updatekpisemanal(self):
        if 1:#########

            #CREO UNA nueva foto de movspallets:
            foto, created =Foto_Datos_MovPallets.objects.get_or_create(fecha_foto=datetime.now())
            foto.save()

            print("actualizo el Movpallets")

            try:

                #Rango de fechas últimas 4 semanas..

                print("Ahora voy a generar y guardar el resumen de los datos semanales..")

                semanahoy=datetime.now().isocalendar()[1] #Ojo que aquí la semana parte el domingo    Isocalendar entrga [ISO Year,ISO Week Number,ISO Weekday]
                añohoy=datetime.now().isocalendar()[0]
                print("número de semana de hoy: " + str( semanahoy ))


                #labels2.append({"fechaini":fechaini,"fechafin":fechafin, "label"
                lista=[ semanahoy-4, semanahoy-3, semanahoy-2, semanahoy-1, semanahoy]
                labels3=[]
                labels3.append({"hola":1,"dasd":1})
                indx=0

                for semana in lista:

                    #Creo el objeto semana
                    sem, aux= Datos_KPI_Semanal.objects.get_or_create(semana=semana, anno=añohoy)# esto en las primeras semanas de enero va a generar un problema
                    #calculo prodsem: suma de m2 / horas de la semana (24*5+15)
                    remis= Pallet.objects.filter(flagcamion=True, fechacamion__date__week=semana)
                    palletizados= Pallet.objects.filter(flagpll=True, fechapll__date__week=semana)
                    cont= remis.count()
                    sumadays=0
                    sumam2=0
                    sumapll=0


                    antiguedadsem=0
                    producsem=0
                    peakstock=0

                    for pll in palletizados:

                        sumapll+= pll.m2pallet


                    for rem in remis:
                        #print( str(rem.m2pallet) + " " + str(rem.fechacamion)+ " " + str(rem.fechapll) )
                        #print("semana: " + str(semana) + " " +  str( (rem.fechacamion-rem.fechapll).days ) + " " + str(rem.tarja) + " " + str(rem.ORDERID) )
                        sumadays+=max((rem.fechacamion-rem.fechapll).days,0)
                        sumam2+=rem.m2pallet

                    if cont==0:
                        cont=1
                    if sumapll==0:
                        sumapll=1

                    antiguedadsem=(sumadays/cont)#antiguedad promedio de cada pallet
                    producsem= (sumam2/1000)

                    peakstock=(sumam2/sumapll)*100

                    indx+=1
                    sem.productividad=producsem
                    sem.antiguedadstockdesp=antiguedadsem
                    sem.peakstock=peakstock


                    sem.save()

                    print(sem)
                    print(sem.productividad)
                    print(sem.antiguedadstockdesp)
                    print(sem.peakstock)
                    #ahora calculo los KPI de cada op grúa y los muestro asocio a esta sem

                    listaopgruabpt=["1091/PATRICIO FARIAS", "1092/ROBERTO QUILALEO","1083/WALDO  MOLINA", "1095/RICARDO PRADO","1093/JORGE SOTO", "1097/PEDRO MIRANDA", "1096/JORGE ARENAS", "1098/JONATHAN RIVEROS", "1099/SEBASTIAN PONCE", "1112/PETERSON RAIMOND", "1110/VICTOR CORTES", "1111/LUIS LOPEZ", "1090/RENE DONOSO","1193/Jose Salas","-","-","-"]
                    listafiltrosalida=["AN1","AN2","AN3","AN4","AN5","AN6","AN7","AN8","AN9"]
                    filtrosalidaqs=Q()
                    for item in listafiltrosalida:
                        filtrosalidaqs = filtrosalidaqs | Q(DESTINATION=item)



                    for op in listaopgruabpt:
                        opgrua, aux=Datos_KPI_OPGRUA.objects.get_or_create(semana=sem, codigoCTI=op)
                        m2semanal=0
                        npallets=0
                        movs= MovPallets.objects.filter(filtrosalidaqs, OPERATORCODENAME=op, EVENTDATETIME__date__week=semana)
                        for mov in movs:
                            m2semanal+= mov.m2pallet
                            npallets+=1

                        opgrua.m2Cargados=m2semanal
                        opgrua.palletsCargados=npallets

                        opgrua.save()
                        print(opgrua)
                        #calculo todos los m2 cargados por ese operador dentro de la semana.







            except Exception as e:
                print("error")
                print(e)
                sleep(10)




    def updatemovpallets(self):
        if 1:#########

            #CREO UNA nueva foto de movspallets:
            foto, created =Foto_Datos_MovPallets.objects.get_or_create(fecha_foto=datetime.now())
            foto.save()

            print("actualizo el Movpallets")

            try:

                #Rango de fechas últimas 4 semanas..

                print("Ahora voy a generar y guardar el resumen de los datos semanales..")

                semanahoy=datetime.now().isocalendar()[1] #Ojo que aquí la semana parte el domingo
                print("número de semana de hoy: " + str( semanahoy ))


                #labels2.append({"fechaini":fechaini,"fechafin":fechafin, "label"
                lista=[ semanahoy-4, semanahoy-3, semanahoy-2, semanahoy-1, semanahoy]
                labels3=[]
                labels3.append({"hola":1,"dasd":1})
                indx=0

                for semana in lista:

                    #calculo prodsem: suma de m2 / horas de la semana (24*5+15)
                    remis= Pallet.objects.filter(flagcamion=True, fechacamion__date__week=semana)
                    palletizados= Pallet.objects.filter(flagpll=True, fechapll__date__week=semana)
                    cont= remis.count()
                    sumadays=0
                    sumam2=0
                    sumapll=0


                    antiguedadsem=0
                    producsem=0
                    peakstock=0

                    for pll in palletizados:

                        sumapll+= pll.m2pallet


                    for rem in remis:
                        print( str(rem.m2pallet) + " " + str(rem.fechacamion)+ " " + str(rem.fechapll) )
                        print("semana: " + str(semana) + " " +  str( (rem.fechacamion-rem.fechapll).days ) + " " + str(rem.tarja) + " " + str(rem.ORDERID) )
                        sumadays+=max((rem.fechacamion-rem.fechapll).days,0)
                        sumam2+=rem.m2pallet

                    if cont==0:
                        cont=1
                    if sumapll==0:
                        sumapll=1
                    antiguedadsem=(sumadays/cont)
                    producsem= (sumam2/1000)

                    peakstock=(sumam2/sumapll)*100

                    indx+=1

                    print(producsem)
                    labels3.append({"indx": indx, "semana":semana, "producsem":producsem, "antiguedadsem": antiguedadsem, "peakstock":peakstock})




                o = Datos_MovPallets_C.objects.create(programa=foto, semana1=labels3[1]['semana'],producsem1=labels3[1]['producsem'],antiguedadsem1=labels3[1]['antiguedadsem'],peakstock1=labels3[1]['peakstock'], semana2=labels3[2]['semana'],producsem2=labels3[2]['producsem'],antiguedadsem2=labels3[2]['antiguedadsem'],peakstock2=labels3[2]['peakstock'], semana3=labels3[3]['semana'],producsem3=labels3[3]['producsem'],antiguedadsem3=labels3[3]['antiguedadsem'],peakstock3=labels3[3]['peakstock'], semana4=labels3[4]['semana'],producsem4=labels3[4]['producsem'],antiguedadsem4=labels3[4]['antiguedadsem'],peakstock4=labels3[4]['peakstock'], semana5=labels3[5]['semana'],producsem5=labels3[5]['producsem'],antiguedadsem5=labels3[5]['antiguedadsem'],peakstock5=labels3[5]['peakstock'])
                o.save()



                labels=[]
                ahora=datetime.now().replace(hour= 0, minute=0, second=0, microsecond=0)
                horizonte=7
                for i in range(0,horizonte):
                    #por ahora los voy a ordenar por turno, después por hora.
                    fecha=(ahora+timedelta(days=1)-timedelta(days=horizonte-i)).replace(hour= 7)
                    fechafin=(ahora+timedelta(days=1)-timedelta(days=horizonte-i)).replace(hour= 14, minute=30)
                    turno="A"
                    label= fecha.strftime("%d-%m") + " " + turno
                    #calculo el m2 real convertido y corrugado en ese turno, para comparar con las salidas y entradas declaradas
                    m2Conv, m2Corr= (0,0)#pruebaodbcconvertprod.consulta(fecha,fechafin)
                    #print(m2Corr)
                    labels.append({"fecha":fecha ,"fechafin":fechafin ,"turno":turno, "label": label, "m2Conv": m2Conv, "m2Corr": m2Corr})

                    fecha=(ahora+timedelta(days=1)-timedelta(days=horizonte-i)).replace(hour= 14, minute=30)
                    fechafin=(ahora+timedelta(days=1)-timedelta(days=horizonte-i)).replace(hour= 22)
                    turno="B"
                    label= fecha.strftime("%d-%m") + " " + turno
                    m2Conv, m2Corr= (0,0) #pruebaodbcconvertprod.consulta(fecha,fechafin)
                    #print(m2Corr)
                    labels.append({"fecha":fecha ,"fechafin":fechafin ,"turno":turno, "label": label, "m2Conv": m2Conv, "m2Corr": m2Corr})

                    fecha=(ahora+timedelta(days=1)-timedelta(days=horizonte-i)).replace(hour= 22)
                    fechafin=(ahora+timedelta(days=1)-timedelta(days=horizonte-i-1)).replace(hour= 7)
                    turno="C"
                    label= fecha.strftime("%d-%m") + " " + turno
                    m2Conv, m2Corr= (0,0)#pruebaodbcconvertprod.consulta(fecha,fechafin)
                    #print(m2Corr)
                    labels.append({"fecha":fecha ,"fechafin":fechafin ,"turno":turno, "label": label, "m2Conv": m2Conv, "m2Corr": m2Corr})

                print("ahora calculo las listas de lo que se declaró como ingreso y como salida al wip  ")


                #listafiltroproducido=["CORR_UPPER_Stacker", "CORR_LOWER_Stacker"]
                listafiltroentrada=["PLL","PT10"]#Acá el PT10 es pq supuestamente lasdevoluciones se iban a detectar por ahí.Ahora al pareer habría q sacarlas de la tabla FGRETURN
                listafiltrosalida=["AN1","AN2","AN3","AN4","AN5","AN6","AN7","AN8","AN9"]
                listafiltrosalida2=["Truck","TRUCK","truck"]
                listafiltrocallesbpt=["C01","C02","C03","C04","C05","C06","C07","C08","C09","C10","C11","C12","C13","B01","B02","B03","B04","B05","B06","B07","B08","B09","B10","B11","B12","B13","B14","B15","E01","E02","E03","E04","A01","A02","A03","A04","A05","A06","A07","PA1","PA2","PA3"]
                filtroproducidoqs=Q()
                filtroentradaqs=Q()
                filtroentradaexcludeqs=Q()
                filtrosalidaqs=Q()
                filtrosalida2qs=Q()
                filtrosalidaexcludeqs=Q()
                filtrocallesbptqs=Q()
                filtroexcallesbptqs=Q()
                print("iterando para llenar las listas..")



                for item in listafiltrocallesbpt:#OJO acá falta incluir en el filtro para que considere sólo los pallets que entraron a PLL dentro del mismo turno
                    filtrocallesbptqs = filtrocallesbptqs | Q(DESTINATION=item)

                for item in listafiltrocallesbpt:#OJO acá falta incluir en el filtro para que considere sólo los pallets que entraron a PLL dentro del mismo turno
                    filtroexcallesbptqs = filtroexcallesbptqs | Q(SOURCE=item)

                for item in listafiltroentrada:
                    filtroentradaqs = filtroentradaqs | Q(DESTINATION=item)


                for item in listafiltrosalida:
                    filtrosalidaqs = filtrosalidaqs | Q(DESTINATION=item)

                for item in listafiltrosalida2:
                    filtrosalida2qs = filtrosalida2qs | Q(DESTINATION=item)

                print("empezando a agregar los ingresos y salida al labels")

                for i in range(0,len(labels)):


                    print("haciendo consulta 1 Django")
                    #Filtro Entradas
                    filtro=MovPallets.objects.filter(filtroentradaqs, EVENTDATETIME__gte=labels[i]["fecha"], EVENTDATETIME__lt=labels[i]["fechafin"]).exclude(filtroentradaexcludeqs)

                    cantidad1=filtro.count()
                    #sumo los m2 asociados a cada pallets
                    m2tot=0
                    for mov in filtro:
                        m2tot=m2tot+mov.m2pallet

                    labels[i]["cantidadIn"]= cantidad1
                    labels[i]["m2In"]= m2tot
                    print("M2 en " + str(labels[i]["fecha"]) + ": " + str(m2tot) )



                    #sumo los m2 asociados a cada pallets

                    labels[i]["cantidadProd"]= 0
                    labels[i]["m2Prod"]= 0

                    print("haciendo consulta 3 Django")
                    #Salidas
                    filtro=MovPallets.objects.filter(filtrosalida2qs, EVENTDATETIME__gte=labels[i]["fecha"], EVENTDATETIME__lt=labels[i]["fechafin"]).exclude(filtrosalidaexcludeqs)
                    cantidad1=filtro.count()
                    #sumo los m2 asociados a cada pallet
                    m2tot=0
                    for mov in filtro:
                        m2tot=m2tot+mov.m2pallet



                    labels[i]["cantidadOut"]= cantidad1
                    labels[i]["m2Out"]= m2tot


                    #Movimientos a calles bpt
                    filtro=MovPallets.objects.filter(filtrocallesbptqs, EVENTDATETIME__gte=labels[i]["fecha"], EVENTDATETIME__lt=labels[i]["fechafin"]).exclude(filtroexcallesbptqs)
                    cantidad1=filtro.count()
                    #sumo los m2 asociados a cada pallet
                    m2tot=0
                    for mov in filtro:
                        m2tot=m2tot+mov.m2pallet



                    labels[i]["cantidadcallesbpt"]= cantidad1
                    labels[i]["m2BPT"]= m2tot


                print("completado, guardando el Model")


                #antiguos= Datos_MovPallets.objects.all().delete()

                print("Guandando entradas y salidas")
                for dato in labels:
                    #print(dato['cantidadIn'])
                    o = Datos_MovPallets.objects.create(programa=foto, fecha=dato['fecha'],fechafin=dato['fechafin'],turno=dato['turno'],label=dato['label'],cantidadcallesbpt=dato["cantidadcallesbpt"],m2BPT=dato["m2BPT"],cantidadIn=dato["cantidadIn"],m2In=dato['m2In'],cantidadProd=dato['cantidadProd'],m2Prod=dato['m2Prod'],cantidadOut=dato['cantidadOut'],m2Out=dato['m2Out'], m2Conv=dato['m2Conv'], m2Corr=dato['m2Corr'])
                    o.save()
                    sleep(0.05)


                ###############################################################
                #### Ahora calculo los datos de sólo los movimientos..

                print("iniciando datos B")

                listaopgruabpt=["1091/PATRICIO FARIAS", "1092/ROBERTO QUILALEO","1083/WALDO  MOLINA", "1095/RICARDO PRADO","1093/JORGE SOTO", "1097/PEDRO MIRANDA", "1096/JORGE ARENAS", "1098/JONATHAN RIVEROS", "1099/SEBASTIAN PONCE", "1112/PETERSON RAIMOND", "1110/VICTOR CORTES", "1111/LUIS LOPEZ", "1090/RENE DONOSO","1193/Jose Salas","-","-","-"]
                filtroopgruabptqs=Q()

                for op in listaopgruabpt:
                    filtroopgruabptqs = filtroopgruabptqs | Q(OPERATORCODENAME=op)




                labels2=[]
                ahora=datetime.now().replace(minute=0, second=0, microsecond=0)
                for i in range(0,150):
                    #por ahora los voy a ordenar por turno, después por hora.
                    print("rango movpallet detalle:")


                    fechaini=(ahora+timedelta(hours=1)-timedelta(minutes=(150-i)*10))
                    fechafin=(ahora+timedelta(hours=1)-timedelta(minutes=(150-i-1)*10))

                    print(fechaini)


                    label= (fechaini.strftime("%d-%m %H:%M")+ " a " + fechafin.strftime("%H:%M"))
                    #calculo el m2 real convertido y corrugado en ese turno, para comparar con las salidas y entradas declaradas
                    #m2Conv, m2Corr= pruebaodbcconvertprod.consulta(fecha,fechafin)
                    #print(m2Corr)


                    #movimientos por cada gruero:
                    datosopB=[[0,"0"]]
                    for op in listaopgruabpt:
                        datosopB.append([op , MovPallets.objects.filter( filtrosalidaqs , OPERATORCODENAME=op, EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count(), MovPallets.objects.filter( filtrocallesbptqs , OPERATORCODENAME=op, EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count() ])
                    #print(datosop)


                    #Calculo el n° de movimientos registrados en ese turno:

                    #hago el filtrro de movimientos internos en bodega

                    datosWIP={
                    "C01":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
                    "C02":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
                    "C03":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
                    "C04":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
                    "C05":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
                    "C06":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
                    "C07":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
                    "C08":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
                    "C09":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
                    "C10":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
                    "C11":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
                    "C12":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
                    "C13":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":11,"al2":37,"al3":44},
                    "B01":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
                    "B02":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":13,"al3":44},
                    "B03":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
                    "B04":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
                    "B05":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
                    "B06":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
                    "B07":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
                    "B08":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
                    "B09":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
                    "B10":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
                    "B11":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
                    "B12":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
                    "B13":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
                    "B14":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
                    "B15":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":37,"al3":44},
                    "E01":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
                    "E02":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
                    "E03":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
                    "E04":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
                    "A01":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
                    "A02":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
                    "A03":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
                    "A04":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
                    "A05":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
                    "A06":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
                    "A07":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
                    "PA1":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
                    "PA2":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},
                    "PA3":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},}


                    filtromovinternoqs =Q()

                    for calle in datosWIP.keys():

                        filtromovinternoqs = filtromovinternoqs | Q(DESTINATION=str(calle))

                    if MovPallets.objects.filter(Q(DESTINATION="PLL")).filter(EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count()>0:
                        movsaBPT= 1
                    else:
                        movsaBPT= 0



                    if MovPallets.objects.filter(filtromovinternoqs).filter(EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count()>0:
                        movsaCalles= 1
                    else:
                        movsaCalles= 0
                    #movsandenes= MovPallets.objects.filter(Q(DESTINATION="AN1") | Q(DESTINATION="AN2") | Q(DESTINATION="AN3") | Q(DESTINATION="AN4") | Q(DESTINATION="AN5") | Q(DESTINATION="AN6") | Q(DESTINATION="AN7") | Q(DESTINATION="AN8") | Q(DESTINATION="AN9")).filter(EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count()
                    movsandenes1= MovPallets.objects.filter(DESTINATION="AN1", EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count()
                    movsandenes2= MovPallets.objects.filter(DESTINATION="AN2", EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count()
                    movsandenes3= MovPallets.objects.filter(DESTINATION="AN3", EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count()
                    movsandenes4= MovPallets.objects.filter(DESTINATION="AN4", EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count()
                    movsandenes5= MovPallets.objects.filter(DESTINATION="AN5", EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count()
                    movsandenes6= MovPallets.objects.filter(DESTINATION="AN6", EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count()


                    movsconv1= MovPallets.objects.filter(filtromovinternoqs).filter(EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count()
                    movsconv2= MovPallets.objects.filter(Q(DESTINATION="FFW") | Q(DESTINATION="DRO")| Q(DESTINATION="FFG")).filter( EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count()

                    print("labels2:")

                    labels2.append({"fechaini":fechaini,"fechafin":fechafin, "label": label, "movsaBPT":movsaBPT, "movsaCalles":movsaCalles, "movsandenes1":movsandenes1, "movsandenes2":movsandenes2, "movsandenes3":movsandenes3, "movsandenes4":movsandenes4, "movsandenes5":movsandenes5, "movsandenes6":movsandenes6, "movsconv1":movsconv1, "movsconv2":movsconv2, "opbpt1":datosopB[1][0], "movsopbpt1":datosopB[1][1], "opbpt2":datosopB[2][0], "movsopbpt2":datosopB[2][1], "opbpt3":datosopB[3][0], "movsopbpt3":datosopB[3][1], "opbpt4":datosopB[4][0], "movsopbpt4":datosopB[4][1], "opbpt5":datosopB[5][0], "movsopbpt5":datosopB[5][1], "opbpt6":datosopB[6][0], "movsopbpt6":datosopB[6][1], "opbpt7":datosopB[7][0], "movsopbpt7":datosopB[7][1], "opbpt8":datosopB[8][0], "movsopbpt8":datosopB[8][1], "opbpt9":datosopB[9][0], "movsopbpt9":datosopB[9][1], "opbpt10":datosopB[10][0], "movsopbpt10":datosopB[10][1], "opbpt11":datosopB[11][0], "movsopbpt11":datosopB[11][1], "opbpt12":datosopB[12][0], "movsopbpt12":datosopB[12][1], "opbpt13":datosopB[13][0], "movsopbpt13":datosopB[13][1], "opbpt14":datosopB[14][0], "movsopbpt14":datosopB[14][1], "movsopbptIN1":datosopB[1][2], "movsopbptIN2":datosopB[2][2],"movsopbptIN3":datosopB[3][2],"movsopbptIN4":datosopB[4][2], "movsopbptIN5":datosopB[5][2], "movsopbptIN6":datosopB[6][2],"movsopbptIN7":datosopB[7][2],"movsopbptIN8":datosopB[8][2],"movsopbptIN9":datosopB[9][2], "movsopbptIN10":datosopB[10][2], "movsopbptIN11":datosopB[11][2], "movsopbptIN12":datosopB[12][2], "movsopbptIN13":datosopB[13][2],"movsopbptIN14":datosopB[14][2]})
                    print("ok labels 2")


                for dato in labels2:
                    print("guardando el model")
                    #print(dato['cantidadIn'])
                    o = Datos_MovPallets_B.objects.create(programa=foto, fechaini=dato['fechaini'],fechafin=dato['fechafin'],label=dato['label'],movsaBPT=dato["movsaBPT"],movsaCalles=dato["movsaCalles"],movsandenes1=dato['movsandenes1'],movsandenes2=dato['movsandenes2'],movsandenes3=dato['movsandenes3'],movsandenes4=dato['movsandenes4'],movsandenes5=dato['movsandenes5'],movsandenes6=dato['movsandenes6'],movsconv1=dato['movsconv1'],movsconv2=dato['movsconv2'],opbpt1=dato['opbpt1'],movsopbpt1=dato['movsopbpt1'],opbpt2=dato['opbpt2'],movsopbpt2=dato['movsopbpt2'],opbpt3=dato['opbpt3'],movsopbpt3=dato['movsopbpt3'],opbpt4=dato['opbpt4'],movsopbpt4=dato['movsopbpt4'],opbpt5=dato['opbpt5'],movsopbpt5=dato['movsopbpt5'],opbpt6=dato['opbpt6'],movsopbpt6=dato['movsopbpt6'],opbpt7=dato['opbpt7'],movsopbpt7=dato['movsopbpt7'],opbpt8=dato['opbpt8'],movsopbpt8=dato['movsopbpt8'],opbpt9=dato['opbpt9'],movsopbpt9=dato['movsopbpt9'],opbpt10=dato['opbpt10'],movsopbpt10=dato['movsopbpt10'],opbpt11=dato['opbpt11'],movsopbpt11=dato['movsopbpt11'],opbpt12=dato['opbpt12'],movsopbpt12=dato['movsopbpt12'],opbpt13=dato['opbpt13'],movsopbpt13=dato['movsopbpt13'],opbpt14=dato['opbpt14'],movsopbpt14=dato['movsopbpt14'],movsopbptIN1=dato['movsopbptIN1'],movsopbptIN2=dato['movsopbptIN2'],movsopbptIN3=dato['movsopbptIN3'],movsopbptIN4=dato['movsopbptIN4'],movsopbptIN5=dato['movsopbptIN5'],movsopbptIN6=dato['movsopbptIN6'],movsopbptIN7=dato['movsopbptIN7'],movsopbptIN8=dato['movsopbptIN8'],movsopbptIN9=dato['movsopbptIN9'],movsopbptIN10=dato['movsopbptIN10'],movsopbptIN11=dato['movsopbptIN11'],movsopbptIN12=dato['movsopbptIN12'],movsopbptIN13=dato['movsopbptIN13'],movsopbptIN14=dato['movsopbptIN14'])

                    o.save()

                    print("model guardado")




                #Borrar las fotos antiguos..
                instance=Foto_Datos_MovPallets.objects.filter(fecha_foto__lt=foto.fecha_foto)
                instance.delete()
                print("foto datos_movpalles antiguos borrados!!")
                print(":D")
                sleep(3)
            except Exception as e:
                print("errooorrr")
                print(e)
                print("error!!")
                print(" ")
                sleep(10)
                ###########


    def updatewipprog(self):
        if 1:
            try:

                print("actualizo el update_wip_prog")

                listaCorrplanINV=("TCY","HCR","WRD","FFW","DRO","FFG")
                ahora=datetime.now()
                for maq in listaCorrplanINV:
                    print(maq)
                    #datosCorrplanINV.[str(maq)]['indice']= UbicPallet.objects.get(calle__iexact=str(calle)).pk
                    auxm2inv=0
                    auxm2inv24h=0
                    auxm2totprog24h=0
                    print("Corrplan 24h entre:")
                    print(ahora)
                    print("y")
                    print(ahora+timedelta(days=1))
                    for order in OrdenCorrplan.objects.filter(fecha_inicio__gte=ahora, fecha_inicio__lte=ahora+timedelta(days=12), maquina=Maquinas.objects.filter(maquina=str(maq))[0]):
                        for pallet in Pallet.objects.filter( Q(ubic="ZFFG1") | Q(ubic="ZFFG2")| Q(ubic="ZFFW1")| Q(ubic="ZFFW2")| Q(ubic="ZDRO1")| Q(ubic="ZDRO2")| Q(ubic="ZTCY1") | Q(ubic="ZTCY2")| Q(ubic="ZWRD1")| Q(ubic="ZWRD2")| Q(ubic="ZHCR1")| Q(ubic="ZHCR2")| Q(ubic="ZSOB1") | Q(ubic="ZSOB2") | Q(ubic="ZPASILLO")):
                            if pallet.ORDERID == order.order_id:
                                auxm2inv=auxm2inv+pallet.m2pallet


                    for order in OrdenCorrplan.objects.filter(fecha_inicio__gte=ahora, fecha_inicio__lte=ahora+timedelta(days=1), maquina=Maquinas.objects.filter(maquina=str(maq))[0]):
                        auxm2totprog24h=auxm2totprog24h+order.area
                        for pallet in Pallet.objects.filter( Q(ubic="ZFFG1") | Q(ubic="ZFFG2")| Q(ubic="ZFFW1")| Q(ubic="ZFFW2")| Q(ubic="ZDRO1")| Q(ubic="ZDRO2")| Q(ubic="ZTCY1") | Q(ubic="ZTCY2")| Q(ubic="ZWRD1")| Q(ubic="ZWRD2")| Q(ubic="ZHCR1")| Q(ubic="ZHCR2")| Q(ubic="ZSOB1") | Q(ubic="ZSOB2") | Q(ubic="ZPASILLO")):
                            if pallet.ORDERID == order.order_id:
                                auxm2inv24h=auxm2inv24h+pallet.m2pallet

                    #datosCorrplanINV[str(maq)]['m2Prog24h']=auxm2totprog24h # Toto lo que se va a consumir según corrplan en las prox 24h.
                    #datosCorrplanINV[str(maq)]['m2inv24h']=auxm2inv24h # de lo que se va a consumir el 24 horas, lo que sí está en inventario.
                    #datosCorrplanINV[str(maq)]['m2inv']=auxm2inv# Todo lo que está en inventario asignado a esa máquina y que esté en corrplan, independiente de cuándo se vaya a consumir.
                    o, created=DatosWIP_Prog.objects.get_or_create(maquina=str(maq))
                    o.m2Prog24h=auxm2totprog24h
                    o.m2inv24h=auxm2inv24h
                    o.m2inv=auxm2inv
                    o.save()
                    sleep(0.5)
            except Exception as e:
                print(e)
                print("error")
                sleep(10)


    def updateproywip(self):
        if 1:
            print("para el cálculo del aproyección primero saco el dato del programa de corrugado:")
            try:
                prog_corrugado = webscrap3.webscrap_prog_corr()


                foto, created =FotoProgCorr.objects.get_or_create(fecha_foto=datetime.now())
                foto.save()
                #Borrar los antiguos..
                instance=FotoProgCorr.objects.filter(fecha_foto__lt=foto.fecha_foto)
                instance.delete()



                fecha_fin_anterior=0
                for prog in prog_corrugado:
                    #transformando el dato de fecha a datetime

                    fechafin=datetime.strptime(prog[6], '%d-%m %H:%M')
                    fechafin=fechafin.replace(year= datetime.now().year)
                    #print(fechafin)

                    id, created =IDProgCorr.objects.get_or_create(programa=foto, order_id=prog[1], color=prog[0], fecha_fin=fechafin)
                    id.ancho=int(prog[2])
                    id.refile=int(prog[3])
                    id.carton=prog[4]
                    id.metrosL=int(prog[5])
                    if fecha_fin_anterior==0:
                        id.fecha_inicio=fechafin
                    else:
                        id.fecha_inicio=fecha_fin_anterior
                    id.area=(((int(prog[2])-int(prog[3]))/1000)*int(prog[5]))/1000

                    #registro datos del upper knife:
                    id.UKID=prog[7]
                    #calculo área placa
                    ancho,largo =prog[8].split(' x ')
                    areaplaca=(int(ancho)/1000)*(int(largo)/1000)
                    id.UKID_areaplaca=areaplaca
                    id.UKID_nplacas=int(prog[9])
                    id.UKID_areatot=int(prog[9])*areaplaca

                    id.LKID=prog[11]
                    #calculo área placa
                    ancho,largo =prog[12].split(' x ')
                    areaplaca=(int(ancho)/1000)*(int(largo)/1000)
                    id.LKID_areaplaca=areaplaca
                    id.LKID_nplacas=int(prog[13])
                    id.LKID_areatot=int(prog[13])*areaplaca


                    #sleep(30)


                    id.save()
                    fecha_fin_anterior = id.fecha_fin
                    #print(id)
                    #print(id.fecha_inicio)
                    #print(id.fecha_fin)


                #########

                print("Ahora actualizo los datos del panel de proyección.")

                print("hago lista de fechas que quiero mostrar:") #basado en el get_data_mov_pallets pero genera las fechas a futuro. Como texto y como datetime
                labels=[]#fechas, será el label del gráfico
                ahora=datetime.now()
                ahorafix=ahora.replace(hour= 0, minute=0, second=0, microsecond=0)-timedelta(days=1)
                for i in range(0,3):
                    #por ahora los voy a ordenar por turno, después por hora.
                    fecha_inicio=(ahorafix+timedelta(days=i)).replace(hour= 7)
                    fecha_fin=(ahorafix+timedelta(days=i)).replace(hour= 14, minute=30)
                    turno="A"
                    label= fecha_inicio.strftime("%d-%m") + " " + turno
                    if ahora<=fecha_fin:#ahora<=(ahorafix+timedelta(days=i)).replace(hour= 14, minute=30):
                        labels.append({"fecha_inicio":fecha_inicio ,"fecha_fin":fecha_fin ,"turno":turno, "label": label})

                    fecha_inicio=(ahorafix+timedelta(days=i)).replace(hour= 14, minute=30)
                    fecha_fin=(ahorafix+timedelta(days=i)).replace(hour= 22)
                    turno="B"
                    label= fecha_inicio.strftime("%d-%m") + " " + turno
                    if ahora<=fecha_fin:#ahora<=(ahorafix+timedelta(days=i)).replace(hour= 22):
                        labels.append({"fecha_inicio":fecha_inicio ,"fecha_fin":fecha_fin ,"turno":turno, "label": label})

                    fecha_inicio=(ahorafix+timedelta(days=i)).replace(hour= 22)
                    fecha_fin=(ahorafix+timedelta(days=i+1)).replace(hour= 7)
                    turno="C"
                    label= fecha_inicio.strftime("%d-%m") + " " + turno
                    if ahora<=fecha_fin:#ahora<=(ahorafix+timedelta(days=i+1)).replace(hour= 7):
                        labels.append({"fecha_inicio":fecha_inicio ,"fecha_fin":fecha_fin,"turno":turno,"label": label})

                #Ahora, por cada label, calculo la suma de Mm2 de conversión que se iniciarán en ese turno según corrplan

                print(labels)

                #calculo el inventario inicial a la fecha en el WIP:
                invtotwip=0
                for pallet in Pallet.objects.filter( Q(ubic="ZFFG1") | Q(ubic="ZFFG2")| Q(ubic="ZFFW1")| Q(ubic="ZFFW2")| Q(ubic="ZDRO1")| Q(ubic="ZDRO2")| Q(ubic="ZTCY1") | Q(ubic="ZTCY2")| Q(ubic="ZWRD1")| Q(ubic="ZWRD2")| Q(ubic="ZHCR1")| Q(ubic="ZHCR2")| Q(ubic="ZSOB1") | Q(ubic="ZSOB2") | Q(ubic="ZPASILLO")):
                #        if pallet.ORDERID != order.order_id:
                    invtotwip=invtotwip+(pallet.m2pallet/1000)



                fecha_anterior=0
                for turn in labels:
                    #print(turno['fecha'])


                    filtro=OrdenCorrplan.objects.filter(fecha_inicio__gte=turn['fecha_inicio']).filter(fecha_inicio__gte=ahora).filter(fecha_inicio__lt=turn['fecha_fin'])
                    sumaM2=0
                    for orden in filtro:
                        sumaM2=sumaM2 + orden.area
                    #print(sumaM2)

                    turn["M2Conv"]=sumaM2


                    filtrocorr=IDProgCorr.objects.filter(fecha_inicio__gte=turn['fecha_inicio']).filter(fecha_inicio__gte=ahora).filter(fecha_inicio__lt=turn['fecha_fin'])
                    sumaM2=0
                    print("suma M2 corr filtro inicio entre " + str(turn['fecha_inicio']) + " y " + str(turn['fecha_fin']) )
                    for orden in filtrocorr:
                        print(str(orden)+": "+ str(orden.fecha_inicio))


                        sumaM2=sumaM2 + (orden.area)
                    print("suma tot M2 tramo: " + str(sumaM2) )
                    turn["M2Corr"]=sumaM2




                    datosWIP={"ZFFG1":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZFFG2":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZDRO1":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZDRO2":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZFFW1":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZFFW2":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZSOB1":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZWRD1":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZWRD2":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZSOB2":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZHCR1":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZHCR2":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZTCY1":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZTCY2":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZPNC":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZPASILLO":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0}}

                    filtrocalleqs=Q()

                    for calle in datosWIP.keys():
                        filtrocalleqs = filtrocalleqs | Q(ubic=calle)

                    #los pallets que están en esa ubicación según CTI, pero exluyendo los que ya están en palletstomainv
                    palletsencorrplan= Pallet.objects.filter(filtrocalleqs).filter(ORDERID__in=[o.order_id for o in filtro])

                    m2enInv=0
                    for pallet in palletsencorrplan:
                        m2enInv+=pallet.m2pallet
                    print("M2 en inventario para este corrplan")
                    print(m2enInv)

                    #ahora, de la lista de IDs en UKID y LKID, veo cuáles coinciden con los ID que están en corrplan para ese día. ése M2 se lo resto al ProyCorr ya que sí está programado.




                    UKIDencorrplan= IDProgCorr.objects.filter(fecha_inicio__gte=turn['fecha_inicio']).filter(fecha_inicio__gte=ahora).filter(fecha_inicio__lt=turn['fecha_fin']).filter(UKID__in=[o.order_id for o in filtro])
                    m2enProgCorr=0


                    filtrocorr2=IDProgCorr.objects.filter(fecha_inicio__gte=ahora).filter(fecha_inicio__lt=turn['fecha_fin'])

                    for ordencorr in filtrocorr2:
                        #print("ordencorr" + ordencorr.UKID)
                        for ordenprog in filtro:
                            #print("ordencorrplan" + ordenprog.order_id)
                            if ordencorr.UKID == ordenprog.order_id:
                                m2enProgCorr+=ordencorr.UKID_areatot
                                print("coincide!")
                                #sleep(30)

                            if ordencorr.LKID == ordenprog.order_id:
                                m2enProgCorr+=ordencorr.LKID_areatot
                                print("coincide!")



                    print(m2enProgCorr)


                    turn["M2ProyCorr"]=turn["M2Conv"]-(m2enInv/1000)-(m2enProgCorr/1000)

                    invtotwip=invtotwip+int(turn["M2Corr"])-int(turn["M2Conv"])+int(turn["M2ProyCorr"])

                    #ahora, de la lista de IDs en UKID y LKID, veo cuáles coinciden con los ID que están en corrplan para ese día.


                    turn["M2Inv"]=invtotwip

                    #ya tengo la porción de Corrplan que no está en inventario para cada día. Me falta la porción de corrplan que está cubierta por la producción programada de corrugado.
                    #cómo ahora no hay inventario programado, voy a mostrar el graf sólo con la primera parte.

                antiguos= Datos_Proy_WIP.objects.all().delete()



                print(labels)

                for dato in labels:

                    o = Datos_Proy_WIP.objects.create(fecha_inicio=dato['fecha_inicio'],fecha_fin=dato['fecha_fin'],turno=dato['turno'],label=dato['label'],M2Conv=dato['M2Conv'],M2Corr=dato['M2Corr'],M2Inv=dato['M2Inv'],M2ProyCorr=dato['M2ProyCorr'])
                    o.save()
                    sleep(0.02)




            except Exception as e:
                print(e)
                print("error")
                sleep(10)





    #def updatepanelwip(self):

    def handle(self, *args, **options):
        while (1):

            try:
                self.updatekpisemanal()
                self.updatemovpallets()
                self.update_datos_wip()


                #self.updatewipprog()
                #self.updateproywip()



                ###########


                print("Esperando para hacer prox carga masiva de datos")
                sleep(3)

            except Exception as e:
                print(e)
                print("error, posiblemente database is locked??")
                sleep(10)

        #print(labels)
