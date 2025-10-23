import requests
import time
from telebot import TeleBot


token = '7353840144:AAFVAHgDOVlJ7UMoHmywROb0u6KuG8vAD6Q'
bot = TeleBot(token)
chat_id = '-1002535850677'
from_chat_id = '7353840144'
say = ''
ans = ''
k = 0

@bot.message_handler(commands=["start"])
def start_message(message):
   bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEO04FoY_Obj4K5W6jkcmdW7nebtJPqdwAC1RoAAhbmYUuVzr2lqcjHbDYE")
   bot.send_message(chat_id = message.chat.id, text = "Привет, я принимаю ответы на разные вопросы). Если нужна какя-то помощь, используйте команду help. узнать вопрос - question, а ответить - answer или chekc_ans. Не забывайте ставить слеш перед командой)")
 
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(chat_id = message.chat.id, text = '''Вам нужна помощь или не помните команды? Значит, вам сюда!
                     /question - узнать вопрос 
                     /answer - ответить на вопрос без проверки и отправке лично мне
                     /check_ans - ответить на вопрос с проверкой (расширенные вопросы на подумать на эту команду не распространяются)
                     Это пока все, но будут обновления и новые функции)''')

@bot.message_handler(commands=["kreker"])
def question_special(message):
    msg = bot.send_message(chat_id = message.chat.id, text = "Пиши вопрос, я готов)")
    bot.register_next_step_handler(msg, qwerty)
def qwerty(message): 
   global say   
   say = message.text
   rtxt = 'Ваш вопрос был принят: ' + say
   bot.send_message(chat_id = message.chat.id, text = rtxt)
   
@bot.message_handler(commands=["saturn"])
def answer_special(message):
    msg = bot.send_message(chat_id = message.chat.id, text = "Пиши ответ, я готов)")
    bot.register_next_step_handler(msg, wasd)
def wasd(message):    
   global ans
   ans = message.text
   rtxt = 'Ваш ответ был принят: ' + ans
   bot.send_message(chat_id = message.chat.id, text = rtxt)   
   
@bot.message_handler(commands=["question"])
def question(message):
    txt = '''Уже готов к вопросу? Тогда лови! 
    -----------------------------------------
    ''' + say + '''
    -----------------------------------------'''
    bot.send_message(chat_id = message.chat.id, text = txt)

 
@bot.message_handler(commands=['answer'])
def text_message(message):
   bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEO03toY9-MObX5jHq-42ux2oxM41Lr5AAC2S0AArLh2Ul_cy4QprS86jYE")
   msg = bot.send_message(message.chat.id, 'Ваш итоговый ответ?')
   bot.register_next_step_handler(msg, answer)   
def answer(message):
   bot.send_message(chat_id, message.from_user.id)
   bot.forward_message(chat_id, message.chat.id, message.message_id)
   bot.send_message(message.chat.id, 'Ответ отправлен)')
   
@bot.message_handler(commands=['check_ans'])
def answer_big(message):
   bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEO03toY9-MObX5jHq-42ux2oxM41Lr5AAC2S0AArLh2Ul_cy4QprS86jYE")
   msg = bot.send_message(message.chat.id, 'Ваш итоговый ответ?')
   bot.register_next_step_handler(msg, answer_check)
def answer_check(message):
   bot.send_message(chat_id, message.from_user.id)
   bot.forward_message(chat_id, message.chat.id, message.message_id)
   if message.text == ans:
      bot.send_message(message.chat.id, 'Молодец, твой ответ правильный!')
   elif message.text != ans:
      bot.send_message(message.chat.id, 'Неверно, подумай еще...')

@bot.message_handler(commands=["rat"])
def comeback(message):
   txt = 'Кому хочешь ответить?'
   msg = bot.send_message(chat_id = message.chat.id, text = txt)
   bot.register_next_step_handler(msg, comes)
def comes(message):
   txt = 'Что хочешь ответить?'
   global id
   id = message.text
   msg = bot.send_message(chat_id = message.chat.id, text = txt)
   bot.register_next_step_handler(msg, come)
def come(message):
   txt = 'Создатель отвечает: ' + message.text
   bot.send_message(chat_id = id, text=txt)

while True == True:
   time.sleep(800)
   k += 1

bot.polling(non_stop=True)


