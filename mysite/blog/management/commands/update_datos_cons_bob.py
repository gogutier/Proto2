from django.core.management.base import BaseCommand, CommandError
from blog.models import OrdenCorrplan as OrdenCorrplan
from blog.models import FotoCorrplan as FotoCorrplan
from blog.models import Cartones as Cartones
from blog.models import Maquinas as Maquinas
from blog.models import ConsumoRollos as ConsumoRollos
from blog.models import Foto_ConsumoRollos as Foto_ConsumoRollos

from django.utils import timezone
from datetime import datetime, timedelta
from time import time, sleep

import pruebaAPIRollCons



class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)
        poll_id="hola"

    def handle(self, *args, **options):

        while(1):
            try:

                ##Calculo los turnos que quiero actualizar.
                labels=[]
                ahora=datetime.now().replace(hour= 0, minute=0, second=0, microsecond=0)
                for i in range(0,7):
                    #por ahora los voy a ordenar por turno, después por hora.
                    fechaini=(ahora-timedelta(days=7-i)).replace(hour= 7)
                    fechafin=(ahora-timedelta(days=7-i)).replace(hour= 14, minute=30)
                    turno="A"
                    label= fechaini.strftime("%d-%m") + " " + turno
                    #calculo el m2 real convertido y corrugado en ese turno, para comparar con las salidas y entradas declaradas

                    #print(m2Corr)
                    labels.append({"fechaini":fechaini ,"fechafin":fechafin ,"turno":turno, "label": label})

                    fechaini=(ahora-timedelta(days=7-i)).replace(hour= 14, minute=30)
                    fechafin=(ahora-timedelta(days=7-i)).replace(hour= 22)
                    turno="B"
                    label= fechaini.strftime("%d-%m") + " " + turno

                    #print(m2Corr)
                    labels.append({"fechaini":fechaini ,"fechafin":fechafin ,"turno":turno, "label": label})

                    fechaini=(ahora-timedelta(days=7-i)).replace(hour= 22)
                    fechafin=(ahora-timedelta(days=7-i-1)).replace(hour= 7)
                    turno="C"
                    label= fechaini.strftime("%d-%m") + " " + turno
                    labels.append({"fechaini":fechaini ,"fechafin":fechafin ,"turno":turno, "label": label})

                print("ahora calculo las listas de lo que se declaró como ingreso y como salida al wip  ")

                for label in labels:
                    print(label['label'])
                    consumos=pruebaAPIRollCons.cargaconsbob(label['fechaini'],label['fechafin'])


                    foto, created =Foto_ConsumoRollos.objects.get_or_create(fecha_foto=ahora, label=label['label'], turno=label['turno'])
                    foto.save()




                    for consumo in consumos:
                        print(consumo['RollID'])

                        o, created= ConsumoRollos.objects.get_or_create(foto= foto, RollID=consumo['RollID'],RollStandID=consumo['RollStandID'],formato=consumo['formato'],peso=consumo['peso'],grado=consumo['grado'],diametro=consumo['diametro'],mlusados=consumo['mlusados'],mlrestantes=consumo['mlrestantes'], peelwaste=consumo['peelwaste'], turno=label['turno'],fechaini=label['fechaini'])
                        o.save()


                    instance=Foto_ConsumoRollos.objects.filter(fecha_foto__lt=foto.fecha_foto, turno=label['label'])
                    instance.delete()

                    sleep(2)





                #print(consumos)
                print("TODO LISTOOOO")
                sleep(360)
            except Exception as e:
                print(e)
                print("error!")
