from django.core.management.base import BaseCommand, CommandError
from blog.models import OrdenCorrplan as OrdenCorrplan
from blog.models import FotoCorrplan as FotoCorrplan
from blog.models import FotoProgCorr as FotoProgCorr
from blog.models import Datos_Proy_WIP as Datos_Proy_WIP
from blog.models import Foto_Datos_Inv_WIP as Foto_Datos_Inv_WIP
from blog.models import Datos_Inv_WIP as Datos_Inv_WIP
from blog.models import MovPallets as MovPallets
from blog.models import Datos_MovPallets as Datos_MovPallets
from blog.models import IDProgCorr as IDProgCorr
from blog.models import UbicPallet as UbicPallet
from blog.models import FiltroEntradaWIP as FiltroEntradaWIP
from blog.models import FiltroSalidaWIP as FiltroSalidaWIP
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

        datosWIP={"ZFFG1":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":36,"al2":45,"al3":52},"ZFFG2":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":36,"al2":45,"al3":52},"ZDRO1":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":36,"al2":45,"al3":52},"ZDRO2":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":36,"al2":45,"al3":52},"ZFFW1":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":36,"al2":45,"al3":53},"ZFFW2":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":36,"al2":45,"al3":52},"ZSOB1":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":36,"al2":45,"al3":52},"ZWRD1":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":25,"al2":30,"al3":35},"ZWRD2":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":25,"al2":30,"al3":35},"ZSOB2":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":36,"al2":45,"al3":52},"ZHCR1":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":30,"al2":38,"al3":45},"ZHCR2":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":30,"al2":38,"al3":45},"ZTCY1":{"cuenta":0,"dias":0,"m2tot":0,"dias":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},"ZTCY2":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":31,"al2":37,"al3":44},"ZPNC":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":10,"al2":20,"al3":30},"CORR_UPPER_Stacker":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":1,"al2":2,"al3":3},"CORR_LOWER_Stacker":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":1,"al2":2,"al3":3},"ZPASILLO":{"cuenta":0,"m2tot":0,"indice":0,"dias":0,"al1":1,"al2":2,"al3":3}}

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
        filtro=MovPallets.objects.filter(Q(DESTINATION="ZPNC") | Q(DESTINATION="ZHCR1") | Q(DESTINATION="ZHCR2")| Q(DESTINATION="ZTCY1")| Q(DESTINATION="ZTCY2")| Q(DESTINATION="ZWRD1")| Q(DESTINATION="ZWRD2")| Q(DESTINATION="ZSOB1")| Q(DESTINATION="ZSOB2")| Q(DESTINATION="ZFFW1")| Q(DESTINATION="ZFFW2")| Q(DESTINATION="ZDRO1")| Q(DESTINATION="ZDRO2")| Q(DESTINATION="ZFFG1")| Q(DESTINATION="ZFFG2")| Q(DESTINATION="ZPNC")| Q(DESTINATION="ZPASILLO") ).exclude( Q(SOURCE="ZPNC") | Q(SOURCE="ZHCR1") | Q(SOURCE="ZHCR2")| Q(SOURCE="ZTCY1")| Q(SOURCE="ZTCY2")| Q(SOURCE="ZWRD1")| Q(SOURCE="ZWRD2")| Q(SOURCE="ZSOB1")| Q(SOURCE="ZSOB2")| Q(SOURCE="ZFFW1")| Q(SOURCE="ZFFW2")| Q(SOURCE="ZDRO1")| Q(SOURCE="ZDRO2")| Q(SOURCE="ZFFG1")| Q(SOURCE="ZFFG2")| Q(SOURCE="ZPNC")| Q(SOURCE="ZPASILLO")).order_by('-TRANSACTIONINDEX')[:4]

        # referencia: datetime.strptime(datoprocesado[1][colFecha], "%d-%m-%Y %H:%M")

        for mov in filtro:
            #movimiento=[tarja, destino, hora]
            movimiento=[mov.LOADID, mov.ORDERID, mov.DESTINATION, mov.EVENTDATETIME.strftime("%d-%m-%y %H:%M:%S")]
            filtroentrada.append(movimiento)

        #print(filtroentrada)
        filtrosalida=[]
        filtro2=MovPallets.objects.filter(Q(DESTINATION="FFG") | Q(DESTINATION="FFW") | Q(DESTINATION="TCY")| Q(DESTINATION="HCR")| Q(DESTINATION="DRO")| Q(DESTINATION="WRD") | Q(DESTINATION="DIM")| Q(DESTINATION="TAB") | Q(DESTINATION="ZPICADO")| Q(DESTINATION="PLL") ).order_by('-TRANSACTIONINDEX')[:4]

        for mov in filtro2:
            #movimiento=[tarja, destino, hora]
            movimiento=[mov.LOADID, mov.ORDERID, mov.DESTINATION, mov.EVENTDATETIME.strftime("%d-%m-%y %H:%M:%S")]
            filtrosalida.append(movimiento)


        print(filtroentrada)
        print(filtrosalida)

        print("Pasando objetos: ")



        foto, created =Foto_Datos_Inv_WIP.objects.get_or_create(fecha_foto=datetime.now())
        foto.save()
        #Borrar los antiguos..
        instance=Foto_Datos_Inv_WIP.objects.filter(fecha_foto__lt=foto.fecha_foto)
        instance.delete()

        #filtroentrada:

        for mov in filtroentrada:

            dato, created =FiltroEntradaWIP.objects.get_or_create(programa=foto, LOADID=mov[0], ORDERID=mov[1], DESTINATION=mov[2], EVENTDATETIME=mov[3])
            dato.save()

        for mov in filtrosalida:

            dato, created =FiltroSalidaWIP.objects.get_or_create(programa=foto, LOADID=mov[0], ORDERID=mov[1], DESTINATION=mov[2], EVENTDATETIME=mov[3])
            dato.save()


        #sectores:
        for calle in datosWIP.keys():

            dato, created =Datos_Inv_WIP.objects.get_or_create(programa=foto, sector=str(calle), cuenta=datosWIP[str(calle)]['cuenta'], m2tot=datosWIP[str(calle)]['m2tot'], indice=datosWIP[str(calle)]['indice'], dias=datosWIP[str(calle)]['dias'], al1=datosWIP[str(calle)]['al1'], al2=datosWIP[str(calle)]['al2'], al3=datosWIP[str(calle)]['al3'])
            dato.save()



        print("Enviando datos inventario")
