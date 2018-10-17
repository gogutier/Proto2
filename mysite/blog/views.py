from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post,Comment,SolCamb, appointment, CargaCSV, OCImportacion, ProdID, Book, PruebaMod, PruebaTabla, OrdenProg, DetalleProg, ProdReal, Maquinas, Turnos, Minuta, OrderInfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from blog.forms import PostForm, CommentForm, SolCambForm, ContactForm, AppointmentForm, OCImportacionForm, ProdIDForm, BookFormset, BookModelFormset, PruebaModForm, MinutaForm
from django.views.generic import (TemplateView,ListView,CreateView,DetailView, UpdateView, DeleteView, View)
from django.http import JsonResponse
import csv
from datetime import datetime, timedelta
from io import StringIO


#VIEWS ES DONDE SE PUEDE PROGRAMR EN PYTHON?
#views functions take as input: HTTPRESPONSE objects, and returns HTTPRESpose object (html output)

def minuta_detail(request, pk):
    minuta = get_object_or_404(Minuta, pk=pk)
    return render(request, 'blog/minuta_detail.html', {'minuta': minuta})

def minutas(request):
    minutas = Minuta.objects.all()
    template_name = 'blog/minutas.html'
    return render(request, template_name, {'minutas':minutas})


def minuta_new(request):

    if request.method == "POST":
        form = MinutaForm(request.POST)
        if form.is_valid():
            minuta = form.save(commit=False)
            #minuta.author = request.user
            #minuta.published_date = timezone.now()
            minuta.save()
            return redirect('minuta_detail', pk=minuta.pk)
    else:
        form = MinutaForm()
    return render(request, 'blog/minuta_edit.html', {'form': form})



class OrdenProgDetailView(DetailView):
    context_object_name = 'ordenprog'
    model = OrdenProg
    #maquinas = Maquinas.objects.all()

    #ordenes = OrdenProg.objects.all()
    #detallesProg = DetalleProg.objects.all()






    def actualizadatos(self, pk):
        #referencia = OrdenProg.objects.filter(pk=pk[0])#ojo tmabién puede ser con el get. ahí hay que poner el [0] ya que no acepta más de un resultado
        referencia = OrdenProg.objects.get(pk=pk)
        detalles = DetalleProg.objects.filter(programma = referencia)
        '''
        for produccionprogramada in detalles:
            #print("hola")
            for real in ProdReal.objects.filter(orderId = produccionprogramada.orderId, datefinajustada=produccionprogramada.datefinajustada):
                produccionprogramada.completo_unidades = str(real.qProd)+"/"+str(produccionprogramada.qIn)
                produccionprogramada.save()
            #busco si en las producciones reales hay alguna que coincida en orderID, máquina y fecha-Turno
        '''

        '''
        for ref in referencia## por cada orden programada que tenga el pk que se está consultando

            for real in detallesProg.filter(orderId = ref.orderId): #por cada producción real que tenga el mismo order id (y máquina) que se está consultando
            ref
            #real.qProd='llenoooo'
            #real.save()

            print("actualizado: " + real.orderId )
            '''



    def get_context_data(self, **kwargs):
        """
        This has been overridden to add `car` to the template context,
        now you can use {{ car }} within the template
        """
        pk = self.kwargs['pk']# this is the primary key from your URL
        # your other code

        print(pk)

        #Aquí calcula indicadores programado vs real y los guarda en la base de datos, para que después del detailview pueda mostrarlos como dato.

        self.actualizadatos(pk)

        context = super().get_context_data(**kwargs)
        context['detalleprog'] = DetalleProg.objects.filter(programma = OrdenProg.objects.get(pk=pk))#.filter(published_date__isnull=True).order_by('-published_date')
        context['prodreal'] = ProdReal.objects.all()#.filter(published_date__isnull=True).order_by('-published_date')#Acá hay que filtrar para que sean las órdenes reales desde la fecha del programa de referencia en adelante
        context['maquinas'] = Maquinas.objects.all()#.filter(published_date__isnull=True).order_by('-published_date')
        context['turnos'] = Turnos.objects.all()#.filter(published_date__isnull=True).order_by('-published_date')
        context['orderinfos'] = OrderInfo.objects.all()#Agregarle al orderinfo fecha de subida y filtrar para que busque
        #context['maquinas'] = maquinas
        return context


class Inicio(View): #ESto se puede cambiar a format based view (para que no sea clase)
    'blog/inicio.html'
    #suma el total de órdenes producidas reales para los últimos 5 días.
    datefinajustadaini = datetime(2018, 9 ,12,0,0)
    datefinajustadafin=  datetime(2018, 9 ,25,0,0)
    datefinajustadaobj=  datetime(1,1,1,0,0)
    Producciones = []
    Dias=[]
    datefinajustadaobj = datefinajustadaini


    while True:
        Dias.append(datefinajustadaobj)
        datefinajustadaobj=datefinajustadaobj + timedelta(days=1)
        if datefinajustadaobj > datefinajustadafin :
            break



    def get(self, request, *args, **kwargs):
        return render(request, 'blog/inicio.html', {"customers": 111})



def get_data(request, *args, **kwargs):
    ordenes = OrdenProg.objects.all()
    detallesProg = DetalleProg.objects.all()
    prodsreales = ProdReal.objects.all()

    datefinajustadaini = datetime(2018, 9 ,12,0,0)
    datefinajustadafin=  datetime(2018, 9 ,25,0,0)
    datefinajustadaobj=  datetime(1,1,1,0,0)
    Producciones = []
    Dias=[]
    Dias2=[]
    datefinajustadaobj = datefinajustadaini
    datefinajustadaobj2 = datefinajustadaini.strftime("%d %m %Y")


    while True:
        Dias.append(datefinajustadaobj)
        Dias2.append(datefinajustadaobj2)
        datefinajustadaobj=(datefinajustadaobj + timedelta(days=1))
        datefinajustadaobj2=(datefinajustadaobj + timedelta(days=1)).strftime("%d %m %Y")
        if datefinajustadaobj > datefinajustadafin :
            break


    #ahora agrego el número de producciones que se hicieron en cada días
    for dia in Dias:
        Producciones.append(ProdReal.objects.filter(datefinajustada=dia).count())
    print(Producciones)



    labels=["red","blue","green"]
    default_items=[123, 124, 432]
    data = {
    "labels": labels,
    "default": default_items,
    "labelDias": Dias2,
    "Producciones":Producciones,
    }
    print("Enviando Json Datos Graph")
    return JsonResponse(data)#http response con el datatype de JS




def res_conv_v2(request):
    template_name = 'blog/resumenconv.html'
    ordenes = OrdenProg.objects.all()
    detallesProg = DetalleProg.objects.all()

    ##Acá calcula los indicadores para cada Programa de producción?


    return render(request, template_name, {'ordenes':ordenes, "detallesProg": detallesProg})#acá le puedo decir que los mande ordenados por fecha?

class ResConvView(ListView):
    model = OrdenProg


def carga_prod_real(request):
    template_name = 'blog/cargaprodreal.html'
    prodsreales = ProdReal.objects.all()
    if request.method == "POST":

        form = PruebaModForm(request.POST) ##Ojo esta sí sirve, es el Ultrafile donde se pega el excel
        if form.is_valid():
            datocrudo=form.cleaned_data["ultrafile"]
            print("datocrudo.clean: " + datocrudo)
        else:
            datocrudo=form.data["ultrafile"]
            datoprocesado=datocrudo.split(",;,")
            print("datoprocesado1:")
            print(datoprocesado)
            for i in range (len(datoprocesado)):
                datoprocesado[i]=datoprocesado[i].split(",")
            print(datoprocesado)
            ####### identifica las columnas y crea los objetos que me interesanself.
            colCliente = None
            colOrderId = None
            colPadron = None
            colDatefin = None
            colDatefinajust = None
            colTurno = None
            colUnisprod = None
            colMaquina = None
            colqOrd = None

            for i in range(len(datoprocesado[0])):
                if datoprocesado[0][i] == "Cliente":
                    #print("columna creación en: " + str(i))
                    colCliente = i

                if datoprocesado[0][i] == "No. Orden":
                    #print("columna transaction en: " + str(i))
                    colOrderId = i

                if datoprocesado[0][i] == "ID Especificacion":
                    #print("columna transaction en: " + str(i))
                    colPadron = i

                if datoprocesado[0][i] == "Fecha Hora de termino":
                    #print("columna transaction en: " + str(i))
                    colDatefin = i

                if datoprocesado[0][i] == "Fecha termino ajustada":
                    #print("columna transaction en: " + str(i))
                    colDatefinajust = i


                if datoprocesado[0][i] == "Turno":
                    #print("columna transaction en: " + str(i))
                    colTurno = i

                if datoprocesado[0][i] == "Cantidad Ordenada":#Esto en verdad corresponde a las cajas producidas
                    #print("columna transaction en: " + str(i))
                    colqOrd = i


                if datoprocesado[0][i] == "Laminas Producidas":#Esto en verdad corresponde a las cajas producidas
                    #print("columna transaction en: " + str(i))
                    colUnisprod = i


                if datoprocesado[0][i] == "Maquina":
                    #print("columna transaction en: " + str(i))
                    colMaquina= i
            #fecha_now = datetime.now()
            #nuevacarga=CargaProducciones.objects.get_or_create(fecha_carga=fecha_now)
            '''
            #ejemplo

            obj, created = Person.objects.get_or_create(
                first_name='John',
                last_name='Lennon',
                defaults={'birthday': date(1940, 10, 9)},
            )
            '''


            for i in range(1,len(datoprocesado)):
                #if i==1:
                #    Reciencreado=ProdReal.objects.get_or_create(cliente=datoprocesado[i][colCliente], orderId=datoprocesado[i][colOrderId], orderIdPrev="Primero", orderIdPost=datoprocesado[i+1][colOrderId])
                #elif i==len(datoprocesado):
                #    Reciencreado=ProdReal.objects.get_or_create(cliente=datoprocesado[i][colCliente], orderId=datoprocesado[i][colOrderId], orderIdPrev=datoprocesado[i-1][colOrderId], orderIdPost=datoprocesado[i+1][colOrderId])
                #else:
                datefinajustada_datetime = datetime.strptime(datoprocesado[i][colDatefinajust], "%d-%m-%Y")#"%d-%m-%Y %H:%M"
                datefin_datetime = datetime.strptime(datoprocesado[i][colDatefin], "%d-%m-%Y %H:%M:%S")

                ProdReal.objects.get_or_create(cliente=datoprocesado[i][colCliente], orderId=datoprocesado[i][colOrderId], qOrd=datoprocesado[i][colqOrd], orderIdPrev="pendiente", orderIdPost="Final", datefin=datefin_datetime, datefinajustada=datefinajustada_datetime, turno=datoprocesado[i][colTurno], qProd=datoprocesado[i][colUnisprod], maquina=datoprocesado[i][colMaquina])
            #################


    else:
        form = PruebaModForm()

    return render(request, template_name, {'form':form})



#################################################

def carga_orderinfo(request):
    pruebamods = PruebaMod.objects.all()

    template_name = 'blog/cargaorderinfo.html'

    if request.method == "POST":
        form = PruebaModForm(request.POST)
        if form.is_valid():


            datocrudo=form.cleaned_data["ultrafile"]
            datoprocesado=datocrudo.split(";")

            #PruebaTabla.objects.create(item1=datoprocesado[0],item2=datoprocesado[1],item3=datoprocesado[2])

            post = form.save(commit=False)

            post.save()

        else:
            datocrudo=form.data["ultrafile"]

            datoprocesado=datocrudo.split(",;,")

            for i in range (len(datoprocesado)):
                datoprocesado[i]=datoprocesado[i].split(",")

            ####### identifica las columnas y crea los objetos que me interesanself.
            colOrderId = None#Esta la tengo que pasar a datetime
            colPadron = None
            colCliente = None#Esta la tengo que pasar a datetime


            for i in range(len(datoprocesado[0])):
                if datoprocesado[0][i] == "ORDERID":
                    #print("columna creación en: " + str(i))
                    colOrderId = i

                if datoprocesado[0][i] == "INTERNALSPECID":
                    #print("columna transaction en: " + str(i))
                    colPadron = i

                if datoprocesado[0][i] == "CUSTOMERNAME":
                    #print("columna Horizonteini en: " + str(i))
                    colCliente = i

            print("guardando..")
            for i in range(1,len(datoprocesado)):


                    OrderInfo.objects.get_or_create(orderId=datoprocesado[i][colOrderId],padron=datoprocesado[i][colPadron], cliente=datoprocesado[i][colCliente])

            print("completado!")
    else:
        form = PruebaModForm()

    return render(request, template_name, {'form':form})









###############################################33

def carga_prog(request):
    pruebamods = PruebaMod.objects.all()
    posts= "HOLA Q ASE"
    template_name = 'blog/cargaprog.html'

    if request.method == "POST":
        form = PruebaModForm(request.POST)
        if form.is_valid():


            datocrudo=form.cleaned_data["ultrafile"]
            datoprocesado=datocrudo.split(";")

            #PruebaTabla.objects.create(item1=datoprocesado[0],item2=datoprocesado[1],item3=datoprocesado[2])

            post = form.save(commit=False)

            post.save()

        else:
            datocrudo=form.data["ultrafile"]
            '''
            f = StringIO(datocrudo)
            reader = list(csv.reader(f, delimiter=','))
            print("hola")
            for row in reader:
                print('\t'.join(row))
                print("siguiente linea")
            #print(reader)
            '''
            datoprocesado=datocrudo.split(",;,")
            #print("datoprocesado1:")
            #print(datoprocesado)
            #print("Largo: " + str(len(datoprocesado)))
            for i in range (len(datoprocesado)):
                datoprocesado[i]=datoprocesado[i].split(",")

            #print("datoprocesado2:")
            #print(datoprocesado)
            '''
            print(datoprocesado[0])
            print("otro metodo:")

            print ((str.strip, s_inner.split(',')) for s_inner in datocrudo.split(";"))
            print("tercer metodo:")
            x = csv.reader(datocrudo)
            list(x)
            '''
            ####### identifica las columnas y crea los objetos que me interesanself.
            colFecha = None#Esta la tengo que pasar a datetime
            colTransindex = None
            colHorini = None#Esta la tengo que pasar a datetime
            colHorfin = None#Esta la tengo que pasar a datetime






            for i in range(len(datoprocesado[0])):
                if datoprocesado[0][i] == "CREACION_PROGRAMACION":
                    #print("columna creación en: " + str(i))
                    colFecha = i

                if datoprocesado[0][i] == "TRANSACTIONINDEX":
                    #print("columna transaction en: " + str(i))
                    colTransindex = i

                if datoprocesado[0][i] == "Horizonteini":
                    #print("columna Horizonteini en: " + str(i))
                    colHorini = i

                if datoprocesado[0][i] == "Horizontefin":
                    #print("columna Horizontefin en: " + str(i))
                    colHorfin= i

            '''
            #ejemplo

            obj, created = Person.objects.get_or_create(
                first_name='John',
                last_name='Lennon',
                defaults={'birthday': date(1940, 10, 9)},
            )
            '''

            fecha_programa_datetime=datetime.strptime(datoprocesado[1][colFecha], "%d-%m-%Y %H:%M")
            fecha_programa_horini=fecha_programa_datetime.replace(hour=0, minute=0, second=0)
            fecha_programa_horfin=fecha_programa_horini + timedelta(days=1)
            #print("fecha programa")
            #print(fecha_programa_datetime)

            OrdenProg.objects.get_or_create(fecha_programa=fecha_programa_datetime, transaction_index=datoprocesado[1][colTransindex], horizonteini=fecha_programa_horini, horizontefin=fecha_programa_horfin )

            #################
            #################
            ## guardo el objeto DetalleProg por cada fila de la tabla procesada

            colworkcenter = None
            colorderid = None
            coldateini = None
            coldatefin = None
            colqin = None
            colidprev = None
            colidpost = None
            coldatefinajust = None
            colturno = None


            #print("Largo: " + str(len(datoprocesado[0])))
            for j in range(1,len(datoprocesado[0])):
                if datoprocesado[0][j] == "WORKCENTERID":
                    #print("columna colworkcenter en: " + str(j))
                    colworkcenter = j
                if datoprocesado[0][j] == "ORDERID":
                    #print("columna colorderid en: " + str(j))
                    colorderid = j
                if datoprocesado[0][j] == "SETUPSTARTDATE":
                    #print("columna dateini en: " + str(j))
                    coldateini = j
                if datoprocesado[0][j] == "RUNENDDATE":
                    #print("columna datefin en: " + str(j))
                    coldatefin = j
                if datoprocesado[0][j] == "QUANTITYIN":
                    #print("columna qin en: " + str(j))
                    colqin = j
                if datoprocesado[0][j] == "Fecha Termino Ajustada":
                    #print("columna datefinajust en: " + str(j))
                    coldatefinajust = j
                if datoprocesado[0][j] == "Turno":
                    #print("columna turno en: " + str(j))
                    colturno = j
            #print("Completado!!!!")

            for i in range(1,len(datoprocesado)):
                #try:
                    #print(OrdenProg.objects.all())



                    #print(datoprocesado[i])

                    datefinajustada_datetime = datetime.strptime(datoprocesado[i][coldatefinajust], "%d-%m-%Y")#"%d-%m-%Y %H:%M"
                    dateini_datetime = datetime.strptime(datoprocesado[i][coldateini], "%d-%m-%Y %H:%M")#"%d-%m-%Y %H:%M"
                    datefin_datetime = datetime.strptime(datoprocesado[i][coldatefin], "%d-%m-%Y %H:%M")#"%d-%m-%Y %H:%M"
                    cantQin=int(datoprocesado[i][colqin])
                    print("datefinajustada: " + str(datefinajustada_datetime))
                    print(OrdenProg.objects.filter(fecha_programa=fecha_programa_datetime, transaction_index=datoprocesado[1][colTransindex])[0])
                    print(datoprocesado[i][colworkcenter])
                    print(datoprocesado[i][colorderid])
                    print(datoprocesado[i][coldateini])
                    print(datoprocesado[i][coldatefin])
                    print(datoprocesado[i][colqin])
                    print(fecha_programa_datetime)
                    print(datoprocesado[i][colturno])
                    print(datoprocesado[i][colorderid])


                    DetalleProg.objects.get_or_create(programma=OrdenProg.objects.filter(fecha_programa=fecha_programa_datetime, transaction_index=datoprocesado[1][colTransindex])[0]  ,workcenter=datoprocesado[i][colworkcenter],orderId=datoprocesado[i][colorderid], dateini=dateini_datetime, datefin=datefin_datetime,qIn=cantQin, datefinajustada= datefinajustada_datetime , turno=datoprocesado[i][colturno], orderIdPrev=datoprocesado[i][colorderid], orderIdPost=datoprocesado[i][colorderid])


                #except:

                    #print("hola")



            #PruebaTabla.objects.create(item1="form no valido11 !!", item2=datoprocesado[0], item3=datoprocesado,)



    else:
        form = PruebaModForm()

    return render(request, template_name, {'form':form})




def prueba_ultimate(request):
    pruebamods = PruebaMod.objects.all()
    posts= "HOLA Q ASE"
    template_name = 'blog/pruebaultimate.html'
    redirec_field_name = 'blog/pruebaultimate.html'

    if request.method == "POST":
        form = PruebaModForm(request.POST)
        if form.is_valid():

            '''
            ##Ejemplo de cómo crear un objeto de otra clase al llenar el form (para hacer el parse el ultimatefile y generar filas de info productiva)
            ##Se llena form de producto y si la categoría no existe, se crea el objeto de una categoría nueva (model Category)
            if form.is_valid():
                c = form.cleaned_data["category"]
                category = Category.objects.filter(name=c).first()
                if not category:
                    category = Category.objects.create(name=c)
            product = form.save(commit=False)
            product.category = category
            product.save()

            '''
            datocrudo=form.cleaned_data["ultrafile"]
            datoprocesado=datocrudo.split(",")

            PruebaTabla.objects.create(item1=datoprocesado[0],item2=datoprocesado[1],item3=datoprocesado[2])




            post = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            #return redirect('post_detail', pk=post.pk)
    else:
        form = PruebaModForm()



    return render(request, template_name, {'pruebamods':pruebamods, 'posts':posts, 'form':form})



def create_book_with_authors(request):
    template_name = 'blog/create_with_author.html'
    if request.method == 'GET':
        bookform = BookModelForm(request.GET or None)
        formset = AuthorFormset(queryset=Author.objects.none())
    elif request.method == 'POST':
        bookform = BookModelForm(request.POST)
        formset = AuthorFormset(request.POST)
        if bookform.is_valid() and formset.is_valid():
            # first save this book, as its reference will be used in `Author`
            book = bookform.save()
            for form in formset:
                # so that `book` instance can be attached.
                author = form.save(commit=False)
                author.book = book
                author.save()
            return redirect('blog:book_list')
    return render(request, template_name, {
        'bookform': bookform,
        'formset': formset,
    })

def create_book_model_form(request):
    template_name = 'blog/create_normal.html'
    heading_message = 'Model Formset Demo'
    if request.method == 'GET':
        # we don't want to display the already saved model instances
        formset = BookModelFormset(queryset=Book.objects.none())
    elif request.method == 'POST':
        formset = BookModelFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # only save if name is present
                if form.cleaned_data.get('name'):
                    form.save()
            return redirect('book_list')
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })




#Para el ejemplo de dynamic form creation
def create_book_normal(request):
    template_name = 'blog/create_normal.html'
    heading_message = 'Formset Demo'
    if request.method == 'GET':
        formset = BookFormset(request.GET or None)
    elif request.method == 'POST':
        formset = BookFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # extract name from each form and save
                name = form.cleaned_data.get('name')
                # save book instance
                if name:
                    Book(name=name).save()
            # once all books are saved, redirect to book list view
            return redirect('book_normal')
            #return redirect('book_list')
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })








def solcambiosss(request):

    return render(request, 'blog/solicitud_cambio.html')


def listaprodid(request):
    lista = ProdID.objects.all() #Tb podría haber sido filter
    context= {'lista_a_mostrar': lista}
    return render(request, 'blog/prodid_list.html', context)


class ProdIDListView(ListView):
    login_url = '/login/'
    #redirec_field_name = 'blog/post_detail.html'



    model = ProdID


    #redirect_field_name = 'blog/prodid_list.html'


    def get_queryset(self):
        return ProdID.objects.filter(published_date__isnull=True).order_by('-published_date')#sql query


def CargaCSV2(request):
    login_url = '/login/'
    redirec_field_name = 'blog/post_detail.html'
    with open("prueba2.csv") as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            _, created = ProdID.objects.get_or_create(
                transactindex =row[0],
                plantid=row[1],
                workcenter=row[2],
                orderid=row[4],
                title=row[4]+row[2],
                #middle_name=row[2],
                )

    def get_queryset(self):
        return ProdID.objects.filter(published_date__isnull=True).order_by('-published_date')#sql query
            # creates a tuple of the new object or
            # current object and a boolean of if it was created
    lista = ProdID.objects.all() #Tb podría haber sido filter
    context= {'lista_a_mostrar': lista}
    return render(request, 'blog/prodid_list.html', context)





def CargaCSV1(request):
    login_url = '/login/'
    redirec_field_name = 'blog/post_detail.html'
    with open("prueba.csv") as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            _, created = appointment.objects.get_or_create(
                title=row[0],
                text=row[1],
                #middle_name=row[2],
                )

    def get_queryset(self):
        return appointment.objects.filter(published_date__isnull=True).order_by('-published_date')#sql query
            # creates a tuple of the new object or
            # current object and a boolean of if it was created
    return render(request, 'blog/base.html')

def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'contact.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})





def product(x,y):
    return x*y

def tomanombre():
    return SolCamb.objects.all()[:5]


class CreateOCIView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    #redirec_field_name = 'blog/post_detail.html'

    form_class = OCImportacionForm

    model = OCImportacion

class appointmentCreate(LoginRequiredMixin, CreateView):
    model = appointment
    form_class = AppointmentForm

    def get_initial(self):
      #patient = self.request.GET.get('patient')
      patient = "dsds"
      location = "Hola Q hace"
      producto= product(3,5)
      tomanomb = tomanombre()


      return {
        'Patient': patient,
        'Location': location,
        #'Duration':producto,
        'Clinician': tomanomb,
      }



class AboutView(TemplateView):
    template_name = 'about.html'

class SolCambDetailView(DetailView):
    model = SolCamb

class SolCambListView( ListView):

    model = SolCamb
    redirect_field_name = 'blog/post_list.html'

    def get_queryset(self):
        return SolCamb.objects.filter(published_date__isnull=True).order_by('-published_date')#sql query

'''
class SolCambListView(TemplateView):
    template_name = 'solcamb_list.html'

    model = SolCamb

    def get_queryset(self):
        return SolCamb.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')#sql query

    '''

class CreateSolCambView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirec_field_name = 'blog/solcamb_detail.html'

    form_class = SolCambForm

    model = SolCamb

    def get_initial(self):
          #patient = self.request.GET.get('patient')
          cliente = "Juanito"

          return {
            'cliente': cliente,
            }


class PostListView(ListView):
    model = Post


    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')#sql query

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirec_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirec_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')


########################
########################

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)



@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def solcamb_publish(request, pk):
    solcamb = get_object_or_404(SolCamb, pk=pk)
    solcamb.publish()
    return redirect('solcamb_detail', pk=pk)



'''
@login_required
def editprofile(request):
    try:
    userprofile = UserProfiles.objects.get(user=request.user)
    except UserProfiles.DoesNotExist:
       return render(request, 'profile_edit.html', {'form':UserProfileForm()})
    form = UserProfileForm(instance=userprofile)
    return render(request, 'profile_edit.html', {'form':form})
'''

# Create your views here.
