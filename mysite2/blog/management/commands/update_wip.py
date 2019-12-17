from django.core.management.base import BaseCommand, CommandError
from blog.models import InfoWIP as InfoWIP
from django.utils import timezone
import pruebawebscrap

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)
        poll_id="hola"

    def handle(self, *args, **options):
        ''' #esto es el ejemplo con el poll_id que se crea en el add arguments.
        for poll_id in options['poll_id']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()
        '''

        poll_id="hola"
        self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))


        #################

        self.stdout.write("cargando datos wip")

        placas_wip = pruebawebscrap.webscrap_wip()
                ## [N° máquina, n° piezas, Area]
        self.stdout.write("preparandose para copiar")#Esto debería checkear también si fué un éxito la toma de datos del webscrap.
        for i in range(9,0,-1):
            self.stdout.write("copiando datos "+ str(i))
            Info=InfoWIP.objects.all().order_by('contador')[i]
            Infoprev=InfoWIP.objects.all().order_by('contador')[i-1]

            Info.M2FFG=Infoprev.M2FFG
            Info.PiFFG=Infoprev.PiFFG

            Info.M2FFW=Infoprev.M2FFW
            Info.PiFFW=Infoprev.PiFFW

            Info.M2TCY=Infoprev.M2TCY
            Info.PiTCY=Infoprev.PiTCY

            Info.M2DRO=Infoprev.M2DRO
            Info.PiDRO=Infoprev.PiDRO

            Info.M2WRD=Infoprev.M2WRD
            Info.PiWRD=Infoprev.PiWRD

            Info.M2HCR=Infoprev.M2HCR
            Info.PiHCR=Infoprev.PiHCR

            Info.M2CORR=Infoprev.M2CORR
            Info.PiCORR=Infoprev.PiCORR

            Info.M2DIM=Infoprev.M2DIM
            Info.PiDIM=Infoprev.PiDIM

            Info.M2Otros= Infoprev.M2Otros
            Info.PiOtros= Infoprev.PiOtros

            Info.M2Total= Infoprev.M2Total
            Info.PiTotal= Infoprev.PiTotal

            Info.fechamuestra= Infoprev.fechamuestra

            Info.save()

        #Actualizo el objeto InfoWIP n° cero:
        Info=InfoWIP.objects.all().order_by('contador')[0]

        Info.M2FFG=round(placas_wip[0][2],2)
        Info.PiFFG=round(placas_wip[0][1],2)

        Info.M2FFW=round(placas_wip[2][2],2)
        Info.PiFFW=round(placas_wip[2][1],2)

        Info.M2TCY=round(placas_wip[1][2],2)
        Info.PiTCY=round(placas_wip[1][1],2)

        Info.M2DRO=round(placas_wip[3][2],2)
        Info.PiDRO=round(placas_wip[3][1],2)

        Info.M2WRD=round(placas_wip[4][2],2)
        Info.PiWRD=round(placas_wip[4][1],2)

        Info.M2HCR=round(placas_wip[5][2],2)
        Info.PiHCR=round(placas_wip[5][1],2)

        Info.M2DIM=round(placas_wip[6][2],2)
        Info.PiDIM=round(placas_wip[6][1],2)

        Info.M2CORR=round(placas_wip[7][2],2)
        Info.PiCORR=round(placas_wip[7][1],2)

        Info.M2Total= Info.M2FFG +Info.M2FFW+Info.M2TCY+Info.M2DRO+Info.M2WRD+Info.M2HCR+Info.M2DIM+Info.M2CORR
        Info.PiTotal= Info.PiFFG +Info.PiFFW+Info.PiTCY+Info.PiDRO+Info.PiWRD+Info.PiHCR+Info.PiDIM+Info.PiCORR

        Info.fechamuestra = timezone.now()

        Info.save()

        self.stdout.write("Datos actualizados")
        self.stdout.write(str(Info.fechamuestra))
