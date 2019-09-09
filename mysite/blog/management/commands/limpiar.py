from django.core.management.base import BaseCommand, CommandError
from blog.models import Pallet as Pallet
from blog.models import MovPallets as MovPallets


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("iniciando limpieza pallets")
        Pallet.objects.all().delete()
        print("iniciando limpieza mov pallets")

        MovPallets.objects.all().delete()
        print("listo")
