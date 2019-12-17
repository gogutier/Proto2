import telepot
import time

token="798683442:AAFaNBMaTRt5Cu7FemBpYFbM0xbnezInOMA"
TelegramBot = telepot.Bot(token)

print(TelegramBot.getMe())

print(TelegramBot.getUpdates(746598385+1))

chat_id= 306739207

TelegramBot.sendMessage(chat_id, 'I do not understand you, Sir!')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        TelegramBot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))

TelegramBot.message_loop(handle)

print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
