from django.core.management.base import BaseCommand, CommandError
from blog.models import OrdenCorrplan as OrdenCorrplan
from blog.models import FotoCorrplan as FotoCorrplan
from blog.models import FotoProgCorr as FotoProgCorr
from blog.models import Datos_Proy_WIP as Datos_Proy_WIP
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
        ###########

        #Primero saco el dato del programa de corrugado:
        while (1):
            if 1:
                prog_corrugado = webscrap3.webscrap_prog_corr()


                foto, created =FotoProgCorr.objects.get_or_create(fecha_foto=datetime.now())
                foto.save()
                instance=FotoProgCorr.objects.filter(fecha_foto__lt=foto.fecha_foto)
                instance.delete()

                #Borrar los antiguos..

                fecha_fin_anterior=0
                for prog in prog_corrugado:
                    #transformando el dato de fecha a datetime
                    #print(prog)

                    fechafin=datetime.strptime(prog[6], '%d-%m %H:%M')
                    fechafin=fechafin.replace(year= datetime.now().year)
                    print(fechafin)

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
                    id.save()
                    fecha_fin_anterior = id.fecha_fin
                    print(id)



                #########

                sleep(3)

                #Ahora actualizo los datos del panel de proyección.

                "hago lista de fechas que quiero mostrar:" #basado en el get_data_mov_pallets pero genera las fechas a futuro. Como texto y como datetime
                labels=[]#fechas, será el label del gráfico
                ahora=datetime.now()
                ahorafix=ahora.replace(hour= 0, minute=0, second=0, microsecond=0)
                for i in range(0,2):
                    #por ahora los voy a ordenar por turno, después por hora.
                    fecha=(ahorafix+timedelta(days=i)).replace(hour= 7)
                    turno="A"
                    label= fecha.strftime("%d-%m") + " " + turno
                    if ahora<=(ahorafix+timedelta(days=i)).replace(hour= 14, minute=30):
                        labels.append({"fecha":fecha ,"turno":turno, "label": label})

                    fecha=(ahorafix+timedelta(days=i)).replace(hour= 14, minute=30)
                    turno="B"
                    label= fecha.strftime("%d-%m") + " " + turno
                    if ahora<=(ahorafix+timedelta(days=i)).replace(hour= 22):
                        labels.append({"fecha":fecha ,"turno":turno, "label": label})

                    fecha=(ahorafix+timedelta(days=i)).replace(hour= 22)
                    turno="C"
                    label= fecha.strftime("%d-%m") + " " + turno
                    if ahora<=(ahorafix+timedelta(days=i+1)).replace(hour= 7):
                        labels.append({"fecha":fecha,"turno":turno, "label": label})

                #Ahora, por cada label, calculo la suma de Mm2 de conversión que se iniciarán en ese turno según corrplan


                #calculo el inventario inicial a la fecha en el WIP:
                invtotwip=0
                for pallet in Pallet.objects.filter( Q(ubic="ZFFG1") | Q(ubic="ZFFG2")| Q(ubic="ZFFW1")| Q(ubic="ZFFW2")| Q(ubic="ZDRO1")| Q(ubic="ZDRO2")| Q(ubic="ZTCY1") | Q(ubic="ZTCY2")| Q(ubic="ZWRD1")| Q(ubic="ZWRD2")| Q(ubic="ZHCR1")| Q(ubic="ZHCR2")| Q(ubic="ZSOB1") | Q(ubic="ZSOB2") | Q(ubic="ZPASILLO")):
                #        if pallet.ORDERID != order.order_id:
                    invtotwip=invtotwip+(pallet.m2pallet/1000)



                fecha_anterior=0
                for fechaturno in labels:
                    #print(fechaturno['fecha'])


                    if fecha_anterior==0:
                        fecha_anterior=datetime.now()



                    filtro=OrdenCorrplan.objects.filter(fecha_inicio__gte=fecha_anterior, fecha_inicio__lt=fechaturno['fecha'])
                    sumaM2=0
                    for orden in filtro:
                        sumaM2=sumaM2 + orden.area
                    #print(sumaM2)

                    fechaturno["M2Conv"]=sumaM2




                    filtrocorr=IDProgCorr.objects.filter(fecha_inicio__gte=fecha_anterior, fecha_inicio__lt=fechaturno['fecha'])
                    sumaM2=0

                    for orden in filtrocorr:

                        sumaM2=sumaM2 + (orden.area)

                    fechaturno["M2Corr"]=sumaM2



                    fecha_anterior=fechaturno['fecha']


                    invtotwip=invtotwip+int(fechaturno["M2Corr"])-int(fechaturno["M2Conv"])


                    fechaturno["M2Inv"]=invtotwip


                antiguos= Datos_Proy_WIP.objects.all().delete()



                for dato in labels:

                    o = Datos_Proy_WIP.objects.create(fecha=dato['fecha'],turno=dato['turno'],label=dato['label'],M2Conv=dato['M2Conv'],M2Corr=dato['M2Corr'],M2Inv=dato['M2Inv'])
                    o.save()
            #except:
            #    print("error")

            sleep(60)
        #print(labels)
