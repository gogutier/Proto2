from django.core.management.base import BaseCommand, CommandError
from blog.models import Pallet as Pallet
from blog.models import MovPallets as MovPallets
from blog.models import ConsumoRollos as ConsumoRollos
from blog.models import Foto_ConsumoRollos as Foto_ConsumoRollos


class Command(BaseCommand):
    def handle(self, *args, **options):
        '''
        print("iniciando limpieza pallets")
        Pallet.objects.all().delete()
        print("iniciando limpieza mov pallets")
        MovPallets.objects.all().delete()
        '''
        #print("iniciando limpieza Foto consumo rollos")
        #Foto_ConsumoRollos.objects.all().delete()

        print("mobver pallets corrugado a Z01")
        for pallet in Pallet.objects.filter(ubic="CORR_UPPER_Stacker"):
            pallet.ubic="Z01"
            pallet.save()
        for pallet in Pallet.objects.filter(ubic="CORR_LOWER_Stacker"):
            pallet.ubic="Z01"
            pallet.save()
        for pallet in Pallet.objects.filter(ubic="ZFFG2"):
            pallet.ubic="Z01"
            pallet.save()


        #print("iniciando limpieza consumo rollos")
        #ConsumoRollos.objects.all().delete()





        print("listo")
