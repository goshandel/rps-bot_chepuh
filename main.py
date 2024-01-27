import telebot
from info import about_version_text, start_help_text, info_about_bot_text, file_path, file_quest_1_1, file_quest_1_2, file_quest_2_1, file_quest_2_2, file_quest_3_1_1, file_quest_3_1_2, file_quest_3_2_1, file_quest_3_2_2
from button import markup_my, markup_event, markup_quest_1, markup_quest_2, markup_quest_22
token = "/"
bot = telebot.TeleBot(token=token)
chat_id = 1171114800
bot.send_message(chat_id, "1111", reply_markup=markup_my)
# Внимание, это не оскорбление. Так я вижу, что код запустился.
# bot.send_dice(chat_id)
# 1171114800
# 5626106111

# _____________________________________________________________________________________________________________________
@bot.message_handler(commands=['quest'])
def qest(message):
    bot.send_message(message.chat.id, "предлогаю начинать согласен?", reply_markup=markup_event)
    bot.register_next_step_handler(message, quest_1)
def quest_1(message):
    if message.text.lower() == "да" or message.text.lower() == "да!":
        bot.send_message(message.chat.id, "вот представь ты проголодался но в холодильнике пусто!\nКуда ты хочешь пойти за продуктами?", reply_markup=markup_quest_1)
        send_file(file_quest_1_1 ,message.chat.id)
        send_file(file_quest_1_2, message.chat.id)
        bot.register_next_step_handler(message, quest_2)
    elif message.text.lower() == "нет":
        bot.send_message(message.chat.id, "И ЗАЧЕМ ТЫ ЭТО ЗАПУСТИЛ?!?!?!??!")
    else:
        bot.send_message(message.chat.id, "???", reply_markup=markup_event)
        bot.register_next_step_handler(message, quest_1)
def quest_2(message):
    bot.send_message(message.chat.id, "тебя не смущает что ты в 2012? и лотос сгорел:(")
    if message.text == "2":
        bot.send_message(message.chat.id, "по списку пойдёшь?", reply_markup=markup_quest_2)
        send_file(file_quest_2_1, message.chat.id)
        bot.register_next_step_handler(message, quest_3_1)
    elif message.text =="1":
        bot.send_message(message.chat.id, "сыкономить?", reply_markup=markup_quest_22)
        send_file(file_quest_2_2, message.chat.id)
    else:
        bot.send_message(message.chat.id, "???", reply_markup=markup_quest_1)
        bot.register_next_step_handler(message, quest_2)
def quest_3_1(message):
    if message.text == "нет, я слишком крут":
        bot.send_message(message.chat.id, "ты купил: \nУран 238\nКамни\nКонсервированные ананасы!\n\nИ ты приготовил из этого радиоктивные блины!")
        bot.send_photo(chat_id=message.chat.id, photo=file_quest_3_1_1)
    elif message.text == "да":
        bot.send_message(message.chat.id, "ну ничего интересного ты просто блины приготовил")
        bot.send_photo(chat_id=message.chat.id, photo=file_quest_3_1_2)
    else:
        bot.send_message(message.chat.id, "???", reply_markup=markup_quest_2)
        bot.register_next_step_handler(message, quest_3_1)
def quest_3_2(message):
    if message.text == "нет":
        bot.send_message(message.chat.id, "ты купил золотой слиток и проиграл \nпочему?\n\nпотому")
        bot.send_photo(chat_id=message.chat.id, photo=file_quest_3_2_1)
    elif message.text == "да":
        bot.send_message(message.chat.id, "сыкономил значит заработал! теперь ты миллиардерн")
        bot.send_photo(chat_id=message.chat.id, photo=file_quest_3_2_2)
    else:
        bot.send_message(message.chat.id, "???", reply_markup=markup_quest_22)
        bot.register_next_step_handler(message, quest_3_2)
# _____________________________________________________________________________________________________________________
def send_file(file_path, chat_id):
    file = open(file_path, 'rb')
    bot.send_document(chat_id, document=file)
    file.close()
# _____________________________________________________________________________________________________________________
@bot.message_handler(commands=['my_chanel'])
def handle_channel(message):
    bot.send_message(message.chat.id, "https://t.me/wowowowowowoeoeoeo")
    pass
# _____________________________________________________________________________________________________________________
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, start_help_text, reply_markup=markup_my, parse_mode='html')
    pass
# _____________________________________________________________________________________________________________________
@bot.message_handler(commands=['info_about_bot'])
def handle_info_about_bot(message):
    bot.send_message(message.chat.id, info_about_bot_text, parse_mode = 'html')
    pass
# _____________________________________________________________________________________________________________________
@bot.message_handler(commands=['about_version'])
def handle_about_version(message):
    bot.send_message(message.chat.id, about_version_text, parse_mode = 'html')
# _____________________________________________________________________________________________________________________
def filter_password(message):
    password = "Лох"
    return password.lower() in message.text.lower()
@bot.message_handler(content_types=['text'], func = filter_password)
def say_hello(message):
    bot.send_message(message.chat.id, "сам такой!")
# ________________________________________________________________________________________________________________________________________________________
def filter_password(message):
    password = "сквазимабзабза"
    return password.lower() in message.text.lower()
@bot.message_handler(content_types=['text'], func = filter_password)
def say_hello(message):
    send_file(file_path, message.chat.id)
# _____________________________________________________________________________________________________________________
def filter_password(message):
    password = "ДПХР"
    return password in message.text
@bot.message_handler(content_types=['text'], func = filter_password)
def say_hello(message):
    bot.send_message(message.chat.id, "неожиданно! Привет участник ДПХР")
# _____________________________________________________________________________________________________________________
def filter_password(message):
    password = "спам"
    return password.lower() in message.text.lower()
@bot.message_handler(content_types=['text'], func = filter_password)
def say_hello(message):
    x = 0
    while x < 15:
        bot.send_message(message.chat.id, "нет!!!!!!!!!!!!!!!!!!!")
        x += 1
# _____________________________________________________________________________________________________________________
@bot.message_handler(content_types=['text'])
def repeat_message(message):
    bot.send_message(message.chat.id, message.text)
# _____________________________________________________________________________________________________________________
bot.infinity_polling()