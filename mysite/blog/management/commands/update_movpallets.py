from django.core.management.base import BaseCommand, CommandError
from blog.models import OrdenCorrplan as OrdenCorrplan
from blog.models import FotoCorrplan as FotoCorrplan
from blog.models import FotoProgCorr as FotoProgCorr
from blog.models import Datos_Proy_WIP as Datos_Proy_WIP
from blog.models import MovPallets as MovPallets
from blog.models import Datos_MovPallets as Datos_MovPallets
from blog.models import IDProgCorr as IDProgCorr
from blog.models import Pallet as Pallet
from blog.models import Cartones as Cartones
from blog.models import Maquinas as Maquinas

from django.db.models import Q
import webscrap3

from django.utils import timezone
from datetime import datetime, timedelta
from time import time, sleep



class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)
        poll_id="hola"

    def handle(self, *args, **options):

        #muestra evolución de últimas horas de cuántos pallets entraron a WIP y cuántos salieron (m2 y unidades)
        #entrega datos para armar gráfico.
        #como referencia, el de WIP.

        labels=[]
        ahora=timezone.now().replace(hour= 0, minute=0, second=0, microsecond=0)
        for i in range(0,8):
            #por ahora los voy a ordenar por turno, después por hora.
            fecha=(ahora-timedelta(days=7-i)).replace(hour= 7)
            turno="A"
            label= fecha.strftime("%d-%m") + " " + turno
            labels.append({"fecha":fecha ,"turno":turno, "label": label})

            fecha=(ahora-timedelta(days=7-i)).replace(hour= 14, minute=30)
            turno="B"
            label= fecha.strftime("%d-%m") + " " + turno
            labels.append({"fecha":fecha ,"turno":turno, "label": label})

            fecha=(ahora-timedelta(days=7-i)).replace(hour= 22)
            turno="C"
            label= fecha.strftime("%d-%m") + " " + turno
            labels.append({"fecha":fecha ,"turno":turno, "label": label})

        #ahpra por cada labe[] le anexo el dato de los m2 de entrada.

        listafiltroproducido=["CORR_UPPER_Stacker", "CORR_LOWER_Stacker"]
        listafiltroentrada=["ZTCY1","ZTCY2","ZHCR1","ZHCR2","ZWRD1","ZWRD2","ZFFW1","ZFFW2","ZDRO1","ZDRO2","ZFFG1","ZFFG2","ZSOB1","ZSOB2","ZPNC","ZPASILLO"]
        listafiltrosalida=["TCY","HCR","WRD","FFW","DRO","FFG","ZPICADO"]

        filtroproducidoqs=Q()

        filtroentradaqs=Q()
        filtrosalidaqs=Q()

        for item in listafiltroproducido:
            filtroproducidoqs = filtroproducidoqs | Q(DESTINATION=item)

        for item in listafiltroentrada:
            filtroentradaqs = filtroentradaqs | Q(DESTINATION=item)

        for item in listafiltrosalida:
            filtrosalidaqs = filtrosalidaqs | Q(DESTINATION=item)

        for i in range(0,len(labels)-1):

            #Entradas
            filtro=MovPallets.objects.filter(filtroentradaqs, EVENTDATETIME__gte=labels[i]["fecha"], EVENTDATETIME__lt=labels[i+1]["fecha"])
            cantidad1=filtro.count()
            #sumo los m2 asociados a cada pallets
            m2tot=0
            for mov in filtro:
                m2tot=m2tot+mov.m2pallet

            labels[i]["cantidadIn"]= cantidad1
            labels[i]["m2In"]= m2tot



            #Producidos pero excluyendo los pallets que ya están en la lista de Entradas (acá saco el m2 actualizado de cada pallet, para descartar las producciones que se fueron a cero)
            filtro2=MovPallets.objects.filter(filtroproducidoqs, EVENTDATETIME__gte=labels[i]["fecha"], EVENTDATETIME__lt=labels[i+1]["fecha"])


            for item in filtro:
                filtro2=filtro2.exclude(LOADID=item.LOADID)


            cantidad1=filtro2.count()
            #sumo los m2 asociados a cada pallets
            m2tot=0
            for mov in filtro2:
                #print(str(mov) + ".." + str(mov.LOADID) )
                try:
                    m2tot=m2tot+Pallet.objects.get(tarja=mov.LOADID).m2pallet
                except:
                    print("error con " + str(mov) + ".." + str(mov.LOADID) + "!!")


            labels[i]["cantidadProd"]= cantidad1
            labels[i]["m2Prod"]= m2tot


            #Salidas
            filtro=MovPallets.objects.filter(filtrosalidaqs, EVENTDATETIME__gte=labels[i]["fecha"], EVENTDATETIME__lt=labels[i+1]["fecha"])
            cantidad1=filtro.count()
            #sumo los m2 asociados a cada pallet
            m2tot=0
            for mov in filtro:
                m2tot=m2tot+mov.m2pallet

            labels[i]["cantidadOut"]= cantidad1
            labels[i]["m2Out"]= m2tot





        #este es el último item de cada lista (como termina donde empieza el siguiente no funciona dentro del for)


        #Entrada
        filtro=MovPallets.objects.filter(filtroentradaqs, EVENTDATETIME__gte=labels[len(labels)-1]["fecha"])
        cantidad1=filtro.count()


        m2tot=0
        for mov in filtro:
            m2tot=m2tot+mov.m2pallet

        labels[len(labels)-1]["cantidadIn"]= cantidad1
        labels[len(labels)-1]["m2In"]= m2tot



        #Producido no ingresado
        filtro2=MovPallets.objects.filter(filtroproducidoqs, EVENTDATETIME__gte=labels[len(labels)-1]["fecha"])


        for item in filtro:
            filtro2=filtro2.exclude(LOADID=item.LOADID)



        cantidad1=filtro2.count()


        m2tot=0
        for mov in filtro2:
            m2tot=m2tot+Pallet.objects.get(tarja=mov.LOADID).m2pallet

        labels[len(labels)-1]["cantidadProd"]= cantidad1
        labels[len(labels)-1]["m2Prod"]= m2tot


        #Salida
        filtro=MovPallets.objects.filter(filtrosalidaqs, EVENTDATETIME__gte=labels[len(labels)-1]["fecha"])
        cantidad1=filtro.count()

        m2tot=0
        for mov in filtro:
            m2tot=m2tot+mov.m2pallet


        labels[len(labels)-1]["cantidadOut"]= cantidad1
        labels[len(labels)-1]["m2Out"]= m2tot

        antiguos= Datos_MovPallets.objects.all().delete()

        print(labels)
        for dato in labels:
            o = Datos_MovPallets.objects.create(fecha=dato['fecha'],turno=dato['turno'],label=dato['label'],cantidadIn=dato['cantidadIn'],m2In=dato['m2In'],cantidadProd=dato['cantidadProd'],m2Prod=dato['m2Prod'],cantidadOut=dato['cantidadOut'],m2Out=dato['m2Out'])
            o.save()
