from django.core.management.base import BaseCommand, CommandError

from blog.models import TomaInvCic as TomaInvCic
from blog.models import PalletCic as PalletCic
from blog.models import MovPallets as MovPallets
from blog.models import Pallet as Pallet
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

    def handle(self, *args, **options):

        while (1):

            try:
                datosWIP={"ZFFG1":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZFFG2":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZDRO1":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZDRO2":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZFFW1":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZFFW2":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZSOB1":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZWRD1":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZWRD2":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZSOB2":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZHCR1":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZHCR2":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZTCY1":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZTCY2":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZPNC":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0},"ZPASILLO":{"cuentaenc":0,"cuentanoenc":0,"cuentacti":0}}



                tomainv=TomaInvCic.objects.all().order_by('-pk')[0]

                fotoinvcic, created=Foto_Inv_Cic_WIP.objects.get_or_create(fecha_foto=datetime.now())
                fotoinvcic.save()



                for calle in datosWIP.keys():

                    print(calle)

                    palletstomainv = PalletCic.objects.filter(ubic=calle, tomainvcic=tomainv)

                    #los pallets que están en esa ubicación según CTI, pero exluyendo los que ya están en palletstomainv
                    palletscti= Pallet.objects.filter(ubic=calle).exclude(tarja__in=[o.tarja for o in palletstomainv]).order_by('tarja')

                    #palletsnoencontrados son los que se pistolearon pero no aparecen en palletsCTI
                    palletsnoencontrados=  PalletCic.objects.filter(ubic=calle, tomainvcic=tomainv).exclude(tarja__in=[o.tarja for o in Pallet.objects.filter(ubic=calle)]).order_by('tarja')

                    #hago grupo de calles a excluir
                    palletsCTIenotracalle = Pallet.objects.all().exclude(ubic=calle).order_by('tarja')
                    tarjasnot=[]

                    for aux in palletsCTIenotracalle:
                        tarjasnot.append(aux.tarja)

                    palletsenotracalle=[[],[]]

                    for aux in PalletCic.objects.filter(ubic=calle, tomainvcic=tomainv).order_by('tarja'):
                        if aux.tarja in tarjasnot:
                            palletsenotracalle[0].append(aux.tarja)

                            try:
                                palletsenotracalle[1].append(Pallet.objects.filter(tarja=aux.tarja)[0].ORDERID)
                            except:
                                #print("hola")
                                palletsenotracalle[1].append("vacio")

                    datosWIP[calle]['palletsenotracalle'] = palletsenotracalle
                    #print("palletsenotracalle")
                    #print(palletsenotracalle)


                    palletsencontrados = PalletCic.objects.filter(ubic=calle, tomainvcic=tomainv).exclude(tarja__in=[o.tarja for o in palletsnoencontrados]).order_by('tarja')



                    #palletsnoencontrados= palletsnoencontrados.exclude(tarja__in=[o.tarja for o in palletsenotracalle]).order_by('tarja')

                    lista=[[],[]]

                    for pallet in palletscti.filter(ubic=calle).order_by('tarja'):

                        lista[0].append(pallet.tarja)

                        try:
                            lista[1].append(Pallet.objects.filter(tarja=pallet.tarja)[0].ORDERID)
                        except:
                            #print("hola")
                            lista[1].append("vacio")

                    datosWIP[calle]['palletscti'] = lista
                    #print('palletscti')
                    #print(datosWIP[calle]["palletscti"])

                    lista=[[],[]]

                    for pallet in palletsencontrados.filter(ubic=calle).order_by('tarja'):

                        lista[0].append(pallet.tarja)

                        try:
                            lista[1].append(Pallet.objects.filter(tarja=pallet.tarja)[0].ORDERID)
                        except:
                            #print("hola")
                            lista[1].append("vacio")

                    datosWIP[calle]['palletsencontrados'] = lista


                    lista=[[],[]]

                    for pallet in palletsnoencontrados:

                        if (pallet.tarja not in palletsenotracalle[0]):
                            lista[0].append(pallet.tarja)

                            try:
                                lista[1].append(Pallet.objects.filter(tarja=pallet.tarja)[0].ORDERID)
                            except:
                                #print("hola")
                                lista[1].append("vacio")

                    datosWIP[calle]['palletsnoencontrados'] = lista




                    fotocalle, created =Foto_Calles_Inv_Cic_WIP.objects.get_or_create(foto = fotoinvcic, calle=calle)
                    fotocalle.save()

                    for i in range(0,len(datosWIP[calle]['palletscti'][0])):
                        #print (str(datosWIP[calle]['palletscti'][0][i]) + " " + str(datosWIP[calle]['palletscti'][1][i]) )

                        o =Foto_Palletscti_Inv_Cic_WIP.objects.create( calle=fotocalle, pallet=datosWIP[calle]['palletscti'][0][i] ,ORDERID=datosWIP[calle]['palletscti'][1][i])
                        o.save() #print(pallet[1])


                    for i in range(0,len(datosWIP[calle]['palletsnoencontrados'][0])):
                        #print (str(datosWIP[calle]['palletscti'][0][i]) + " " + str(datosWIP[calle]['palletscti'][1][i]) )

                        o =Foto_Palletsnoencontrados_Inv_Cic_WIP.objects.create( calle=fotocalle, pallet=datosWIP[calle]['palletsnoencontrados'][0][i] ,ORDERID=datosWIP[calle]['palletsnoencontrados'][1][i])
                        o.save() #print(pallet[1])


                    for i in range(0,len(datosWIP[calle]['palletsencontrados'][0])):
                        #print (str(datosWIP[calle]['palletscti'][0][i]) + " " + str(datosWIP[calle]['palletscti'][1][i]) )

                        o =Foto_Palletsencontrados_Inv_Cic_WIP.objects.create( calle=fotocalle, pallet=datosWIP[calle]['palletsencontrados'][0][i] ,ORDERID=datosWIP[calle]['palletsencontrados'][1][i])
                        o.save() #print(pallet[1])

                    for i in range(0,len(datosWIP[calle]['palletsenotracalle'][0])):
                        #print (str(datosWIP[calle]['palletscti'][0][i]) + " " + str(datosWIP[calle]['palletscti'][1][i]) )

                        o =Foto_Palletsenotracalle_Inv_Cic_WIP.objects.create( calle=fotocalle, pallet=datosWIP[calle]['palletsenotracalle'][0][i] ,ORDERID=datosWIP[calle]['palletsenotracalle'][1][i])
                        o.save() #print(pallet[1])


                    ultimatoma=(tomainv.fechatomainvcic).strftime("%m/%d/%Y %H:%M:%S")

                instance=Foto_Inv_Cic_WIP.objects.filter(fecha_foto__lt=fotoinvcic.fecha_foto)
                instance.delete()

                #print(datosWIP)
                print(ultimatoma)
                sleep(10)
            except Exception as e:
                print(e)
                print("error!")
                sleep(10)
            sleep(360)
