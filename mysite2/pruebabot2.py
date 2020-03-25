import telepot
import time

token="906256196:AAFQPbKjDD0MkctsKcX4cI_t39kZu8Y_qnw"
TelegramBot = telepot.Bot(token)

print(TelegramBot.getMe())

#print(TelegramBot.getUpdates(746598385+1))

chat_id= 306739207 # Este es mi chatID (GG)

#TelegramBot.sendMessage(chat_id, 'Hola! Cómo te llamas?')

#Matriz estados por UsuaRIO


#matriz_estados=[["chat_id","estado","nombre", "auxiliar", "ultima entrada", "ultima respuesta"] ] #ahora esta será una lista de diccionarios.

matriz_estados=[ ]


estadoz="Inicio"





def respuesta(text, chat_id): #devuelve el texto de la respuesta y el nuevo estado en que está.

    texto=text.lower()
    respuestaz=""

    global matriz_estados

    chat_dict = next((item for item in matriz_estados if item["chat_id"] == chat_id), False)

    #print("estadoz en respuesta():")
    print(chat_dict["estado"])

    estadoz=chat_dict["estado"]




    respuesta="Mmm no me queda claro lo que dices...\n puedes preguntarme usando palabras clave como 'ID', 'stock', etc"
    estado="Inicio"
    estadoz=chat_dict["estado"]
    print("estadoz: "+estadoz)
    if estadoz=="Inicio":
        if ("hola" in texto):
            if chat_dict["nombre"]== "vacio":
                respuesta= "hola! Cómo te llamas?"
                estado="preguntanombre1"
            else:
                respuesta = "Hola "+ chat_dict["nombre"] +", en qué te puedo ayudar? \n (preguntar por  'Aviso', 'Alerta' )"


        if ("aviso" in texto or "alerta" in texto or "alarma" in texto):
            respuesta = "Ok, primero dime qué tipo de alarma quieres activar \n responder con 'ingreso', 'carga', 'despacho' "
            estado="preguntaalarma2"

    elif estadoz=="preguntaalarma2":
        respuesta="Ok, entonces se programará aviso para"
        flag=0
        if ("ingreso" in texto):
            flag=1
            respuesta+=" ingreso."
            estado="preguntaingreso"
        elif ("carga" in texto):
            flag=1
            respuesta+=" carga."
            estado="preguntacarga"

        elif ("despacho" in texto):
            flag=1
            respuesta+=" despacho."
            estado="preguntadespacho"
        elif ("cancelar" in texto):
            flag=2

        if flag==1:
            respuesta+=" Ahora dime el número de ID de la orden"

        elif flag==2:
            respuesta="Ok."
            estado="Inicio"

        else:
            respuesta="No entendí lo que quieres decir, por favor responde con 'ingreso', 'carga', 'despacho'. También puedes responder 'Cancelar' "
            estado="preguntaalarma2"


    elif estadoz=="preguntaingreso":

        respuesta= "ok, se generará una alarma para cuando la ID "+ texto +" ingrese a bpt"
        estado="Inicio"

    elif estadoz=="preguntacarga":
        respuesta= "ok, se generará una alarma para cuando la ID "+ texto + " inicie su carga a camión"
        estado="Inicio"

    elif estadoz=="preguntadespacho":
        respuesta= "ok, se generará una alarma para cuando la ID "+ texto + " sea despachada en camión"
        estado="Inicio"

    elif estadoz=="preguntanombre1":
        respuesta = "Ok, recordaré tu nombre como "+ texto + ", está bien? \n (responder si/no)"
        chat_dict["nombre"] = texto
        estado="preguntanombre2"

    elif estadoz=="preguntanombre2":
        if texto=="si" or texto=="sí" or texto=="ok":
            respuesta = "Perfecto, "+ chat_dict["nombre"]
            estado="Inicio"
        else:
            respuesta = "Mm ok.."
            chat_dict["nombre"] = "vacio"
            estado="Inicio"

    print("devolviendo: R:" + respuesta+ " E:" + estado)
    return (respuesta, estado)




def handle(msg):


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
        TelegramBot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))

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

TelegramBot.message_loop(handle)




print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
