from django.core.management.base import BaseCommand, CommandError
from blog.models import DatosWIP_Prog as DatosWIP_Prog
from blog.models import OrdenCorrplan as OrdenCorrplan
from blog.models import Maquinas as Maquinas
from blog.models import Pallet as Pallet
from django.db.models import Q

from datetime import datetime, timedelta




class Command(BaseCommand):

    def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)
        poll_id="hola"

    def handle(self, *args, **options):

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
