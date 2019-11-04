from django.core.management.base import BaseCommand, CommandError
from blog.models import FotoCorrplan as FotoProgCorr
from blog.models import FotoCorrplan as IDProgCorr

from django.utils import timezone
from datetime import datetime, timedelta

import webscrap3

    def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)
        poll_id="hola"

    def handle(self, *args, **options):
        prog_corrugado = webscrap3.webscrap_prog_corr()


        foto, created =FotoProgCorr.objects.get_or_create(fecha_foto=fechfot)
        foto.save()

        for prog in prog_corrugado:
            #transformando el dato de fecha a datetime
            print(prog[5])

        '''
        for i in (1,len(prog_corrugado)):
            #supuesto: La primera fila nunca es una en proceso.
            id, created =FotoProgCorr.objects.get_or_create(programa=foto)
            id.color=prog_corrugado[i][0]
            id.fecha_inicio=prog_corrugado[i-1][]
            id.fecha_fin
            id.order_id
            id.ancho
            id.refile
            id.metrosL
            id.carton


            prog.save()
        '''
