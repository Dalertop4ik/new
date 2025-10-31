import telebot

API_TOKEN = '8000101066:AAHgDYk02TT0YE1wgvajXlFKht3dVaRKFCs'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который может банить пользователей. Используйте /ban, чтобы забанить пользователя.")

@bot.message_handler(commands=['ban'])
def ban_user(message):
    if message.reply_to_message:  
        chat_id = message.chat.id 
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status 
        
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно забанить администратора.")
        else:
            bot.ban_chat_member(chat_id, user_id)
            bot.reply_to(message, f"Пользователь {user_id} был забанен.")
    else:
        bot.reply_to(message, "Пожалуйста, ответьте на сообщение пользователя, которого хотите забанить.")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    if message.text and "https://" in message.text:
        chat_id = message.chat.id
        user_id = message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        
        if user_status != 'administrator' and user_status != 'creator':
            bot.ban_chat_member(chat_id, user_id)
            bot.reply_to(message, f"Пользователь {message.from_user.username} был забанен за отправку ссылки.")
        else:
            bot.reply_to(message, "Администраторов нельзя банить.")

if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)

