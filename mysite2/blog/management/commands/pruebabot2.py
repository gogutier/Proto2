import telepot
import time
from django.db.models import Q
from blog.models import MovPallets as MovPallets
from blog.models import Pallet as Pallet
from blog.models import AlertaBot as AlertaBot
from datetime import datetime, timedelta

token="906256196:AAFQPbKjDD0MkctsKcX4cI_t39kZu8Y_qnw" #Oficial
#token="798683442:AAFaNBMaTRt5Cu7FemBpYFbM0xbnezInOMA" #Prueba

TelegramBot = telepot.Bot(token)

print(TelegramBot.getMe())

#print(TelegramBot.getUpdates(746598385+1))

chat_id= 306739207 # Este es mi chatID (GG)

#TelegramBot.sendMessage(chat_id, 'Hola! Cómo te llamas?')

#Matriz estados por UsuaRIO


#matriz_estados=[["chat_id","estado","nombre", "auxiliar", "ultima entrada", "ultima respuesta"] ] #ahora esta será una lista de diccionarios.

matriz_estados=[ ]


estadoz="Inicio"



def checkeventos():
    print("datetime.now():")
    print(datetime.now())
    for alerta in AlertaBot.objects.filter(flagevento=False):
        if alerta.tipoevento == "ingreso":
            print("buscando ingresos para esta ID: "+ alerta.order_id)
            listaentrada=Q()
            if MovPallets.objects.filter( Q(DESTINATION="PLL") | Q(DESTINATION="RP1") | Q(DESTINATION="PT10"), ORDERID=alerta.order_id, EVENTDATETIME__gte=alerta.fechaalerta).order_by("-EVENTDATETIME"):
                busqueda=MovPallets.objects.filter( Q(DESTINATION="PLL") | Q(DESTINATION="RP1") | Q(DESTINATION="PT10"), ORDERID=alerta.order_id, EVENTDATETIME__gte=alerta.fechaalerta).order_by("-EVENTDATETIME")[0]
                TelegramBot.sendMessage(alerta.chat_id, 'Hola! un pallet de la orden ' + alerta.order_id+" ingresó a la bodega por la ubicación " + busqueda.DESTINATION + " a las " + (busqueda.EVENTDATETIME).strftime("%H:%M:%S del %d-%m-%y") +"." )
                alerta.fechaevento=busqueda.EVENTDATETIME
                alerta.flagevento=True
                alerta.save()

        if alerta.tipoevento == "carga":
            print("buscando cargas para esta ID: "+ alerta.order_id)
            listaentrada=Q()
            if MovPallets.objects.filter( Q(DESTINATION="AN1") | Q(DESTINATION="AN2") | Q(DESTINATION="AN3") | Q(DESTINATION="AN4") | Q(DESTINATION="AN5") | Q(DESTINATION="AN6") | Q(DESTINATION="AN7") | Q(DESTINATION="AN8") | Q(DESTINATION="AN9"), ORDERID=alerta.order_id, EVENTDATETIME__gte=alerta.fechaalerta).order_by("-EVENTDATETIME"):
                busqueda=MovPallets.objects.filter( Q(DESTINATION="AN1") | Q(DESTINATION="AN2") | Q(DESTINATION="AN3") | Q(DESTINATION="AN4") | Q(DESTINATION="AN5") | Q(DESTINATION="AN6") | Q(DESTINATION="AN7") | Q(DESTINATION="AN8") | Q(DESTINATION="AN9"), ORDERID=alerta.order_id, EVENTDATETIME__gte=alerta.fechaalerta).order_by("-EVENTDATETIME")[0]
                TelegramBot.sendMessage(alerta.chat_id, 'Hola! un pallet de la orden ' + alerta.order_id+" fue cargado a camión por " + busqueda.OPERATORCODENAME + " a las " + (busqueda.EVENTDATETIME).strftime("%H:%M:%S del %d-%m-%y") +"." )
                alerta.fechaevento=busqueda.EVENTDATETIME
                alerta.flagevento=True
                alerta.save()

        if alerta.tipoevento == "despacho":
            print("buscando despachos para esta ID: "+ alerta.order_id)
            listaentrada=Q()
            if MovPallets.objects.filter( DESTINATION="TRUCK", ORDERID=alerta.order_id, EVENTDATETIME__gte=alerta.fechaalerta).order_by("-EVENTDATETIME"):

                busqueda=MovPallets.objects.filter( DESTINATION="TRUCK", ORDERID=alerta.order_id, EVENTDATETIME__gte=alerta.fechaalerta).order_by("-EVENTDATETIME")[0]
                TelegramBot.sendMessage(alerta.chat_id, 'Hola! un pallet de la orden ' + alerta.order_id+" ya fue despachado a las " + (busqueda.EVENTDATETIME).strftime("%H:%M:%S del %d-%m-%y") +" bajo la remisión <b>"+ str(busqueda.remision) +"</b>." + " Puedes ver más detalles en control.corrupac.cl:8090/busqueda_remision/", parse_mode='HTML') #interlink.corrupac.cl/pagegenerator.dll/OrderStatusSearch?%21+SplitN+=isNULL%28O.SplitNumber%2C0%29%3D0&O.OrderID+like="+str(busqueda.ORDERID) + "\n (recuerda que debes estar logeado en el sitio)" ) #http://interlink.corrupac.cl/pagegenerator.dll/OrderStatusSearch?%21+SplitN+=isNULL%28O.SplitNumber%2C0%29%3D0&O.OrderID+like=6632252
                alerta.fechaevento=busqueda.EVENTDATETIME
                alerta.flagevento=True
                alerta.save()

def respuesta(text, chat_id): #devuelve el texto de la respuesta y el nuevo estado en que está.

    texto=text.lower()
    respuestaz=""

    global matriz_estados

    chat_dict = next((item for item in matriz_estados if item["chat_id"] == chat_id), False)

    #print("estadoz en respuesta():")
    print(chat_dict["estado"])

    estadoz=chat_dict["estado"]




    respuesta="Mmm no me queda claro lo que dices...\n puedes preguntarme usando palabras clave como 'alerta entrada a bpt', 'aviso despacho', 'Status ID' etc.."
    estado="Inicio"
    estadoz=chat_dict["estado"]
    print("estadoz: "+estadoz)

    if "gracias" in texto :
        respuesta="de nada!"
        estado="Inicio"

    elif "cancela" in texto :
        respuesta="ok, hasta la próxima!"
        estado="Inicio"

    elif "adios" in texto :
        respuesta="nos vemos!"
        estado="Inicio"

    elif "ayuda" in texto :
        respuesta="Por ahora sólo puedo establecer avisos para: Entrada a BPT, carga a camion y despacho a cliente. Para esto monitoreo los pallets de una ID y te aviso cuando el primero de ellos realice el movimiento consultado."
        estado="Inicio"

    elif "status" in texto :
        respuesta="Quieres conocer el status de una ID, cierto? Por favor dime el n° de ID."
        estado="status"

    elif estadoz == "status":

        if texto.isdigit() and len(texto)==7:
            respuesta= "El status de la ID "+ texto +" es: \n"
            respuesta += status(texto)
            estado="Inicio"
        else:
            respuesta="Mm creo que escribiste mal en ID, por favor revisa y vuelve a intentar."
            estado="status"



    elif estadoz=="Inicio":
        if ("hola" in texto):
            if chat_dict["nombre"]== "vacio":
                respuesta= "hola! Cómo te llamas?"
                estado="preguntanombre1"
            else:
                respuesta = "Hola "+ chat_dict["nombre"] +", en qué te puedo ayudar? \n (Puedo establecer 'Avisos', 'Alertas', etc.)"


        if ("avis" in texto or "alert" in texto or "alarm" in texto):
            respuesta = "Ok, primero dime qué tipo de alarma quieres activar \n responder con 'ingreso', 'carga', 'despacho' "
            estado="preguntaalarma2"

        if ("camion" in texto or "entrada" in texto or "ingres" in texto or "carg" in texto or "despach" in texto):
            if ("ingreso" in texto or "entrada" in texto):
                respuesta="Ok, entonces programaré un aviso de ingreso a bodega. Ahora dime el número de ID que te interesa monitorear."
                estado="preguntaingreso"
            elif ("carga" in texto or "camion" in texto or "camión" in texto):
                respuesta="Ok, entonces programaré un aviso de carga a camión. Ahora dime el número de ID que te interesa monitorear."
                estado="preguntacarga"
            elif ("despacho" in texto):
                respuesta="Ok, entonces programaré un aviso de despacho a cliente. Ahora dime el número de ID que te interesa monitorear."
                estado="preguntadespacho"


    elif estadoz=="preguntaalarma2":
        respuesta="entonces programaré aviso para"
        flag=0
        if ("ingreso" in texto or "entrada" in texto):
            flag=1
            respuesta+=" ingreso a BPT."
            estado="preguntaingreso"
        elif ("carga" in texto or "camion" in texto or "camión" in texto):
            flag=1
            respuesta+=" carga a camión."
            estado="preguntacarga"

        elif ("despacho" in texto):
            flag=1
            respuesta+=" despacho a cliente."
            estado="preguntadespacho"

        elif ("cancela" in texto):
            flag=2

        if flag==1:
            respuesta+=" Ahora dime el número de ID de la orden."

        elif flag==2:
            respuesta="Ok."
            estado="Inicio"

        else:
            respuesta="No entendí lo que quieres decir, por favor responde con 'ingreso', 'carga', 'despacho'. También puedes responder 'Cancelar'. "
            estado="preguntaalarma2"


    elif estadoz=="preguntaingreso":

        if texto.isdigit() and len(texto)==7:
            respuesta= "ok, te avisaré cuando la ID "+ texto +" ingrese a bpt"
            o, created = AlertaBot.objects.get_or_create(chat_id=chat_dict["chat_id"], order_id=texto, tipoevento="ingreso")
            o.fechaalerta=datetime.now()
            o.flagevento=False
            estado="Inicio"
        else:
            respuesta="Mm creo que escribiste mal en ID, por favor revisa y vuelve a intentar."
            estado="preguntaingreso"

    elif estadoz=="preguntacarga":
        if texto.isdigit() and len(texto)==7:
            respuesta= "ok, te avisaré cuando la ID "+ texto + " inicie su carga a camión."
            o, created = AlertaBot.objects.get_or_create(chat_id=chat_dict["chat_id"], order_id=texto, tipoevento="carga")
            o.fechaalerta=datetime.now()
            o.flagevento=False
            estado="Inicio"
        else:
            respuesta="Mm creo que escribiste mal en ID, por favor revisa y vuelve a intentar."
            estado="preguntacarga"

    elif estadoz=="preguntadespacho":
        if texto.isdigit() and len(texto)==7:
            respuesta= "ok, te avisaré cuando la ID "+ texto + " sea despachada a cliente."
            o, created = AlertaBot.objects.get_or_create(chat_id=chat_dict["chat_id"], order_id=texto, tipoevento="despacho")
            o.fechaalerta=datetime.now()
            o.flagevento=False
            o.save()
            estado="Inicio"
        else:
            respuesta="Mm creo que escribiste mal en ID, por favor revisa y vuelve a intentar."
            estado="preguntadespacho"

    elif estadoz=="preguntanombre1":
        respuesta = "Ok, recordaré tu nombre como "+ texto + ", está bien? \n (responder sí/no)."
        chat_dict["nombre"] = texto
        estado="preguntanombre2"


    elif estadoz=="preguntanombre2":
        if texto=="si" or texto=="sí" or texto=="ok":
            respuesta = "Perfecto, "+ chat_dict["nombre"]+", Ahora me puedes preguntar sobre alertas de ingreso a bodega, carga a camión, etc"
            estado="Inicio"
        else:
            respuesta = "Mm ok, entonces no te recordaré.."
            chat_dict["nombre"] = "vacio"
            estado="Inicio"

    print("devolviendo: R:" + respuesta+ " E:" + estado)
    return (respuesta, estado)

def status(id):

    #cuento el número de pallet en ubicacion andén ("en proceso de carga")
    #cuento el número de pallet en ubicacion TRUCK ("Despachados")
    listabodega=[]

    filtrocallesbptqs=Q()
    filtroandenqs=Q()



    listafiltroanden=["AN1","AN2","AN3","AN4","AN5","AN6","AN7","AN8","AN9"]
    listafiltrocallesbpt=["C01","C02","C03","C04","C05","C06","C07","C08","C09","C10","C11","C12","C13","B01","B02","B03","B04","B05","B06","B07","B08","B09","B10","B11","B12","B13","B14","B15","E01","E02","E03","E04","A01","A02","A03","A04","A05","A06","A07","PA1","PA2","PA3","PLL","RP1","PT10"]

    for item in listafiltroanden:#OJO acá falta incluir en el filtro para que considere sólo los pallets que entraron a PLL dentro del mismo turno
        filtroandenqs = filtroandenqs | Q(ubic=item)

    for item in listafiltrocallesbpt:#OJO acá falta incluir en el filtro para que considere sólo los pallets que entraron a PLL dentro del mismo turno
        filtrocallesbptqs = filtrocallesbptqs | Q(ubic=item)


    ntruck = Pallet.objects.filter(ubic="TRUCK", ORDERID=str(id)).count()
    nanden= Pallet.objects.filter(filtroandenqs, ORDERID=str(id)).count()
    nbodega= Pallet.objects.filter(filtrocallesbptqs , ORDERID=str(id)).count()

    respuesta=" Pallets despachados: "+str(ntruck)+ " \n Pallets cargándose en camión: "+ str(nanden)+"\n Pallets en bodega: "+str(nbodega)

    return(respuesta)

def handle(msg):

    try:
        global estadoz
        global matriz_estados

        chat_dict = {}

        content_type, chat_type, chat_id= telepot.glance(msg)

        estadoy=estadoz
        flag=0
        indice_chat=-1



        if  (   next((item for item in matriz_estados if item["chat_id"] == chat_id), False)  ) == False:

            matriz_estados.append({"chat_id": chat_id, "estado": "Inicio", "nombre": "vacio", "auxiliar": "auxiliar", "ultima entrada":  msg["text"] , "ultima respuesta": "nuevo chat"})
            chat_dict = next((item for item in matriz_estados if item["chat_id"] == chat_id), False)
            #["chat_id","estado","nombre", "auxiliar", "ultima entrada"]
        else:
            chat_dict = next((item for item in matriz_estados if item["chat_id"] == chat_id), False)
            print("Conversación ya existente")


        if content_type == 'text':
            #TelegramBot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))

            #respuestaz =respuesta(msg["text"])

            chat_dict["ultima entrada"] = msg["text"]

            mensaje_respuesta, chat_dict["estado"]= respuesta(msg["text"], chat_id )
            print("estado: "+ chat_dict["estado"])

            TelegramBot.sendMessage(chat_id, mensaje_respuesta )

            chat_dict["ultima respuesta"]=mensaje_respuesta

            #print("estado en handle:")
            #print(estadoz)

        print(" ")
        print("matriz estados final:")
        for chat in matriz_estados:
            print(chat)

    except Exception as e:
        print(e)



TelegramBot.message_loop(handle)

print ('Listening ...')

# Keep the program running.
while 1:
    try:
        time.sleep(10)
        print("ejecutando búsqueda de eventos...")
        checkeventos()
    except Exception as e:
        print("Error!")
        print(e)
