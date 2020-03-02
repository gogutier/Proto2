from django.core.management.base import BaseCommand, CommandError
from blog.models import OrdenCorrplan as OrdenCorrplan
from blog.models import FotoCorrplan as FotoCorrplan
from blog.models import FotoProgCorr as FotoProgCorr
from blog.models import m2Maqruta_WIP as m2Maqruta_WIP
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

from blog.models import TomaInvCic as TomaInvCic
from blog.models import PalletCic as PalletCic
from blog.models import Foto_Inv_Cic_WIP as Foto_Inv_Cic_WIP
from blog.models import Foto_Calles_Inv_Cic_WIP as Foto_Calles_Inv_Cic_WIP
from blog.models import Foto_Palletscti_Inv_Cic_WIP as Foto_Palletscti_Inv_Cic_WIP
from blog.models import Foto_Palletsencontrados_Inv_Cic_WIP as Foto_Palletsencontrados_Inv_Cic_WIP
from blog.models import Foto_Palletsenotracalle_Inv_Cic_WIP as Foto_Palletsenotracalle_Inv_Cic_WIP
from blog.models import Foto_Palletsnoencontrados_Inv_Cic_WIP as Foto_Palletsnoencontrados_Inv_Cic_WIP

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
        datosWIP={"ZFFG1":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":36,"al2":45,"al3":52},"ZFFG2":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":36,"al2":45,"al3":52},"ZDRO1":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":36,"al2":45,"al3":52},"ZDRO2":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":36,"al2":45,"al3":52},"ZFFW1":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":36,"al2":45,"al3":53},"ZFFW2":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":36,"al2":45,"al3":52},"ZSOB1":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":36,"al2":45,"al3":52},"ZWRD1":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":25,"al2":30,"al3":35},"ZWRD2":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":25,"al2":30,"al3":35},"ZSOB2":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":36,"al2":45,"al3":52},"ZHCR1":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":30,"al2":38,"al3":45},"ZHCR2":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":30,"al2":38,"al3":45},"ZTCY1":{"cuenta":0,"dias":0,"m2tot":0,"dias":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},"ZTCY2":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},"ZPNC":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":20,"al3":30},"CORR_UPPER_Stacker":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":1,"al2":2,"al3":3},"CORR_LOWER_Stacker":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":1,"al2":2,"al3":3},"ZPASILLO":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":1,"al2":2,"al3":3}}

        m2totalINV=0
        npalletstotalINV=0

        m2totalCORR=0
        npalletstotalCORR=0


        for calle in datosWIP.keys():
            print(str(calle))

            datosWIP[str(calle )]['cuenta']= Pallet.objects.filter(ubic__iexact=str(calle)).count()
            datosWIP[str(calle)]['indice']= UbicPallet.objects.get(calle__iexact=str(calle)).pk
            try:
                datosWIP[str(calle)]['dias']= (datetime.now()-(Pallet.objects.filter(ubic__iexact=str(calle)).earliest('fechacreac').fechacreac.replace(tzinfo=None))).days#- datetime.now()))

            except:
                datosWIP[str(calle)]['dias']=0

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



        print("calculando filtros últimas entradas y salidas")
        filtroentrada=[]
        filtro=MovPallets.objects.filter(Q(DESTINATION="ZPNC") | Q(DESTINATION="ZHCR1") | Q(DESTINATION="ZHCR2")| Q(DESTINATION="ZTCY1")| Q(DESTINATION="ZTCY2")| Q(DESTINATION="ZWRD1")| Q(DESTINATION="ZWRD2")| Q(DESTINATION="ZSOB1")| Q(DESTINATION="ZSOB2")| Q(DESTINATION="ZFFW1")| Q(DESTINATION="ZFFW2")| Q(DESTINATION="ZDRO1")| Q(DESTINATION="ZDRO2")| Q(DESTINATION="ZFFG1")| Q(DESTINATION="ZFFG2")| Q(DESTINATION="ZPNC")| Q(DESTINATION="ZPASILLO") ).exclude( Q(SOURCE="ZPNC") | Q(SOURCE="ZHCR1") | Q(SOURCE="ZHCR2")| Q(SOURCE="ZTCY1")| Q(SOURCE="ZTCY2")| Q(SOURCE="ZWRD1")| Q(SOURCE="ZWRD2")| Q(SOURCE="ZSOB1")| Q(SOURCE="ZSOB2")| Q(SOURCE="ZFFW1")| Q(SOURCE="ZFFW2")| Q(SOURCE="ZDRO1")| Q(SOURCE="ZDRO2")| Q(SOURCE="ZFFG1")| Q(SOURCE="ZFFG2")| Q(SOURCE="ZPNC")| Q(SOURCE="ZPASILLO")).order_by('-TRANSACTIONINDEX')[:4]

        # referencia: datetime.strptime(datoprocesado[1][colFecha], "%d-%m-%Y %H:%M")

        for mov in filtro:
            #movimiento=[tarja, destino, hora]
            movimiento=[mov.LOADID, mov.ORDERID, mov.SOURCE, mov.DESTINATION, mov.EVENTDATETIME.strftime("%d-%m-%y %H:%M:%S")]
            filtroentrada.append(movimiento)

        #print(filtroentrada)
        filtrosalida=[]
        filtro2=MovPallets.objects.filter(Q(DESTINATION="FFG") | Q(DESTINATION="FFW") | Q(DESTINATION="TCY")| Q(DESTINATION="HCR")| Q(DESTINATION="DRO")| Q(DESTINATION="WRD") | Q(DESTINATION="DIM")| Q(DESTINATION="TAB") | Q(DESTINATION="ZPICADO")| Q(DESTINATION="PLL") ).order_by('-TRANSACTIONINDEX')[:4]

        for mov in filtro2:
            #movimiento=[tarja, destino, hora]
            movimiento=[mov.LOADID, mov.ORDERID, mov.SOURCE, mov.DESTINATION, mov.EVENTDATETIME.strftime("%d-%m-%y %H:%M:%S")]
            filtrosalida.append(movimiento)


        #print(filtroentrada)
        #print(filtrosalida)



        m2maqruta={"TCY":0, "HCR":0, "WRD":0, "FFG":0, "DRO":0, "FFW":0, "Otros":0}

        for ruta in m2maqruta.keys():

            filt= Pallet.objects.filter(maqruta=str(ruta)).filter(Q(ubic="ZPNC") | Q(ubic="ZHCR1") | Q(ubic="ZHCR2")| Q(ubic="ZTCY1")| Q(ubic="ZTCY2")| Q(ubic="ZWRD1")| Q(ubic="ZWRD2")| Q(ubic="ZSOB1")| Q(ubic="ZSOB2")| Q(ubic="ZFFW1")| Q(ubic="ZFFW2")| Q(ubic="ZDRO1")| Q(ubic="ZDRO2")| Q(ubic="ZFFG1")| Q(ubic="ZFFG2")| Q(ubic="ZPNC")| Q(ubic="ZPASILLO") )
            totm2=0
            for pallet in filt:
                totm2=totm2 + pallet.m2pallet
            m2maqruta[ruta]= totm2




        print("Pasando objetos: ")



        foto, created =Foto_Datos_Inv_WIP.objects.get_or_create(fecha_foto=datetime.now())
        foto.m2totalINV = m2totalINV
        foto.save()
        #Borrar los antiguos..

        #filtroentrada:
        for ruta in m2maqruta.keys():
            m2Maqruta_WIP.objects.get_or_create(programa=foto, maquina=ruta, m2=m2maqruta[ruta])

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
                ahora=datetime.now().replace(hour= 0, minute=0,second=0, microsecond=0)
                horizonte=7
                for i in range(0,horizonte+1):
                    #por ahora los voy a ordenar por turno, después por hora.
                    fecha=(ahora-timedelta(days=horizonte-i)).replace(hour= 7, minute=0, second=0, microsecond=0)
                    fechafin=(ahora-timedelta(days=horizonte-i)).replace(hour= 14, minute=30, second=0, microsecond=0)
                    turno="A"
                    label= fecha.strftime("%d-%m") + " " + turno
                    #calculo el m2 real convertido y corrugado en ese turno, para comparar con las salidas y entradas declaradas
                    m2Conv, m2Corr= pruebaodbcconvertprod.consulta(fecha,fechafin)
                    #print(m2Corr)
                    labels.append({"fecha":fecha ,"fechafin":fechafin ,"turno":turno, "label": label, "m2Conv": m2Conv, "m2Corr": m2Corr})

                    fecha=(ahora-timedelta(days=horizonte-i)).replace(hour= 14, minute=30, second=0, microsecond=0)
                    fechafin=(ahora-timedelta(days=horizonte-i)).replace(hour= 22, minute=0, second=0, microsecond=0)
                    turno="B"
                    label= fecha.strftime("%d-%m") + " " + turno
                    m2Conv, m2Corr= pruebaodbcconvertprod.consulta(fecha,fechafin)
                    #print(m2Corr)
                    labels.append({"fecha":fecha ,"fechafin":fechafin ,"turno":turno, "label": label, "m2Conv": m2Conv, "m2Corr": m2Corr})

                    fecha=(ahora-timedelta(days=horizonte-i)).replace(hour= 22, minute=0, second=0, microsecond=0)
                    fechafin=(ahora-timedelta(days=horizonte-i-1)).replace(hour= 7, minute=0, second=0, microsecond=0)
                    turno="C"
                    label= fecha.strftime("%d-%m") + " " + turno
                    m2Conv, m2Corr= pruebaodbcconvertprod.consulta(fecha,fechafin)
                    #print(m2Corr)
                    labels.append({"fecha":fecha ,"fechafin":fechafin ,"turno":turno, "label": label, "m2Conv": m2Conv, "m2Corr": m2Corr})

                print("ahora calculo las listas de lo que se declaró como ingreso y como salida al wip  ")


                listafiltroproducido=["CORR_UPPER_Stacker", "CORR_LOWER_Stacker"]
                listafiltrobodega=["ZTCY1","ZTCY2","ZHCR1","ZHCR2","ZWRD1","ZWRD2","ZFFW1","ZFFW2","ZDRO1","ZDRO2","ZFFG1","ZFFG2","ZSOB1","ZSOB2","ZPASILLO","FFW", "FFG" , "DRO" ,"TCY" ,"HCR", "WRD" ,"DIM", "TAB"]
                listafiltroentrada=["ZTCY1","ZTCY2","ZHCR1","ZHCR2","ZWRD1","ZWRD2","ZFFW1","ZFFW2","ZDRO1","ZDRO2","ZFFG1","ZFFG2","ZSOB1","ZSOB2","ZPNC","ZPASILLO"]
                listafiltrosalida=["TCY","HCR","WRD","FFW","DRO","FFG","DIM","PLL"]
                listafiltropicado=["ZPICADO"]

                filtroproducidoqs=Q()
                filtrobodegaqs=Q()
                filtroentradaqs=Q()
                filtrosalidaqs=Q()
                filtrosalidaexcludeqs=Q()
                print("iterando para llenar las listas..")
                for item in listafiltroproducido:
                    filtroproducidoqs = filtroproducidoqs | Q(DESTINATION=item)

                for item in listafiltrobodega:
                    filtrobodegaqs = filtrobodegaqs | Q(SOURCE=item)

                for item in listafiltroentrada:
                    filtroentradaqs = filtroentradaqs | Q(DESTINATION=item)


                for item in listafiltrosalida:
                    filtrosalidaqs = filtrosalidaqs | Q(DESTINATION=item)

                for item in listafiltrosalida:
                    filtrosalidaexcludeqs = filtrosalidaexcludeqs | Q(SOURCE=item)

                print("empezando a agregar los ingresos y salida al labels")

                for i in range(0,len(labels)):


                    #Entradas
                    filtro=MovPallets.objects.filter(filtroentradaqs, EVENTDATETIME__gte=labels[i]["fecha"], EVENTDATETIME__lt=labels[i]["fechafin"]).filter( Q(SOURCE="CORR_UPPER_Stacker") | Q(SOURCE="CORR_LOWER_Stacker") )

                    cantidad1=filtro.count()
                    #sumo los m2 asociados a cada pallets
                    m2tot=0
                    for mov in filtro:
                        #checkeo si la fecha de creación de ese pallet es igual o posterior que el turno que estoy analizando (después se puede agregar la fecha de creación del pallet al movpallet)
                        if Pallet.objects.filter(tarja=mov.LOADID).count() >0:
                            filt=Pallet.objects.filter(tarja=mov.LOADID)[0]
                            print(str(filt.fechacreac.replace(tzinfo=None)) + "---vs---" + str(labels[i]["fecha"]))
                            if filt.fechacreac.replace(tzinfo=None)>=labels[i]["fecha"]:

                                m2tot=m2tot+mov.m2pallet

                    labels[i]["cantidadIn"]= cantidad1
                    labels[i]["m2In"]= m2tot


                    #Filtrando los que se movieron de stacker corrugado directo a máquina.
                    #Producidos pero excluyendo los pallets que ya están en la lista de Entradas (acá saco el m2 actualizado de cada pallet, para descartar las producciones que se fueron a cero)
                    filtro2=MovPallets.objects.filter(filtrosalidaqs, EVENTDATETIME__gte=labels[i]["fecha"], EVENTDATETIME__lt=labels[i]["fechafin"]).filter( Q(SOURCE="CORR_UPPER_Stacker") | Q(SOURCE="CORR_LOWER_Stacker") )


                    cantidad1=filtro2.count()
                    #sumo los m2 asociados a cada pallets
                    m2tot=0
                    for mov in filtro2:
                        #print(str(mov) + ".." + str(mov.LOADID) )

                        filt=Pallet.objects.filter(tarja=mov.LOADID)[0]
                        print(str(filt.fechacreac.replace(tzinfo=None)) + "---vs---" + str(labels[i]["fecha"]))
                        if filt.fechacreac.replace(tzinfo=None)>=labels[i]["fecha"]:
                            m2tot=m2tot+mov.m2pallet



                    labels[i]["cantidadDirectoConv"]= cantidad1
                    labels[i]["m2DirectoConv"]= m2tot


                    #Filtro los que se fueron directo a picado desde corrugado
                    filtro3=MovPallets.objects.filter( Q(DESTINATION="ZPICADO"), EVENTDATETIME__gte=labels[i]["fecha"], EVENTDATETIME__lt=labels[i]["fechafin"]).filter( Q(SOURCE="CORR_UPPER_Stacker") | Q(SOURCE="CORR_LOWER_Stacker") )


                    cantidad1=filtro3.count()
                    #sumo los m2 asociados a cada pallets
                    m2tot=0
                    for mov in filtro3:
                        #print(str(mov) + ".." + str(mov.LOADID) )

                        filt=Pallet.objects.filter(tarja=mov.LOADID)[0]
                        print(str(filt.fechacreac.replace(tzinfo=None)) + "---vs---" + str(labels[i]["fecha"]))
                        if filt.fechacreac.replace(tzinfo=None)>=labels[i]["fecha"]:
                            m2tot=m2tot+mov.m2pallet



                    labels[i]["cantidadCorrPicado"]=  cantidad1
                    labels[i]["m2CorrPicado"]= m2tot



                    #Salidas
                    filtro=MovPallets.objects.filter(filtrosalidaqs, EVENTDATETIME__gte=labels[i]["fecha"], EVENTDATETIME__lt=labels[i]["fechafin"]).exclude(filtrosalidaexcludeqs)
                    cantidad1=filtro.count()
                    #sumo los m2 asociados a cada pallet
                    m2tot=0
                    for mov in filtro:
                        m2tot=m2tot+mov.m2pallet



                    labels[i]["cantidadOut"]= cantidad1
                    labels[i]["m2Out"]= m2tot



                    filtro=MovPallets.objects.filter(Q(DESTINATION="HCR") | Q(DESTINATION="TCY") | Q(DESTINATION="WRD") | Q(DESTINATION="FFG") | Q(DESTINATION="FFW") | Q(DESTINATION="DRO") | Q(DESTINATION="DIM"), EVENTDATETIME__gte=labels[i]["fecha"], EVENTDATETIME__lt=labels[i]["fechafin"])
                    cantidad1=filtro.count()
                    #sumo los m2 asociados a cada pallet
                    m2tot=0
                    for mov in filtro:
                        m2tot=m2tot+mov.m2pallet

                    labels[i]["m2EntregadoAConv"]= m2tot


                    #Filtro de bodega a Picado

                    filtro=MovPallets.objects.filter(filtrobodegaqs, EVENTDATETIME__gte=labels[i]["fecha"], EVENTDATETIME__lt=labels[i]["fechafin"]).filter(DESTINATION="ZPICADO")
                    cantidad1=filtro.count()
                    #sumo los m2 asociados a cada pallet
                    m2tot=0
                    for mov in filtro:
                        m2tot=m2tot+mov.m2pallet

                    labels[i]["m2DeConvAPicado"]= m2tot



                print("completado, guardando el Model")
                sleep(1)


                #antiguos= Datos_MovPallets.objects.all().delete()

                #print(labels)
                for dato in labels:
                    #print(dato['cantidadIn'])
                    o = Datos_MovPallets.objects.create(programa=foto, fecha=dato['fecha'],fechafin=dato['fechafin'],turno=dato['turno'],label=dato['label'],cantidadIn=dato["cantidadIn"],m2In=dato['m2In'], m2DeConvAPicado=dato['m2DeConvAPicado'], m2EntregadoAConv=dato['m2EntregadoAConv'], cantidadCorrPicado=dato['cantidadCorrPicado'],m2CorrPicado=dato['m2CorrPicado'],cantidadDirectoConv=dato['cantidadDirectoConv'],m2DirectoConv=dato['m2DirectoConv'],cantidadOut=dato['cantidadOut'],m2Out=dato['m2Out'], m2Conv=dato['m2Conv'], m2Corr=dato['m2Corr'])
                    o.save()
                    sleep(0.05)

                print("model guardado")


                #######################################################################
                #### Ahora calculo los datos de sólo los movimientos..
                print("iniciando datos B")

                listaopgruacorr=["1009/Nolasco Carreño","1114/Andres Aguilera","1076/OSCAR  TOLEDO","1010/Héctor  Velasquez", "1026/Danilo Moya", "1027/Jaime Marchant", "1115/Hugo Orostiga"]
                filtroopgruacorrqs=Q()
                for op in listaopgruacorr:
                    filtroopgruacorrqs = filtroopgruacorrqs | Q(OPERATORCODENAME=op)

                listaopgruaconv=["1003/Ignacio Molina", "1086/PATRICIO  CHAVEZ", "1017/Raul Ormeño", "1114/Andres Aguilera", "1087/NIBALDO  LARA", "1025/Patricio  Chavez","1018/Daniel Saavedra", "1002/Carlos Paz", "1017/Raul Ormeño", "-","-"]
                filtroopgruaconvqs=Q()
                for op in listaopgruaconv:
                    filtroopgruaconvqs = filtroopgruaconvqs | Q(OPERATORCODENAME=op)






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

                    #Calculo el n° de movimientos registrados en ese turno:

                    datosop=[[0,"0"]]
                    for op in listaopgruacorr:
                        datosop.append([op , MovPallets.objects.filter( Q(SOURCE="CORR_UPPER_Stacker") | Q(SOURCE="CORR_LOWER_Stacker"), OPERATORCODENAME=op, EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count()])
                    #print(datosop)
                    datosopB=[[0,"0"]]
                    #acá muestro todos los movimientos que han hecho esos operadores.
                    for op in listaopgruaconv:
                        datosopB.append([op , MovPallets.objects.filter( OPERATORCODENAME=op, EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count()])
                    #print(datosop)

                    movscorr1= MovPallets.objects.filter(Q(SOURCE="CORR_UPPER_Stacker") | Q(SOURCE="CORR_LOWER_Stacker") ).filter(EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count()
                    movscorr2= MovPallets.objects.filter(Q(SOURCE="CORR_LOWER_Stacker")).filter(EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count()
                    movsconv1= MovPallets.objects.filter(Q(DESTINATION="TCY") | Q(DESTINATION="HCR")| Q(DESTINATION="WRD")).filter( EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count()
                    movsconv2= MovPallets.objects.filter(Q(DESTINATION="FFW") | Q(DESTINATION="DRO")| Q(DESTINATION="FFG")).filter( EVENTDATETIME__gte=fechaini, EVENTDATETIME__lt=fechafin).count()

                    labels2.append({"fechaini":fechaini,"fechafin":fechafin, "label": label, "movscorr1":movscorr1, "movscorr2":movscorr2, "movsconv1":movsconv1, "movsconv2":movsconv2, "opcorr1":datosop[1][0], "movscorrop1":datosop[1][1], "opcorr2":datosop[2][0], "movscorrop2":datosop[2][1], "opcorr3":datosop[3][0], "movscorrop3":datosop[3][1], "opcorr4":datosop[4][0], "movscorrop4":datosop[4][1], "opcorr5":datosop[5][0], "movscorrop5":datosop[5][1], "opcorr6":datosop[6][0], "movscorrop6":datosop[6][1], "opcorr7":datosop[7][0], "movscorrop7":datosop[7][1], "opconv1":datosopB[1][0], "movsconvop1":datosopB[1][1], "opconv2":datosopB[2][0], "movsconvop2":datosopB[2][1], "opconv3":datosopB[3][0], "movsconvop3":datosopB[3][1], "opconv4":datosopB[4][0], "movsconvop4":datosopB[4][1], "opconv5":datosopB[5][0], "movsconvop5":datosopB[5][1], "opconv6":datosopB[6][0], "movsconvop6":datosopB[6][1], "opconv7":datosopB[7][0], "movsconvop7":datosopB[7][1], "opconv8":datosopB[8][0], "movsconvop8":datosopB[8][1], "opconv9":datosopB[9][0], "movsconvop9":datosopB[9][1], "opconv10":datosopB[10][0], "movsconvop10":datosopB[10][1]})

                print("datos obtenidos correctamente")
                #print(datosopB)
                #print(datosop[1][0])
                for dato in labels2:
                    #print(dato['cantidadIn'])
                    o = Datos_MovPallets_B.objects.create(programa=foto,fechaini=dato['fechaini'],fechafin=dato['fechafin'],label=dato['label'],movscorr1=dato["movscorr1"],movscorr2=dato['movscorr2'],movsconv1=dato['movsconv1'],movsconv2=dato['movsconv2'],opcorr1=dato['opcorr1'],movscorrop1=dato['movscorrop1'],opcorr2=dato['opcorr2'],movscorrop2=dato['movscorrop2'],opcorr3=dato['opcorr3'],movscorrop3=dato['movscorrop3'],opcorr4=dato['opcorr4'],movscorrop4=dato['movscorrop4'],opcorr5=dato['opcorr5'],movscorrop5=dato['movscorrop5'],opcorr6=dato['opcorr6'],movscorrop6=dato['movscorrop6'],opcorr7=dato['opcorr7'],movscorrop7=dato['movscorrop7'],opconv1=dato['opconv1'],movsconvop1=dato['movsconvop1'],opconv2=dato['opconv2'],movsconvop2=dato['movsconvop2'],opconv3=dato['opconv3'],movsconvop3=dato['movsconvop3'],opconv4=dato['opconv4'],movsconvop4=dato['movsconvop4'],opconv5=dato['opconv5'],movsconvop5=dato['movsconvop5'],opconv6=dato['opconv6'],movsconvop6=dato['movsconvop6'],opconv7=dato['opconv7'],movsconvop7=dato['movsconvop7'],opconv8=dato['opconv8'],movsconvop8=dato['movsconvop8'],opconv9=dato['opconv9'],movsconvop9=dato['movsconvop9'],opconv10=dato['opconv10'],movsconvop10=dato['movsconvop10'])
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
    def update_datos_inv_cic(self):

        if 1:
            print("iniciando update datos inventario cíclico")
            try:
                datosWIP={"ZFFG1":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZFFG2":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZDRO1":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZDRO2":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZFFW1":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZFFW2":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZSOB1":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZWRD1":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZWRD2":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZSOB2":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZHCR1":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZHCR2":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZTCY1":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZTCY2":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZPNC":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZPASILLO":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0}}



                tomainv=TomaInvCic.objects.all().order_by('-pk')[0]

                fotoinvcic, created=Foto_Inv_Cic_WIP.objects.get_or_create(fecha_foto=datetime.now())
                fotoinvcic.save()
                #sleep(0.05)


                ####Ahora voy a probar sacando el "enotracalle para ver si es más rápido"
                for calle in datosWIP.keys():

                    print(calle)

                    palletstomainv = PalletCic.objects.filter(ubic=calle, tomainvcic=tomainv)

                    #los pallets que están en esa ubicación según CTI, pero exluyendo los que ya están en palletstomainv
                    palletscti= Pallet.objects.filter(ubic=calle).exclude(tarja__in=[o.tarja for o in palletstomainv]).order_by('tarja')

                    #palletsnoencontrados son los que se pistolearon pero no aparecen en palletsCTI
                    palletsnoencontrados=  PalletCic.objects.filter(ubic=calle, tomainvcic=tomainv).exclude(tarja__in=[o.tarja for o in Pallet.objects.filter(ubic=calle)]).order_by('tarja')
                    palletsencontrados = PalletCic.objects.filter(ubic=calle, tomainvcic=tomainv).exclude(tarja__in=[o.tarja for o in palletsnoencontrados]).order_by('tarja')


                    #print("palletsenotracalle")
                    #print(palletsenotracalle)


                    fotocalle, created =Foto_Calles_Inv_Cic_WIP.objects.get_or_create(foto = fotoinvcic, calle=calle)
                    fotocalle.save()



                    for pallet in palletscti.filter(ubic=calle).order_by('tarja'):

                        ordid="vacío"

                        try:
                            ordid=(Pallet.objects.filter(tarja=pallet.tarja)[0].ORDERID)
                        except:
                            #print("hola")
                            ordid=("vacio")


                        o =Foto_Palletscti_Inv_Cic_WIP.objects.create( calle=fotocalle, pallet=pallet.tarja ,ORDERID=ordid)
                        o.save() #print(pallet[1])



                    for pallet in palletsencontrados.filter(ubic=calle).order_by('tarja'):

                        ordid="vacío"


                        try:
                            ordid=(Pallet.objects.filter(tarja=pallet.tarja)[0].ORDERID)
                        except:
                            #print("hola")
                            ordid=("vacio")


                        o =Foto_Palletsencontrados_Inv_Cic_WIP.objects.create( calle=fotocalle, pallet=pallet.tarja ,ORDERID=ordid)
                        o.save() #print(pallet[1])



                    for pallet in palletsnoencontrados:

                        ordid="vacío"
                        try:
                            ordid=(Pallet.objects.filter(tarja=pallet.tarja)[0].ORDERID)
                        except:
                            #print("hola")
                            ordid=("vacio")

                        o =Foto_Palletsnoencontrados_Inv_Cic_WIP.objects.create( calle=fotocalle, pallet=pallet.tarja ,ORDERID=ordid)
                        o.save() #print(pallet[1])


                    ultimatoma=(tomainv.fechatomainvcic).strftime("%m/%d/%Y %H:%M:%S")

                instance=Foto_Inv_Cic_WIP.objects.filter(fecha_foto__lt=fotoinvcic.fecha_foto)
                instance.delete()

                #print(datosWIP)
                print(ultimatoma)
                #sleep(1)
            except Exception as e:
                print(e)
                print("error!")
                sleep(10)


    def handle(self, *args, **options):
        while (1):

            try:
                self.updatemovpallets()
                self.update_datos_inv_cic()
                self.update_datos_wip()
                self.updatewipprog()
                self.updateproywip()

            except Exception as e:
                print(e)
                print("error, posiblemente database is locked??")
                sleep(10)



            ###########


            print("Esperando para hacer prox carga masiva de datos")
            sleep(2)
        #print(labels)
