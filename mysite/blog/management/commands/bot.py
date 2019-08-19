from django.core.management.base import BaseCommand, CommandError
from blog.models import OrdenCorrplan as OrdenCorrplan
from blog.models import Maquinas as Maquinas
import telepot
import time

token="906256196:AAFQPbKjDD0MkctsKcX4cI_t39kZu8Y_qnw"
TelegramBot = telepot.Bot(token)

print(TelegramBot.getMe())



chat_id= 306739207

TelegramBot.sendMessage(chat_id, 'Hola! Cómo te llamas?')

#Matriz estados por UsuaRIO


#matriz_estados=[["chat_id","estado","nombre", "auxiliar", "ultima entrada"] ] #ahora esta será una lista de diccionarios.

matriz_estados=[ ]


estadoz="Inicio"

def respuesta(text, chat_id):

    respuestaz=""

    global matriz_estados

    chat_dict = next((item for item in matriz_estados if item["chat_id"] == chat_id), False)

    #print("estadoz en respuesta():")
    #print(estadoz)
    estado=chat_dict["estado"]

    if ("id" in text.lower()):
        respuestaz="ah ok, quieres saber el estado de una ID, cierto? Puedes decirme el ID de la orden?"
        estado="ID1"
        #print("estado en respuesta():")


    elif (" inventario " in text.lower()) or (" stock " in text.lower()):
        respuestaz="OK dime de qué calle o sector quieres que te indique el nivel de inventario \n También puedo estableces alarmas!"
        estado="INV1"
            #print("estado en respuesta():")
            #print(estado)




    elif (estado=="ID1" and ( "si" in text.lower() or  "sì" in text.lower() or "sí" in text.lower() or "yes" in text.lower()  )):
        respuestaz="Mmm ok, dame el id de la orden por favor"
        estado="ID1"
            #print("estado en respuesta():")
            #print(estado)
    elif (estado=="ID1" and ( "no" in text.lower() or  "not" in text.lower())):
        respuestaz="ok, quedo atento"
        estado="inicio"
            #print("estado en respuesta():")
            #print(estado)

    elif( estado=="ID1" ):

        try:
            orden= OrdenCorrplan.objects.filter(order_id= text.lower()).order_by('fecha_inicio')[0]

            respuestaz="Mmm ok, esta Id se está haciendo en la máquina " + str(orden.maquina) + " y partiendo en la fecha " + str(orden.fecha_inicio)+ "\nQuieres consultar por otra ID?"
            estado="ID1"
        except:

            respuestaz="Creo que esa Id no existe..o ya está completada. Por ahora sólo puedo ver IDs programadas \n Quieres consultar denuevo?"

            estado="ID1"





    elif (estado=="ID2"):
            respuestaz="La hora de inicio de producción de tu ID se estima a las %$#%#$. Quieres que te avise una vez entre a producción"
            estado="Inicio"
            #print("estado en respuesta():")
            #print(estado)



    elif (text =="Mirna" or text =="mirna" or text =="MIRNA"):
            respuestaz="Vaya, veo que eres muy bonita"
            #print("estado en respuesta():")
            #print(estado)
            estado="Inicio"



    else:
        respuestaz = "Mmm no me queda claro lo que dices...\n puedes preguntarme usando palabras clave como 'ID', 'stock', etc"
        #print("estado en respuesta():")
        #print(estado)


    return (respuestaz, estado)




def handle(msg):


    global estadoz
    global matriz_estados

    chat_dict = {}


    content_type, chat_type, chat_id= telepot.glance(msg)

    estadoy=estadoz
    flag=0
    indice_chat=-1





    if  (   next((item for item in matriz_estados if item["chat_id"] == chat_id), False)  ) == False:

        matriz_estados.append({"chat_id": chat_id, "estado": estadoy, "auxiliar": "auxiliar", "ultima entrada":  msg["text"] , "ultima respuesta": "mnuevo chat"})
        #["chat_id","estado","nombre", "auxiliar", "ultima entrada"]
    else:
        chat_dict = next((item for item in matriz_estados if item["chat_id"] == chat_id), False)


    if content_type == 'text':
        TelegramBot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))

        #respuestaz =respuesta(msg["text"])

        chat_dict["ultima entrada"] = msg["text"]

        mensaje_respuesta, chat_dict["estado"]= respuesta(msg["text"], chat_id )



        TelegramBot.sendMessage(chat_id, mensaje_respuesta )

        chat_dict["ultima respuesta"]=mensaje_respuesta

        #print("estado en handle:")
        #print(estadoz)

    print("matriz estados completa:")
    print(matriz_estados)

TelegramBot.message_loop(handle)




print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
