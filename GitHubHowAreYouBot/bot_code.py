import telebot
from telebot import types
import config

id = config.id
bot = telebot.TeleBot(config.token)

btn1 = types.KeyboardButton(text='жалоба')
btn2 = types.KeyboardButton(text='поделиться идеей')
btn3 = types.KeyboardButton(text='вопрос к руководству')
kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(btn1, btn2, btn3)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здравствуйте, для продолжения нажмите кнопки ниже', reply_markup=kb)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'жалоба':
        bot.send_message(message.chat.id, 'напишите вашу жалобу')
        print(
            f'{message.from_user.username} {message.from_user.first_name} {message.from_user.last_name} отпровляет жалобу...')
        bot.send_message(id,
                         f'{message.from_user.username} {message.from_user.first_name} {message.from_user.last_name} отпровляет жалобу...')


    elif message.text == 'поделиться идеей':
        bot.send_message(message.chat.id, 'напишите вашу идею')
        print(
            f'{message.from_user.username} {message.from_user.first_name} {message.from_user.last_name} отпровляет идею...')
        bot.send_message(id,f'{message.from_user.username} {message.from_user.first_name} {message.from_user.last_name} отпровляет идею...')


    elif message.text == 'вопрос к руководству':
        bot.send_message(message.chat.id, 'напишите ваш вопрос к руководству')
        print(f'{message.from_user.username} {message.from_user.first_name} {message.from_user.last_name} отпровляет вопрос к руководству...')
        bot.send_message(id,
                         f'{message.from_user.username} {message.from_user.first_name} {message.from_user.last_name} отпровляет вопрос к руководству...')

    else:
        bot.send_message(id,f'{message.from_user.username} {message.from_user.first_name} {message.from_user.last_name}:{message.text}')
        print(f'{message.from_user.username} {message.from_user.first_name} {message.from_user.last_name}:{message.text}')


bot.infinity_polling()
