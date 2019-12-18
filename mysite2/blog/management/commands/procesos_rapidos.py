from django.core.management.base import BaseCommand, CommandError
from blog.models import OrdenCorrplan as OrdenCorrplan
from blog.models import FotoCorrplan as FotoCorrplan
from blog.models import FotoProgCorr as FotoProgCorr
from blog.models import FiltroEntradaWIP as FiltroEntradaWIP
from blog.models import FiltroSalidaWIP as FiltroSalidaWIP
from blog.models import Datos_Proy_WIP as Datos_Proy_WIP
from blog.models import DatosWIP_Prog as DatosWIP_Prog
#from blog.models import Datos_INV_WIP as Datos_INV_WIP
from blog.models import MovPallets as MovPallets
from blog.models import Datos_MovPallets as Datos_MovPallets
from blog.models import Datos_MovPallets_B as Datos_MovPallets_B
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
        "CORR_UPPER_Stacker":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":1,"al2":2,"al3":3},
        "CORR_LOWER_Stacker":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":1,"al2":2,"al3":3},
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
        "PLL":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":5,"al2":10,"al3":20}}

        m2totalINV=0
        npalletstotalINV=0

        m2totalCORR=0
        npalletstotalCORR=0


        for calle in datosWIP.keys():

            datosWIP[str(calle )]['cuenta']= Pallet.objects.filter(ubic__iexact=str(calle)).count()
            datosWIP[str(calle)]['indice']= UbicPallet.objects.get(calle__iexact=str(calle)).pk
            try:
                datosWIP[str(calle)]['dias']= (datetime.now()-(Pallet.objects.filter(ubic__iexact=str(calle)).earliest('fechacreac').fechacreac.replace(tzinfo=None))).days#- datetime.now()))

            except:
                datosWIP[str(calle)]['dias']=0
                print("errorn no se encontraron días en calle")

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
        filtro=MovPallets.objects.filter(Q(DESTINATION="PLL") | Q(DESTINATION="PT10")).exclude( Q(SOURCE="PLL") | Q(SOURCE="PT10")).order_by('-TRANSACTIONINDEX')[:4]

        # referencia: datetime.strptime(datoprocesado[1][colFecha], "%d-%m-%Y %H:%M")

        for mov in filtro:
            #movimiento=[tarja, destino, hora]
            movimiento=[mov.LOADID, mov.ORDERID, mov.SOURCE, mov.DESTINATION, mov.EVENTDATETIME.strftime("%d-%m-%y %H:%M:%S")]
            filtroentrada.append(movimiento)

        #print(filtroentrada)
        filtrosalida=[]
        filtro2=MovPallets.objects.filter(Q(DESTINATION="Truck") | Q(DESTINATION="AN1") | Q(DESTINATION="AN2")| Q(DESTINATION="AN3")| Q(DESTINATION="AN4")| Q(DESTINATION="AN5") | Q(DESTINATION="AN6")| Q(DESTINATION="AN7") | Q(DESTINATION="AN8")| Q(DESTINATION="AN9") ).order_by('-TRANSACTIONINDEX')[:4]

        for mov in filtro2:
            #movimiento=[tarja, destino, hora]
            movimiento=[mov.LOADID, mov.ORDERID, mov.SOURCE, mov.DESTINATION, mov.EVENTDATETIME.strftime("%d-%m-%y %H:%M:%S")]
            filtrosalida.append(movimiento)


        print(filtroentrada)
        print(filtrosalida)

        print("Pasando objetos: ")



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


        #sectores:
        for calle in datosWIP.keys():

            dato, created =Datos_Inv_WIP.objects.get_or_create(programa=foto, sector=str(calle), cuenta=datosWIP[str(calle)]['cuenta'], m2tot=datosWIP[str(calle)]['m2tot'], indice=datosWIP[str(calle)]['indice'], dias=datosWIP[str(calle)]['dias'], al1=datosWIP[str(calle)]['al1'], al2=datosWIP[str(calle)]['al2'], al3=datosWIP[str(calle)]['al3'])
            dato.save()

        instance=Foto_Datos_Inv_WIP.objects.filter(fecha_foto__lt=foto.fecha_foto)
        instance.delete()



        print("Enviando datos inventario")


    def updatemovpallets(self):
        if 1:#########

            #CREO UNA nueva foto de movspallets:
            foto, created =Foto_Datos_MovPallets.objects.get_or_create(fecha_foto=datetime.now())
            foto.save()

            print("actualizo el Movpallets")

            try:


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
                    m2Conv, m2Corr= pruebaodbcconvertprod.consulta(fecha,fechafin)
                    #print(m2Corr)
                    labels.append({"fecha":fecha ,"fechafin":fechafin ,"turno":turno, "label": label, "m2Conv": m2Conv, "m2Corr": m2Corr})

                    fecha=(ahora+timedelta(days=1)-timedelta(days=horizonte-i)).replace(hour= 14, minute=30)
                    fechafin=(ahora+timedelta(days=1)-timedelta(days=horizonte-i)).replace(hour= 22)
                    turno="B"
                    label= fecha.strftime("%d-%m") + " " + turno
                    m2Conv, m2Corr= pruebaodbcconvertprod.consulta(fecha,fechafin)
                    #print(m2Corr)
                    labels.append({"fecha":fecha ,"fechafin":fechafin ,"turno":turno, "label": label, "m2Conv": m2Conv, "m2Corr": m2Corr})

                    fecha=(ahora+timedelta(days=1)-timedelta(days=horizonte-i)).replace(hour= 22)
                    fechafin=(ahora+timedelta(days=1)-timedelta(days=horizonte-i-1)).replace(hour= 7)
                    turno="C"
                    label= fecha.strftime("%d-%m") + " " + turno
                    m2Conv, m2Corr= pruebaodbcconvertprod.consulta(fecha,fechafin)
                    #print(m2Corr)
                    labels.append({"fecha":fecha ,"fechafin":fechafin ,"turno":turno, "label": label, "m2Conv": m2Conv, "m2Corr": m2Corr})

                print("ahora calculo las listas de lo que se declaró como ingreso y como salida al wip  ")


                listafiltroproducido=["CORR_UPPER_Stacker", "CORR_LOWER_Stacker"]
                listafiltroentrada=["PLL","PT10"]
                listafiltrosalida=["AN1","AN2","AN3","AN4","AN5","AN6","AN7","AN8","AN9"]

                filtroproducidoqs=Q()
                filtroentradaqs=Q()
                filtroentradaexcludeqs=Q()
                filtrosalidaqs=Q()
                filtrosalidaexcludeqs=Q()
                print("iterando para llenar las listas..")
                for item in listafiltroproducido:
                    filtroproducidoqs = filtroproducidoqs | Q(DESTINATION=item)

                for item in listafiltroentrada:
                    filtroentradaqs = filtroentradaqs | Q(DESTINATION=item)

                for item in listafiltroentrada:
                    filtroentradaexcludeqs = filtroentradaexcludeqs | Q(SOURCE=item)


                for item in listafiltrosalida:
                    filtrosalidaqs = filtrosalidaqs | Q(DESTINATION=item)

                for item in listafiltrosalida:
                    filtrosalidaexcludeqs = filtrosalidaexcludeqs | Q(SOURCE=item)

                print("empezando a agregar los ingresos y salida al labels")

                for i in range(0,len(labels)):


                    #Entradas
                    filtro=MovPallets.objects.filter(filtroentradaqs, EVENTDATETIME__gte=labels[i]["fecha"], EVENTDATETIME__lt=labels[i]["fechafin"]).exclude(filtroentradaexcludeqs)

                    cantidad1=filtro.count()
                    #sumo los m2 asociados a cada pallets
                    m2tot=0
                    for mov in filtro:
                        m2tot=m2tot+mov.m2pallet

                    labels[i]["cantidadIn"]= cantidad1
                    labels[i]["m2In"]= m2tot
                    print("M2 en " + str(labels[i]["fecha"]) + ": " + str(m2tot) )



                    #Producidos pero excluyendo los pallets que ya están en la lista de Entradas (acá saco el m2 actualizado de cada pallet, para descartar las producciones que se fueron a cero)
                    filtro2=MovPallets.objects.filter(filtroproducidoqs, EVENTDATETIME__gte=labels[i]["fecha"], EVENTDATETIME__lt=labels[i]["fechafin"])


                    for item in filtro:
                        filtro2=filtro2.exclude(LOADID=item.LOADID)


                    cantidad1=filtro2.count()
                    #sumo los m2 asociados a cada pallets
                    m2tot=0
                    for mov in filtro2:
                        #print(str(mov) + ".." + str(mov.LOADID) )
                        try:
                            m2tot=m2tot+Pallet.objects.get(tarja=mov.LOADID).m2pallet
                        except Exception as e:
                            print(e)
                            print("error con " + str(mov) + ".." + str(mov.LOADID) + "!!")


                    labels[i]["cantidadProd"]= cantidad1
                    labels[i]["m2Prod"]= m2tot


                    #Salidas
                    filtro=MovPallets.objects.filter(filtrosalidaqs, EVENTDATETIME__gte=labels[i]["fecha"], EVENTDATETIME__lt=labels[i]["fechafin"]).exclude(filtrosalidaexcludeqs)
                    cantidad1=filtro.count()
                    #sumo los m2 asociados a cada pallet
                    m2tot=0
                    for mov in filtro:
                        m2tot=m2tot+mov.m2pallet



                    labels[i]["cantidadOut"]= cantidad1
                    labels[i]["m2Out"]= m2tot



                print("completado, guardando el Model")


                #antiguos= Datos_MovPallets.objects.all().delete()

                print("Guandando entradas y salidas")
                for dato in labels:
                    #print(dato['cantidadIn'])
                    o = Datos_MovPallets.objects.create(programa=foto, fecha=dato['fecha'],fechafin=dato['fechafin'],turno=dato['turno'],label=dato['label'],cantidadIn=dato["cantidadIn"],m2In=dato['m2In'],cantidadProd=dato['cantidadProd'],m2Prod=dato['m2Prod'],cantidadOut=dato['cantidadOut'],m2Out=dato['m2Out'], m2Conv=dato['m2Conv'], m2Corr=dato['m2Corr'])
                    o.save()
                    sleep(0.05)


                #### Ahora calculo los datos de sólo los movimientos..

                labels2=[]
                ahora=datetime.now().replace(minute=0, second=0, microsecond=0)
                for i in range(0,300):
                    #por ahora los voy a ordenar por turno, después por hora.
                    print("rango movpallet detalle:")


                    fechaini=(ahora+timedelta(hours=1)-timedelta(minutes=(300-i)*5))
                    fechafin=(ahora+timedelta(hours=1)-timedelta(minutes=(300-i-1)*5))

                    print(fechaini)


                    label= (fechaini.strftime("%d-%m %H:%M")+ " a " + fechafin.strftime("%H:%M"))
                    #calculo el m2 real convertido y corrugado en ese turno, para comparar con las salidas y entradas declaradas
                    #m2Conv, m2Corr= pruebaodbcconvertprod.consulta(fecha,fechafin)
                    #print(m2Corr)

                    #Calculo el n° de movimientos registrados en ese turno:

                    movsaBPT= MovPallets.objects.filter(Q(DESTINATION="PLL")).filter(EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count()
                    movsandenes= MovPallets.objects.filter(Q(DESTINATION="AN1") | Q(DESTINATION="AN2") | Q(DESTINATION="AN3") | Q(DESTINATION="AN4") | Q(DESTINATION="AN5") | Q(DESTINATION="AN6") | Q(DESTINATION="AN7") | Q(DESTINATION="AN8") | Q(DESTINATION="AN9")).filter(EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count()
                    movsconv1= MovPallets.objects.filter(Q(DESTINATION="TCY") | Q(DESTINATION="HCR")| Q(DESTINATION="WRD")).filter( EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count()
                    movsconv2= MovPallets.objects.filter(Q(DESTINATION="FFW") | Q(DESTINATION="DRO")| Q(DESTINATION="FFG")).filter( EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count()
                    labels2.append({"fechaini":fechaini,"fechafin":fechafin, "label": label, "movsaBPT":movsaBPT, "movsandenes":movsandenes, "movsconv1":movsconv1, "movsconv2":movsconv2})
                    print(movsconv2)
                for dato in labels2:
                    #print(dato['cantidadIn'])
                    o = Datos_MovPallets_B.objects.create(programa=foto, fechaini=dato['fechaini'],fechafin=dato['fechafin'],label=dato['label'],movsaBPT=dato["movsaBPT"],movsandenes=dato['movsandenes'],movsconv1=dato['movsconv1'],movsconv2=dato['movsconv2'])
                    o.save()
                    sleep(0.05)


                #Borrar las fotos antiguos..
                instance=Foto_Datos_MovPallets.objects.filter(fecha_foto__lt=foto.fecha_foto)
                instance.delete()
            except Exception as e:
                print(e)
                print("error")
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

            self.update_datos_wip()
            self.updatemovpallets()

            #self.updatewipprog()
            #self.updateproywip()



            ###########


            print("Esperando para hacer prox carga masiva de datos")
            sleep(3)
        #print(labels)
