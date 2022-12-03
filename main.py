import telebot;
import types;
import message_api;
import random;
bot = telebot.TeleBot('5987833282:AAGUbvHQDirtaO1GzNuENM83J0lp5XG6fcw');
help = ['НИКАКОЙ ПОМОЩИ, ТОЛЬКО ХАРДКОР', 'НЕ СКАЖУ', 'я могу.. например.. поговорить с тобой']
r1 = ['дела? хмм... даже не знаю, какие дела вообще могут быть у робота?', 'да нормально вроде, у владельца не отключили свет, и то хорошо', 'ах**** б*** н****! ']
r2 = ['Героям Слава', 'БАМ БАМ БАМ', 'Батько наш Бандера...']
r3 = ['пока-пока', 'аривидерчи', 'не поминай лихом']
@bot.message_handler(content_types=['text'])
def get_text_messages(message):


        if message.text == "/start":
            bot.send_message(message.from_user.id, "Привет. я - бот, но не ИИ. созданый учеником для экзамена в академию ШАГ")
            bot.send_message(message.from_user.id,
                                                  "если чё, могу помочь. напиши помогите")
        if message.text == "чо пон":
            bot.send_message(message.from_user.id,
                             "зроз")
            bot.send_message(message.from_user.id,
                             "если чё, могу помочь. напиши помогите")



            if message.text == "ШАГ?":
                bot.send_message(message.from_user.id, "https://vinnitsa.itstep.org/   -  ШАГ - отличная компьюиерная академия, которая находится по всей Украине!")
            elif message.text == "помогите":
                bot.send_message(message.from_user.id, random.choice(help) )


            else:
                bot.send_message(message.from_user.id, "похоже, я не достаточно изучил ваш язык. я вас не понимаю")
                if message.text == "давай поговорим" :
                    bot.send_message(message.from_user.id, "давай, я люблю говорить! только очень плохо вас понимаю, по этому знаю мало фраз")
                    if message.text == "Как дела?" :
                    bot.send_message(message.from_user.id, random.choice(r1) )
                    if message.text == "Слава Украине" :
                    bot.send_message(message.from_user.id, random.choice(r2) )
                    if message.text == "Пока" :
                    bot.send_message(message.from_user.id, random.choice(r3) )



bot.polling(none_stop=True)