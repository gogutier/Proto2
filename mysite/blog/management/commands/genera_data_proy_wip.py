from django.core.management.base import BaseCommand, CommandError
from blog.models import OrdenCorrplan as OrdenCorrplan
from blog.models import FotoCorrplan as FotoCorrplan
from blog.models import FotoProgCorr as FotoProgCorr
from blog.models import Datos_Proy_WIP as Datos_Proy_WIP
from blog.models import DatosWIP_Prog as DatosWIP_Prog
from blog.models import MovPallets as MovPallets
from blog.models import Datos_MovPallets as Datos_MovPallets
from blog.models import IDProgCorr as IDProgCorr
from blog.models import Pallet as Pallet
from blog.models import Cartones as Cartones
from blog.models import Maquinas as Maquinas

from django.db.models import Q
import webscrap3

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
            #########
            print("actualizo el Movpallets")
            try:


                labels=[]
                ahora=timezone.now().replace(hour= 0, minute=0, second=0, microsecond=0)
                for i in range(0,8):
                    #por ahora los voy a ordenar por turno, después por hora.
                    fecha=(ahora-timedelta(days=7-i)).replace(hour= 7)
                    turno="A"
                    label= fecha.strftime("%d-%m") + " " + turno
                    labels.append({"fecha":fecha ,"turno":turno, "label": label})

                    fecha=(ahora-timedelta(days=7-i)).replace(hour= 14, minute=30)
                    turno="B"
                    label= fecha.strftime("%d-%m") + " " + turno
                    labels.append({"fecha":fecha ,"turno":turno, "label": label})

                    fecha=(ahora-timedelta(days=7-i)).replace(hour= 22)
                    turno="C"
                    label= fecha.strftime("%d-%m") + " " + turno
                    labels.append({"fecha":fecha ,"turno":turno, "label": label})

                #ahpra por cada labe[] le anexo el dato de los m2 de entrada.

                listafiltroproducido=["CORR_UPPER_Stacker", "CORR_LOWER_Stacker"]
                listafiltroentrada=["ZTCY1","ZTCY2","ZHCR1","ZHCR2","ZWRD1","ZWRD2","ZFFW1","ZFFW2","ZDRO1","ZDRO2","ZFFG1","ZFFG2","ZSOB1","ZSOB2","ZPNC","ZPASILLO"]
                listafiltrosalida=["TCY","HCR","WRD","FFW","DRO","FFG","ZPICADO"]

                filtroproducidoqs=Q()

                filtroentradaqs=Q()
                filtrosalidaqs=Q()

                for item in listafiltroproducido:
                    filtroproducidoqs = filtroproducidoqs | Q(DESTINATION=item)

                for item in listafiltroentrada:
                    filtroentradaqs = filtroentradaqs | Q(DESTINATION=item)

                for item in listafiltrosalida:
                    filtrosalidaqs = filtrosalidaqs | Q(DESTINATION=item)

                for i in range(0,len(labels)-1):

                    #Entradas
                    filtro=MovPallets.objects.filter(filtroentradaqs, EVENTDATETIME__gte=labels[i]["fecha"], EVENTDATETIME__lt=labels[i+1]["fecha"])
                    cantidad1=filtro.count()
                    #sumo los m2 asociados a cada pallets
                    m2tot=0
                    for mov in filtro:
                        m2tot=m2tot+mov.m2pallet

                    labels[i]["cantidadIn"]= cantidad1
                    labels[i]["m2In"]= m2tot



                    #Producidos pero excluyendo los pallets que ya están en la lista de Entradas (acá saco el m2 actualizado de cada pallet, para descartar las producciones que se fueron a cero)
                    filtro2=MovPallets.objects.filter(filtroproducidoqs, EVENTDATETIME__gte=labels[i]["fecha"], EVENTDATETIME__lt=labels[i+1]["fecha"])


                    for item in filtro:
                        filtro2=filtro2.exclude(LOADID=item.LOADID)


                    cantidad1=filtro2.count()
                    #sumo los m2 asociados a cada pallets
                    m2tot=0
                    for mov in filtro2:
                        #print(str(mov) + ".." + str(mov.LOADID) )
                        try:
                            m2tot=m2tot+Pallet.objects.get(tarja=mov.LOADID).m2pallet
                        except:
                            print("error con " + str(mov) + ".." + str(mov.LOADID) + "!!")


                    labels[i]["cantidadProd"]= cantidad1
                    labels[i]["m2Prod"]= m2tot


                    #Salidas
                    filtro=MovPallets.objects.filter(filtrosalidaqs, EVENTDATETIME__gte=labels[i]["fecha"], EVENTDATETIME__lt=labels[i+1]["fecha"])
                    cantidad1=filtro.count()
                    #sumo los m2 asociados a cada pallet
                    m2tot=0
                    for mov in filtro:
                        m2tot=m2tot+mov.m2pallet

                    labels[i]["cantidadOut"]= cantidad1
                    labels[i]["m2Out"]= m2tot





                #este es el último item de cada lista (como termina donde empieza el siguiente no funciona dentro del for)


                #Entrada
                filtro=MovPallets.objects.filter(filtroentradaqs, EVENTDATETIME__gte=labels[len(labels)-1]["fecha"])
                cantidad1=filtro.count()


                m2tot=0
                for mov in filtro:
                    m2tot=m2tot+mov.m2pallet

                labels[len(labels)-1]["cantidadIn"]= cantidad1
                labels[len(labels)-1]["m2In"]= m2tot



                #Producido no ingresado
                filtro2=MovPallets.objects.filter(filtroproducidoqs, EVENTDATETIME__gte=labels[len(labels)-1]["fecha"])


                for item in filtro:
                    filtro2=filtro2.exclude(LOADID=item.LOADID)



                cantidad1=filtro2.count()


                m2tot=0
                for mov in filtro2:
                    m2tot=m2tot+Pallet.objects.get(tarja=mov.LOADID).m2pallet

                labels[len(labels)-1]["cantidadProd"]= cantidad1
                labels[len(labels)-1]["m2Prod"]= m2tot


                #Salida
                filtro=MovPallets.objects.filter(filtrosalidaqs, EVENTDATETIME__gte=labels[len(labels)-1]["fecha"])
                cantidad1=filtro.count()

                m2tot=0
                for mov in filtro:
                    m2tot=m2tot+mov.m2pallet


                labels[len(labels)-1]["cantidadOut"]= cantidad1
                labels[len(labels)-1]["m2Out"]= m2tot

                antiguos= Datos_MovPallets.objects.all().delete()

                #print(labels)
                for dato in labels:
                    o = Datos_MovPallets.objects.create(fecha=dato['fecha'],turno=dato['turno'],label=dato['label'],cantidadIn=dato['cantidadIn'],m2In=dato['m2In'],cantidadProd=dato['cantidadProd'],m2Prod=dato['m2Prod'],cantidadOut=dato['cantidadOut'],m2Out=dato['m2Out'])
                    o.save()


                ###########
                print("actualizo el update_wip_prog")

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
            except:
                print("error")
                sleep(10)




                ###########

            print("Primero saco el dato del programa de corrugado:")
            try:
                prog_corrugado = webscrap3.webscrap_prog_corr()


                foto, created =FotoProgCorr.objects.get_or_create(fecha_foto=datetime.now())
                foto.save()
                #Borrar los antiguos..
                instance=FotoProgCorr.objects.filter(fecha_foto__lt=foto.fecha_foto)
                instance.delete()



                fecha_fin_anterior=0
                for prog in prog_corrugado:
                    #transformando el dato de fecha a datetime
                    #print(prog)

                    fechafin=datetime.strptime(prog[6], '%d-%m %H:%M')
                    fechafin=fechafin.replace(year= datetime.now().year)
                    #print(fechafin)

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
                    #print(id)
                    #print(id.fecha_inicio)
                    #print(id.fecha_fin)


                #########

                print("Ahora actualizo los datos del panel de proyección.")

                print("hago lista de fechas que quiero mostrar:") #basado en el get_data_mov_pallets pero genera las fechas a futuro. Como texto y como datetime
                labels=[]#fechas, será el label del gráfico
                ahora=datetime.now()
                ahorafix=ahora.replace(hour= 0, minute=0, second=0, microsecond=0)-timedelta(days=1)
                for i in range(0,2):
                    #por ahora los voy a ordenar por turno, después por hora.
                    fecha_inicio=(ahorafix+timedelta(days=i)).replace(hour= 7)
                    fecha_fin=(ahorafix+timedelta(days=i)).replace(hour= 14, minute=30)
                    turno="A"
                    label= fecha_inicio.strftime("%d-%m") + " " + turno
                    if ahora<=fecha_fin:#ahora<=(ahorafix+timedelta(days=i)).replace(hour= 14, minute=30):
                        labels.append({"fecha_inicio":fecha_inicio ,"fecha_fin":fecha_fin ,"turno":turno, "label": label})


                    fecha_inicio=(ahorafix+timedelta(days=i)).replace(hour= 14, minute=30)
                    fecha_fin=(ahorafix+timedelta(days=i)).replace(hour= 22)
                    turno="B"
                    label= fecha_inicio.strftime("%d-%m") + " " + turno
                    if ahora<=fecha_fin:#ahora<=(ahorafix+timedelta(days=i)).replace(hour= 22):
                        labels.append({"fecha_inicio":fecha_inicio ,"fecha_fin":fecha_fin ,"turno":turno, "label": label})

                    fecha_inicio=(ahorafix+timedelta(days=i)).replace(hour= 22)
                    fecha_fin=(ahorafix+timedelta(days=i+1)).replace(hour= 7)
                    turno="C"
                    label= fecha_inicio.strftime("%d-%m") + " " + turno
                    if ahora<=fecha_fin:#ahora<=(ahorafix+timedelta(days=i+1)).replace(hour= 7):
                        labels.append({"fecha_inicio":fecha_inicio ,"fecha_fin":fecha_fin,"turno":turno,"label": label})

                #Ahora, por cada label, calculo la suma de Mm2 de conversión que se iniciarán en ese turno según corrplan


                #calculo el inventario inicial a la fecha en el WIP:
                invtotwip=0
                for pallet in Pallet.objects.filter( Q(ubic="ZFFG1") | Q(ubic="ZFFG2")| Q(ubic="ZFFW1")| Q(ubic="ZFFW2")| Q(ubic="ZDRO1")| Q(ubic="ZDRO2")| Q(ubic="ZTCY1") | Q(ubic="ZTCY2")| Q(ubic="ZWRD1")| Q(ubic="ZWRD2")| Q(ubic="ZHCR1")| Q(ubic="ZHCR2")| Q(ubic="ZSOB1") | Q(ubic="ZSOB2") | Q(ubic="ZPASILLO")):
                #        if pallet.ORDERID != order.order_id:
                    invtotwip=invtotwip+(pallet.m2pallet/1000)



                fecha_anterior=0
                for turn in labels:
                    #print(turno['fecha'])


                    filtro=OrdenCorrplan.objects.filter(fecha_inicio__gte=turn['fecha_inicio']).filter(fecha_inicio__gte=ahora).filter(fecha_inicio__lt=turn['fecha_fin'])
                    sumaM2=0
                    for orden in filtro:
                        sumaM2=sumaM2 + orden.area
                    #print(sumaM2)

                    turn["M2Conv"]=sumaM2




                    filtrocorr=IDProgCorr.objects.filter(fecha_inicio__gte=turn['fecha_inicio']).filter(fecha_inicio__gte=ahora).filter(fecha_inicio__lt=turn['fecha_fin'])
                    sumaM2=0
                    print("suma M2 corr filtro inicio entre " + str(turn['fecha_inicio']) + " y " + str(turn['fecha_fin']) )
                    for orden in filtrocorr:
                        print(str(orden)+": "+ str(orden.fecha_inicio))


                        sumaM2=sumaM2 + (orden.area)
                    print("suma tot M2 tramo: " + str(sumaM2) )
                    turn["M2Corr"]=sumaM2





                    invtotwip=invtotwip+int(turn["M2Corr"])-int(turn["M2Conv"])


                    turn["M2Inv"]=invtotwip


                antiguos= Datos_Proy_WIP.objects.all().delete()



                for dato in labels:

                    o = Datos_Proy_WIP.objects.create(fecha_inicio=dato['fecha_inicio'],fecha_fin=dato['fecha_fin'],turno=dato['turno'],label=dato['label'],M2Conv=dato['M2Conv'],M2Corr=dato['M2Corr'],M2Inv=dato['M2Inv'])
                    o.save()
            except:
                print("error")
                sleep(30)
            print("Esperando para hacer prox carga masiva de datos")
            sleep(120)
        #print(labels)
