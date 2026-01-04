import os
from telebot import TeleBot

token = os.environ.get("BOT_TOKEN")
bot = TeleBot(token)

chat_id = '-1002535850677'

say = ''
ans = ''

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_sticker(
        message.chat.id,
        "CAACAgIAAxkBAAEO04FoY_Obj4K5W6jkcmdW7nebtJPqdwAC1RoAAhbmYUuVzr2lqcjHbDYE"
    )
    bot.send_message(
        chat_id=message.chat.id,
        text="Привет, я принимаю ответы на разные вопросы). "
             "Если нужна помощь — /help. "
             "Узнать вопрос — /question, "
             "ответить — /answer или /check_ans."
    )

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=(
            "/question — узнать вопрос\n"
            "/answer — ответить без проверки\n"
            "/check_ans — ответить с проверкой\n"
        )
    )

@bot.message_handler(commands=["kreker"])
def question_special(message):
    msg = bot.send_message(message.chat.id, "Пиши вопрос, я готов)")
    bot.register_next_step_handler(msg, qwerty)

def qwerty(message):
    global say
    say = message.text
    bot.send_message(message.chat.id, f"Ваш вопрос был принят: {say}")

@bot.message_handler(commands=["saturn"])
def answer_special(message):
    msg = bot.send_message(message.chat.id, "Пиши ответ, я готов)")
    bot.register_next_step_handler(msg, wasd)

def wasd(message):
    global ans
    ans = message.text
    bot.send_message(message.chat.id, f"Ваш ответ был принят: {ans}")

@bot.message_handler(commands=["question"])
def question(message):
    bot.send_message(
        message.chat.id,
        f"Уже готов к вопросу?\n"
        f"----------------------\n"
        f"{say}\n"
        f"----------------------"
    )

@bot.message_handler(commands=['answer'])
def text_message(message):
    bot.send_sticker(
        message.chat.id,
        "CAACAgIAAxkBAAEO03toY9-MObX5jHq-42ux2oxM41Lr5AAC2S0AArLh2Ul_cy4QprS86jYE"
    )
    msg = bot.send_message(message.chat.id, "Ваш итоговый ответ?")
    bot.register_next_step_handler(msg, answer)

def answer(message):
    bot.send_message(chat_id, str(message.from_user.id))
    bot.forward_message(chat_id, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Ответ отправлен)")

@bot.message_handler(commands=['check_ans'])
def answer_big(message):
    msg = bot.send_message(message.chat.id, "Ваш итоговый ответ?")
    bot.register_next_step_handler(msg, answer_check)

def answer_check(message):
    bot.send_message(chat_id, str(message.from_user.id))
    bot.forward_message(chat_id, message.chat.id, message.message_id)

    if message.text == ans:
        bot.send_message(message.chat.id, "Молодец, твой ответ правильный!")
    else:
        bot.send_message(message.chat.id, "Неверно, подумай еще...")

@bot.message_handler(commands=["rat"])
def comeback(message):
    msg = bot.send_message(message.chat.id, "Кому хочешь ответить?")
    bot.register_next_step_handler(msg, comes)

def comes(message):
    global target_chat_id
    target_chat_id = message.text
    msg = bot.send_message(message.chat.id, "Что хочешь ответить?")
    bot.register_next_step_handler(msg, come)

def come(message):
    bot.send_message(target_chat_id, f"Создатель отвечает: {message.text}")

if __name__ == "__main__":
    bot.infinity_polling()

