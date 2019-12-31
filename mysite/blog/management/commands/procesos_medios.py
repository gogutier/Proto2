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

            self.update_datos_inv_cic()
