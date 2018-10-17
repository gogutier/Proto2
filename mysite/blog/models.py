from django.db import models
from django.utils import timezone
from django.urls import reverse
import datetime
import csv

JAN = "Enero"
FEB = "Febrero"
MAR = "Marzo"
ABR = "Abril"

class OrderInfo(models.Model):
    orderId=models.CharField(unique=True, max_length=100, editable=False, default=".")
    padron=models.CharField(max_length=100, default=".")
    cliente=models.CharField(max_length=100, default=".")

    def __str__(self):
        return (self.orderId)

class Minuta(models.Model):
    dia=models.DateField(blank=False, default = datetime.datetime.now())
    texto=models.TextField(default = "")
    obs=models.CharField(max_length=100, default="S/N")

    def __str__(self):
        return str((self.dia))

class Turnos(models.Model):
    turno=models.CharField(max_length=10, default="vacio")
    horaini=models.CharField(max_length=100, default="vacio")
    horafin=models.CharField(max_length=100, default="vacio")

    def __str__(self):
        return (self.turno)


class Maquinas(models.Model):
    maquina=models.CharField(max_length=10, default="vacio")

    def __str__(self):
        return (self.maquina)



class ProdReal(models.Model):

    #cargamasivaa=models.ForeignKey('blog.CargaProducciones', related_name='fecha_carga_producciones', on_delete=models.CASCADE)
    cliente= models.CharField(max_length=200, default="vacio")
    orderId= models.CharField(max_length=200, default="vacio")
    padron = models.CharField(max_length=200, default="vacio")
    datefin = models.DateTimeField(blank=False)
    datefinajustada = models.DateTimeField(blank=False)
    turno = models.CharField(max_length=200, default="vacio")

    qOrd = models.CharField(max_length=200, default="vacio")
    lamDisp = models.CharField(max_length=200, default="vacio") #en interlink acá dice laminas programadas pero al parecer son las láminas disponible al momento de producir
    nSalidas = models.CharField(max_length=200, default="vacio")
    qProd = models.CharField(max_length=200, default="vacio")
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

class OrdenProg(models.Model):

    fecha_programa= models.DateTimeField(blank=False)# tb puede incluir default=datetime.now
    #fecha_programa=models.CharField(max_length=200, default="vacio")
    transaction_index= models.CharField(max_length=200, default="vacio")
    horizonteini = models.DateTimeField(blank=True)
    horizontefin = models.DateTimeField(blank=True)

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


class SolCamb(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    create_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length = 200, default = "holi")
    #post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE,)
    text = models.CharField(max_length=200)
    solicitudot = models.CharField(max_length=200)
    order_id = models.CharField(max_length=200)
    cliente = models.CharField(max_length=200)
    fechabpt = models.CharField(max_length=200)
    maquina = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    approved_cambio = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
       return reverse("solcamb_detail", kwargs={'pk':self.pk})


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
