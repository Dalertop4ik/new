#!/usr/bin/python

import telebot
import random

API_TOKEN = '8000101066:AAHgDYk02TT0YE1wgvajXlFKht3dVaRKFCs'

bot = telebot.TeleBot(API_TOKEN)

# Переменная для хранения состояния режима эха
echo_mode = True

# Список шуток
jokes = [
    "Почему программисты предпочитают темный цвет? Потому что светлый цвет слишком много бьет по глазам!",
    "Как программист заказывает пиццу? 'Пожалуйста, сделайте ее с 8 битами сыра!'",
    "Почему коты не могут стать программистами? Они слишком часто теряют контекст!",
]

# Класс Car
class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def info(self):
        return f"This is a {self.color} {self.brand}."

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!
You can toggle echo mode with the /echo command.
You can also ask for a joke using /joke command or get info about a car using /car command.
""")

# Handle '/echo' command to toggle echo mode
@bot.message_handler(commands=['echo'])
def toggle_echo(message):
    global echo_mode
    echo_mode = not echo_mode
    status = "enabled" if echo_mode else "disabled"
    bot.reply_to(message, f"Echo mode is now {status}.")

# Handle '/joke' command to tell a random joke
@bot.message_handler(commands=['joke'])
def tell_joke(message):
    joke = random.choice(jokes)
    bot.reply_to(message, joke)

# Handle '/car' command to create an instance of Car
@bot.message_handler(commands=['car'])
def car_info(message):
    args = message.text.split()[1:]  # Получаем аргументы после команды
    if len(args) != 2:
        bot.reply_to(message, "Please provide both color and brand. Usage: /car color brand")
        return
    
    color, brand = args
    my_car = Car(color, brand)
    bot.reply_to(message, my_car.info())

# Handle all other messages with content_type 'text'
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if echo_mode:
        bot.reply_to(message, message.text)
    else:
        bot.reply_to(message, "Echo mode is disabled. Send /echo to enable it.")

bot.infinity_polling()