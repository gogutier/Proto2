from django.db import models
from django.utils import timezone
from django.urls import reverse
import datetime
import csv

JAN = "Enero"
FEB = "Febrero"
MAR = "Marzo"
ABR = "Abril"

class Camion(models.Model):

    #cargamasivaa=models.ForeignKey('blog.CargaProducciones', related_name='fecha_carga_producciones', on_delete=models.CASCADE)

    Patente=models.CharField(blank=False, unique=True, max_length=10, default="vacio")
    Chofer=models.CharField(max_length=15, default="vacio")
    Telefono=models.CharField(max_length=15, default="vacio")
    Rut=models.CharField(max_length=15, default="vacio")
    Transportista=models.CharField(max_length=20, default="vacio")

    dia=models.DateField(max_length=10, default="vacio")

    def __str__(self):
        return (self.Patente)



class InfoWIP(models.Model):

    #cargamasivaa=models.ForeignKey('blog.CargaProducciones', related_name='fecha_carga_producciones', on_delete=models.CASCADE)

    contador = models.IntegerField(default=0)

    M2FFG=models.FloatField(default=0)
    PiFFG=models.FloatField(default=0)

    M2FFW=models.FloatField(default=0)
    PiFFW=models.FloatField(default=0)

    M2TCY=models.FloatField(default=0)
    PiTCY=models.FloatField(default=0)

    M2DRO=models.FloatField(default=0)
    PiDRO=models.FloatField(default=0)

    M2WRD=models.FloatField(default=0)
    PiWRD=models.FloatField(default=0)

    M2HCR=models.FloatField(default=0)
    PiHCR=models.FloatField(default=0)

    M2Otros=models.FloatField(default=0)
    PiOtros=models.FloatField(default=0)

    M2Total=models.FloatField(default=0)
    PiTotal=models.FloatField(default=0)


    fechamuestra= models.DateTimeField(blank=False, default = timezone.now())#.replace(hour= 0, minute=0, second=0, microsecond=0))


    def __str__(self):
        return (str(self.contador))


class ProyMkt(models.Model):

    #cargamasivaa=models.ForeignKey('blog.CargaProducciones', related_name='fecha_carga_producciones', on_delete=models.CASCADE)
    fechaproy= models.DateField(blank=False, default = timezone.now().replace(hour= 0, minute=0, second=0, microsecond=0))


    def __str__(self):
        return (str(self.fechaproy))

class ProyMktMes(models.Model):

    #cargamasivaa=models.ForeignKey('blog.CargaProducciones', related_name='fecha_carga_producciones', on_delete=models.CASCADE)
    proymkt= models.ForeignKey('blog.ProyMkt', related_name='proymkt', on_delete=models.CASCADE,)
    mes=models.CharField(max_length=10, default="vacio")
    mescorto=models.CharField(max_length=10, default="vacio")
    mesnum=models.IntegerField(default=0)

    tot_unidades=models.IntegerField(default=1)
    tot_me=models.IntegerField(default=1)
    tot_golpes=models.IntegerField(default=1)


    def __str__(self):
        return (str(self.proymkt)+"-"+str(mesnum))



#cada padrón en la proyección de marketing se asocia a un proyMktMes, no a un cliente (para no tener que agregar lista de clientes)

class ProyMktPadron(models.Model):

    #cargamasivaa=models.ForeignKey('blog.CargaProducciones', related_name='fecha_carga_producciones', on_delete=models.CASCADE)
    proymktmes= models.ForeignKey('blog.ProyMktMes', related_name='proymktmes', on_delete=models.CASCADE,)
    cliente=models.CharField(max_length=20, default="vacio")
    padron=models.CharField(max_length=20, default="vacio") #lo asocio al maestro padrón?
    descripcion=models.CharField(max_length=100, default="vacio")
    mercado=models.CharField(max_length=10, default="vacio")
    maquina=models.CharField(max_length=10, default="vacio")
    carton=models.CharField(max_length=10, default="vacio")

    unidades=models.IntegerField(default=0)
    m2=models.IntegerField(default=0)
    tons=models.IntegerField(default=0)

    ton_placa_equiv=models.IntegerField(default=0)


    def __str__(self):
        return (str(self.proymkt)+"-"+str(mesnum))




class FotoInventario(models.Model):

    fecha_carga=models.DateField(blank=False, default = timezone.now().replace(hour= 0, minute=0, second=0, microsecond=0))

    total_kraft_kg=models.IntegerField(default=0)
    total_blanco_kg=models.IntegerField(default=0)
    total_CPP_kg=models.IntegerField(default=0)
    total_otros_kg=models.IntegerField(default=0)

    kraft_saldos_kg=models.IntegerField(default=0)
    blanco_saldos_kg=models.IntegerField(default=0)
    CPP_saldos_kg=models.IntegerField(default=0)
    otros_saldos_kg=models.IntegerField(default=0)

    kraft_saldos_un=models.IntegerField(default=0)
    blanco_saldos_un=models.IntegerField(default=0)
    CPP_saldos_un=models.IntegerField(default=0)
    otros_saldos_un=models.IntegerField(default=0)


    kraft_retenidos_un=models.IntegerField(default=0)
    blanco_retenidos_un=models.IntegerField(default=0)
    CPP_retenidos_un=models.IntegerField(default=0)
    otros_retenidos_un=models.IntegerField(default=0)

    kraft_retenidos_kg=models.IntegerField(default=0)
    blanco_retenidos_kg=models.IntegerField(default=0)
    CPP_retenidos_kg=models.IntegerField(default=0)
    otros_retenidos_kg=models.IntegerField(default=0)


    kraft_1_meses_kg=models.IntegerField(default=0)
    blanco_1_meses_kg=models.IntegerField(default=0)
    CPP_1_meses_kg=models.IntegerField(default=0)
    otros_1_meses_kg=models.IntegerField(default=0)

    kraft_3_meses_kg=models.IntegerField(default=0)
    blanco_3_meses_kg=models.IntegerField(default=0)
    CPP_3_meses_kg=models.IntegerField(default=0)
    otros_3_meses_kg=models.IntegerField(default=0)

    kraft_6_meses_kg=models.IntegerField(default=0)
    blanco_6_meses_kg=models.IntegerField(default=0)
    CPP_6_meses_kg=models.IntegerField(default=0)
    otros_6_meses_kg=models.IntegerField(default=0)

    def __str__(self):
        return ( str(self.fecha_carga) )




class DiaConv2(models.Model):
    diaajust=models.DateField(blank=False, default = timezone.now().replace(hour= 0, minute=0, second=0, microsecond=0))
    turno=models.ForeignKey('blog.Turnos', blank=False, on_delete=models.CASCADE)
    semana=models.IntegerField(default=0)
    mes=models.IntegerField(default=0)
    anno=models.IntegerField(default=0)
    #maquina=models.ForeignKey('blog.Maquinas', blank=False, on_delete=models.CASCADE)
    progIdFFG=models.FloatField(default=0) #Id programado
    prodIdFFG=models.FloatField(default=0) #Id producido que sí fue programado para ese turno
    prod2IdFFG=models.FloatField(default=0) #Id roducido dentro del turno pero fuera de programa
    progM2FFG=models.FloatField(default=0) #M2 programado
    prodM2FFG=models.FloatField(default=0) #M2 producido que sí fue programado para ese turno
    prod2M2FFG=models.FloatField(default=0)#M2 roducido dentro del turno pero fuera de programa

    progIdFFW=models.FloatField(default=0)
    prodIdFFW=models.FloatField(default=0)
    prod2IdFFW=models.FloatField(default=0)
    progM2FFW=models.FloatField(default=0)
    prodM2FFW=models.FloatField(default=0)
    prod2M2FFW=models.FloatField(default=0)

    progIdTCY=models.FloatField(default=0)
    prodIdTCY=models.FloatField(default=0)
    prod2IdTCY=models.FloatField(default=0)
    progM2TCY=models.FloatField(default=0)
    prodM2TCY=models.FloatField(default=0)
    prod2M2TCY=models.FloatField(default=0)

    progIdHCR=models.FloatField(default=0)
    prodIdHCR=models.FloatField(default=0)
    prod2IdHCR=models.FloatField(default=0)
    progM2HCR=models.FloatField(default=0)
    prodM2HCR=models.FloatField(default=0)
    prod2M2HCR=models.FloatField(default=0)


    progIdWRD=models.FloatField(default=0)
    prodIdWRD=models.FloatField(default=0)
    prod2IdWRD=models.FloatField(default=0)
    progM2WRD=models.FloatField(default=0)
    prodM2WRD=models.FloatField(default=0)
    prod2M2WRD=models.FloatField(default=0)


    progIdDRO=models.FloatField(default=0)
    prodIdDRO=models.FloatField(default=0)
    prod2IdDRO=models.FloatField(default=0)
    progM2DRO=models.FloatField(default=0)
    prodM2DRO=models.FloatField(default=0)
    prod2M2DRO=models.FloatField(default=0)

    def __str__(self):
        return ( str(self.diaajust)+" " + str(self.turno) )



class Padron(models.Model):
    padron=models.CharField(unique=True, max_length=100, editable=False, default=".")
    m2uni=models.FloatField(default=0)
    uxg=models.IntegerField(default=1)
    status=models.CharField(max_length=100, default=".")

    def __str__(self):
        return (self.padron)

class OrderInfo(models.Model):
    orderId=models.CharField(unique=True, max_length=100, editable=False, default=".")
    padron=models.CharField(max_length=100, default=".")
    cliente=models.CharField(max_length=100, default=".")
    SO=models.CharField(max_length=100, default=".")
    SOPosition=models.IntegerField(default=0)
    qOrd=models.IntegerField(default=0)
    blanksrequired=models.IntegerField(default=0)
    blankstocorr=models.IntegerField(default=0)
    fechacarga=models.DateField(blank=False, default = timezone.now().replace(hour= 0, minute=0, second=0, microsecond=0))
    clave=models.CharField(max_length=100, default=".")
    def __str__(self):
        return (self.orderId)

class Minuta(models.Model):
    dia=models.DateField(blank=False, default = timezone.now())
    texto=models.TextField(default = ".")
    obs=models.CharField(max_length=100, default="S/N")

    def __str__(self):
        return str((self.dia))

class Turnos(models.Model):
    turno=models.CharField(unique=True,max_length=10, default="vacio")
    horaini=models.CharField(max_length=100, default="vacio")
    horafin=models.CharField(max_length=100, default="vacio")

    def __str__(self):
        return (str(self.turno))


class Maquinas(models.Model):
    maquina=models.CharField(unique=True,max_length=10, default="vacio")

    def __str__(self):
        return (str(self.maquina))

class Meses(models.Model):
    mes=models.CharField(max_length=10, default="vacio")
    mescorto=models.CharField(max_length=10, default="vacio")
    mesnum=models.IntegerField(default=0)
    dias=models.CharField(max_length=10, default="vacio")
    diasnoprod=models.CharField(max_length=10, default="vacio")
    año=models.IntegerField(default=0)

    def __str__(self):
        return (str(self.mes))

class Semanas(models.Model):
    semana=models.IntegerField(default="1")
    mescorto=models.CharField(max_length=10, default="vacio")
    mesnum=models.IntegerField(default=0)
    diasprod=models.FloatField(default=5.5)
    año=models.IntegerField(default=0)

    def __str__(self):
        return (str(self.semana))


class ProdReal(models.Model):

    #cargamasivaa=models.ForeignKey('blog.CargaProducciones', related_name='fecha_carga_producciones', on_delete=models.CASCADE)
    cliente= models.CharField(max_length=200, default="vacio")
    orderId= models.CharField(max_length=200, default="vacio")
    padron = models.CharField(max_length=200, default="vacio")
    datefin = models.DateTimeField(blank=False)
    datefinajustada = models.DateTimeField(blank=False)
    turno = models.CharField(max_length=200, default="vacio")

    semana=models.IntegerField(default=0)
    mes=models.IntegerField(default=0)
    anno=models.IntegerField(default=0)

    qOrd = models.IntegerField(default=0)
    lamDisp = models.CharField(max_length=200, default="vacio") #en interlink acá dice laminas programadas pero al parecer son las láminas disponible al momento de producir
    nSalidas = models.CharField(max_length=200, default="vacio")
    qProd = models.IntegerField(default=0)
    porcTerm = models.CharField(max_length=200, default="vacio")
    maquina = models.CharField(max_length=200, default="vacio")


    orderIdPrev = models.CharField(max_length=200, default="vacio")
    orderIdPost = models.CharField(max_length=200, default="vacio")

    def __str__(self):
        return (self.orderId)


class DetalleProg(models.Model):

    programma=models.ForeignKey('blog.OrdenProg', related_name='fecha_prog', on_delete=models.CASCADE)
    workcenter= models.CharField(max_length=200, default="vacio")
    orderId= models.CharField(max_length=200, default="vacio")
    dateini = models.DateTimeField(blank=False)
    datefin = models.DateTimeField(blank=False)
    datefinajustada = models.DateTimeField(blank=False)
    turno = models.CharField(max_length=200, default="vacio")

    qIn = models.IntegerField(default=0)
    anchoplaca= models.FloatField(default=0)
    largoplaca= models.FloatField(default=0)
    numberout=models.IntegerField(default=1)

    orderIdPrev = models.CharField(max_length=200, default="vacio")
    orderIdPost = models.CharField(max_length=200, default="vacio")

    completo_fechaturno = models.CharField(max_length=200, default="vacio")
    completo_secuencia = models.CharField(max_length=200, default="vacio")
    completo_unidades = models.CharField(max_length=200, default="vacio")

    def __str__(self):
        return (self.orderId)
'''
class CargaProducciones(models.Model):

    fecha_carga= models.DateTimeField(default=datetime.datetime.now)# tb puede incluir default=datetime.now
    completo_unidades = models.CharField(max_length=200, default="vacio")
    #fecha_programa=models.CharField(max_length=200, default="vacio")

    def __str__(self):
        return str((self.fecha_carga))
'''


class ProdRealCorr(models.Model):

    #cargamasivaa=models.ForeignKey('blog.CargaProducciones', related_name='fecha_carga_producciones', on_delete=models.CASCADE)
    #ajustedatefin= models.CharField(max_length=40, default="vacio")#para identificar solamente
    ajuste= models.CharField(max_length=20, default="vacio")
    onda= models.CharField(max_length=20, default="vacio")
    formato= models.CharField(max_length=20, default="vacio")
    carton= models.CharField(max_length=20, default="vacio")
    metroslineales= models.IntegerField(default=0)
    trim= models.IntegerField(default=0)
    datefin = models.DateTimeField(blank=False)
    datefinajustada = models.DateTimeField(blank=False)
    turno = models.CharField(max_length=10, default="vacio")
    duración_min = models.IntegerField(default=1)

    def __str__(self):
        return ( str(self.ajuste) + str(self.datefinajustada) )#Ojo que al cargar el ajuste, y hay uno nuevo, hay que sumarlo? Cómo distingur si se carga el mismo ajuste 2 veces? (hora salida)



class DetalleProgCorr(models.Model):

    programma=models.ForeignKey('blog.OrdenProgCorr', related_name='fecha_prog', on_delete=models.CASCADE)

    ajuste= models.CharField(max_length=20, default="vacio")
    onda= models.CharField(max_length=20, default="vacio")
    formato= models.CharField(max_length=20, default="vacio")
    carton= models.CharField(max_length=20, default="vacio")
    metroslineales= models.IntegerField(default=0)
    trim= models.IntegerField(default=0)
    papeles= models.CharField(max_length=50, default="vacio")
    datefin = models.DateTimeField(blank=False)
    datefinajustada = models.DateTimeField(blank=False)
    turno = models.CharField(max_length=10, default="vacio")

    def __str__(self):
        return (str(self.ajuste))




class OrdenProgCorr(models.Model):

    fecha_programa= models.DateTimeField(blank=False, default=timezone.now)# tb puede incluir default=datetime.now
    #fecha_programa=models.CharField(max_length=200, default="vacio")
    #transaction_index= models.CharField(max_length=200, default="vacio")
    horizonteini = models.DateTimeField(blank=True)
    turnohorini = models.CharField(max_length=20, default="vacio")
    horizontefin = models.DateTimeField(blank=True)
    turnohorfin = models.CharField(max_length=20, default="vacio")

    def __str__(self):
        return str((self.fecha_programa))

class OrdenProg(models.Model):

    fecha_programa= models.DateTimeField(blank=False)# tb puede incluir default=datetime.now
    #fecha_programa=models.CharField(max_length=200, default="vacio")
    transaction_index= models.CharField(max_length=200, default="vacio")
    horizonteini = models.DateTimeField(blank=True)
    turnohorini = models.CharField(max_length=20, default="vacio")
    horizontefin = models.DateTimeField(blank=True)
    turnohorfin = models.CharField(max_length=20, default="vacio")

    def __str__(self):
        return str((self.fecha_programa))


class PruebaTabla(models.Model):
    item1 = models.CharField(max_length=200, default="vacio")
    item2 = models.CharField(max_length=200, default="vacio")
    item3 = models.TextField(max_length=200, default="vacio")

    def __str__(self):
        return self.item1

class PruebaMod(models.Model):
    dato1 = models.CharField(max_length=200, default="vacio")
    dato2 = models.CharField(max_length=200, default="vacio")
    ultrafile = models.TextField(default = "")

    def __str__(self):
        return self.dato1



class OrdenConv(models.Model):
    post = models.ForeignKey('blog.ProgramaConv', related_name='ordenconvs', on_delete=models.CASCADE,)
    #author = models.CharField(max_length=200)
    text = models.TextField()
    maquina = models.CharField(max_length=200)
    fechainiprog = models.CharField(max_length=200)
    fechafinprog = models.CharField(max_length=200)
    unisprog = models.CharField(max_length=200)

    #create_date = models.DateTimeField(default=timezone.now)
    #approved_comment = models.BooleanField(default=False)

    '''
    def approve(self):
        self.approved_comment = True
        self.save()
    '''

    def get_absolute_url(self):
        return reverse('ordenconv_list')

    def __str__(self):
        return self.title



class ProgramaConv(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)

    '''
    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
    '''

    def get_absolute_url(self):
        return reverse("programa_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title





#Para el ejemplo de dynamic form creation
class Book(models.Model):

    name = models.CharField(max_length=255)
    isbn_number = models.CharField(max_length=13)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.name


class Author(models.Model):

    name = models.CharField(max_length=255)
    book = models.ForeignKey(
        Book,
        related_name='authors', on_delete=models.SET_NULL,
        null=True)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return self.name




class OCImportacion(models.Model):
        MONTH_CHOICES = (
            (JAN, "January"),
            (FEB, "February"),
            (MAR, "March"),
            (ABR, "April"),
        )
        # Create your models here.

        author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
        oc = models.CharField(max_length = 200)
        proveedor = models.CharField(max_length = 200)
        create_date = models.DateTimeField(default=timezone.now)
        mes_arribo_esperado = models.CharField(max_length = 200, choices= MONTH_CHOICES)
        #published_date = models.DateTimeField(blank=True, null=True)



class CargaCSV(models.Model):

    def get_all_products():
        items = []
        with open('prueba.csv','r') as fp:
            # You can also put the relative path of csv file
            # with respect to the manage.py file
            reader1 = csv.reader(fp, delimiter=';')
            for value in reader1:
                items.append(value)
        return items



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE,)
    author = models.CharField(max_length=200)
    text = models.TextField()

    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.title


class appointment(models.Model):
    #author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    Patient = models.CharField(max_length = 200, blank=True, null=True)
    Date = models.CharField(max_length = 200, blank=True, null=True)
    Time = models.CharField(max_length = 200, blank=True, null=True)
    Duration = models.CharField(max_length = 200, blank=True, null=True)
    Location = models.CharField(max_length = 200, blank=True, null=True)
    Clinician = models.CharField(max_length = 200, blank=True, null=True)
    AppointmentType = models.CharField(max_length = 200, blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title



class ProdID(models.Model):
    #author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    title = models.CharField(max_length = 200, default="orden")
    transactindex = models.CharField(max_length = 200)
    plantid = models.CharField(max_length = 200, blank=True, null=True)
    workcenter = models.CharField(max_length = 200, blank=True, null=True)
    orderid = models.CharField(max_length = 200, blank=True, null=True)

    setupstartdate = models.CharField(max_length = 200, blank=True, null=True)
    setupenddate = models.CharField(max_length = 200, blank=True, null=True)
    runstartdate = models.CharField(max_length = 200, blank=True, null=True)
    runenddate = models.CharField(max_length = 200, blank=True, null=True)
    duracion = models.CharField(max_length = 200, blank=True, null=True)


    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    Patient = models.CharField(max_length = 200, blank=True, null=True)
    Date = models.CharField(max_length = 200, blank=True, null=True)
    Time = models.CharField(max_length = 200, blank=True, null=True)

    Location = models.CharField(max_length = 200, blank=True, null=True)
    Clinician = models.CharField(max_length = 200, blank=True, null=True)
    AppointmentType = models.CharField(max_length = 200, blank=True, null=True)



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title
