from django.core.management.base import BaseCommand, CommandError

from blog.models import OrdenCorrplan as OrdenCorrplan
from blog.models import FotoProgCorr as FotoProgCorr
from blog.models import FotoCorrplan as FotoCorrplan
from blog.models import TomaInvCic as TomaInvCic
from blog.models import PalletCic as PalletCic
from blog.models import MovPallets as MovPallets
from blog.models import Pallet as Pallet
from blog.models import ConsumoRollos as ConsumoRollos
from blog.models import Foto_ConsumoRollos as Foto_ConsumoRollos
from blog.models import Foto_Datos_MovPallets as Foto_Datos_MovPallets
from blog.models import IDProgCorr as IDProgCorr
from blog.models import Cartones as Cartones
from blog.models import Maquinas as Maquinas
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

import pruebaAPIRollCons
import webscrap2



class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)
        poll_id="hola"
    def updateconsbobs(self):
        if 1:
            print("iniciando carga de consumo de rollos")
            sleep(5)
            try:

                ##Calculo los turnos que quiero actualizar.
                labels=[]
                ahora=datetime.now().replace(hour= 0, minute=0, second=0, microsecond=0)
                horizonte=37
                for i in range(0,horizonte):
                    #por ahora los voy a ordenar por turno, después por hora.
                    fechaini=(ahora+timedelta(days=1)-timedelta(days=horizonte-i)).replace(hour= 7)
                    fechafin=(ahora+timedelta(days=1)-timedelta(days=horizonte-i)).replace(hour= 14, minute=30)
                    turno="A"
                    label= fechaini.strftime("%d-%m") + " " + turno
                    #calculo el m2 real convertido y corrugado en ese turno, para comparar con las salidas y entradas declaradas

                    #print(m2Corr)
                    labels.append({"fechaini":fechaini ,"fechafin":fechafin ,"turno":turno, "label": label})

                    fechaini=(ahora+timedelta(days=1)-timedelta(days=horizonte-i)).replace(hour= 14, minute=30)
                    fechafin=(ahora+timedelta(days=1)-timedelta(days=horizonte-i)).replace(hour= 22)
                    turno="B"
                    label= fechaini.strftime("%d-%m") + " " + turno

                    #print(m2Corr)
                    labels.append({"fechaini":fechaini ,"fechafin":fechafin ,"turno":turno, "label": label})

                    fechaini=(ahora+timedelta(days=1)-timedelta(days=horizonte-i)).replace(hour= 22)
                    fechafin=(ahora+timedelta(days=1)-timedelta(days=horizonte-i-1)).replace(hour= 7)
                    turno="C"
                    label= fechaini.strftime("%d-%m") + " " + turno
                    labels.append({"fechaini":fechaini ,"fechafin":fechafin ,"turno":turno, "label": label})



                for label in labels:
                    print("busco el consumo en cada turno: ")
                    print(label['label'])
                    print(label['fechaini'])
                    print(label['fechafin'])
                    consumos=pruebaAPIRollCons.cargaconsbob(label['fechaini'],label['fechafin'])

                    #print(consumos)


                    foto, created =Foto_ConsumoRollos.objects.get_or_create(fecha_foto=ahora, label=label['label'], turno=label['turno'])
                    foto.save()




                    for consumo in consumos:
                        #print(consumo['RollID'])

                        o, created= ConsumoRollos.objects.get_or_create(foto= foto, RollID=consumo['RollID'],RollStandID=consumo['RollStandID'],formato=consumo['formato'],peso=consumo['peso'],grado=consumo['grado'],diametro=consumo['diametro'],mlusados=consumo['mlusados'],mlrestantes=consumo['mlrestantes'], peelwaste=consumo['peelwaste'], turno=label['turno'],fechaini=label['fechaini'])
                        o.save()
                        #sleep(0.1)


                    instance=Foto_ConsumoRollos.objects.filter(fecha_foto__lt=foto.fecha_foto, label=label['label'])
                    instance.delete()

                    sleep(2)

            except Exception as e:
                print(e)
                print("error al consumir bobinas!!!")
                sleep(15)



            #print(consumos)
            print("TODO LISTOOOO, consumos bobinas actualizados!")
            sleep(120)

    def updatecorrplan(self):
        try:
            tini=timezone.now()
            fechfot=datetime.now()#timezone.now()
            self.stdout.write("cargando datos corrplan")
            foto_corrplan = webscrap2.webscrap_corrplan()
                    ## [N° máquina, n° piezas, Area]
            self.stdout.write("preparandose para copiar datos corrplan en BD")#Esto debería checkear también si fué un éxito la toma de datos del webscrap.
            #Creo Primero el Foto CorrPlan
            tfin=timezone.now()
            duracion= tfin-tini
            durac=str(duracion)
            foto, created =FotoCorrplan.objects.get_or_create(fecha_foto=fechfot, usuario_foto="userdefault", tiempo_carga=durac)
            foto.save()
            #creo despuès los ordercorrplan asociado al ùltimo FotoCorrplan creado.
            self.stdout.write("leyendo filas")
            for fila in foto_corrplan:
                #ord_corrplan, created =OrdenCorrplan.objects.get_or_create(programa=foto)
                #pasar la fecha comprometida a datetime y guardarla
                fecha_entrega= datetime.strptime(str(fila[0]), '%d-%m-%Y')
                #continùa guardando sòlo si la fecha de entrega està dentro del rango establecido.
                try:#fecha_entrega < datetime.now() + timedelta(days=10):
                    try:
                        fecha_inicio= datetime.strptime(str(fila[1]), '%d-%m-%Y %H:%M:%S') #ojo, hay que agregarle el timezone, para que no sea "naive"
                    except:
                        try:
                            fecha_inicio= datetime.strptime(str(fila[1]), '%d-%m-%Y') #ojo, hay que agregarle el timezone, para que no sea "naive"
                        except: #este es el caso en que hayan ordenes de estado "Nueva", las cuales todavìa no tienen fecha real asignada en màquina.
                            fecha_inicio= datetime.strptime("1-01-2900", '%d-%m-%Y') #ojo, hay que agregarle el timezone, para que no sea "naive"

                    order_id= (fila[2])
                    cliente= (fila[3])
                    SO= (fila[4])
                    carton = (fila[5])
                    padron = (fila[6])
                    cant_ord = int(fila[7])
                    cant_corr = int(fila[8])
                    medida = (fila[9])
                    area = float(fila[10])
                    ruta = (fila[11])
                    estado = (fila[12])
                    if fila[13]=="Yes":
                        comprometida = True
                    else:
                        comprometida = False

                    #detectando la màquina a la que corresponde:
                    #print(fila[11])
                    if fila[11].find("FFG WARD")>=0:
                        maq, created =Maquinas.objects.get_or_create(maquina="FFW")
                    elif fila[11].find("WARD")>=0:
                        maq, created =Maquinas.objects.get_or_create(maquina="WRD")
                    elif fila[11].find("Flexo Martin")>=0:
                        maq, created =Maquinas.objects.get_or_create(maquina="FFG")
                    elif fila[11].find("HYCORR")>=0:
                        maq, created =Maquinas.objects.get_or_create(maquina="HCR")
                    elif fila[11].find("TCY")>=0:
                        maq, created =Maquinas.objects.get_or_create(maquina="TCY")
                    elif fila[11].find("DRO")>=0:
                        maq, created =Maquinas.objects.get_or_create(maquina="DRO")
                    else:
                        maq, created =Maquinas.objects.get_or_create(maquina="vacio")
                        print(fila[11])
                    #maquina = ("pendiente") #pendiente de sacar en base a la ruta (ùltim màquina de la ruta?)

                    flagok=0
                    while flagok==0:
                        try:
                            ord_corrplan, created =OrdenCorrplan.objects.get_or_create(programa=foto, fecha_entrega=fecha_entrega, fecha_inicio=fecha_inicio, order_id=order_id, cliente=cliente, SO=SO, carton=carton, padron=padron, cant_ord=cant_ord, cant_corr=cant_corr, medida=medida, area=area, ruta=ruta, estado=estado, comprometida=comprometida, maquina=maq  ) #usò siempre la misma :/
                            ord_corrplan.save()
                            flagok=1
                            sleep(0.1)
                        except Exception as e:
                            print(e)
                            print("error al guardar fila corrplan en sistema")

                    #acà podrìa intenar borrar los foto corrplan antiguos para no acumular tantos datos.
                    ##Agregar la parte que borra todos los corrplans anteriores (se borró)
                    #borrando todas las fotos corrplan anteriores a "foto"


                    cartin, created =Cartones.objects.get_or_create(carton=fila[5])
                    cartin.save()
                except Exception as e:
                    print(e)
                    print("error al copiar una orden de corrplan")
                    sleep(15)

                instance=FotoCorrplan.objects.filter(fecha_foto__lt=foto.fecha_foto)
                instance.delete()
                #self.stdout.write(fila[0][4])
            self.stdout.write("Datos actualizados")
            sleep(15)
        except Exception as e:
            print(e)
            print("error")
            sleep(15)





    def handle(self, *args, **options):

        while (1):

            self.updatecorrplan()
            self.updateconsbobs()
