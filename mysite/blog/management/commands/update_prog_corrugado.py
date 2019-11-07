from django.core.management.base import BaseCommand, CommandError
from blog.models import FotoProgCorr as FotoProgCorr
from blog.models import IDProgCorr as IDProgCorr

from django.utils import timezone
from datetime import datetime, timedelta
from time import time, sleep

import webscrap3
class Command(BaseCommand):
    def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)
        poll_id="hola"

    def handle(self, *args, **options):
        if(1):


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


        
