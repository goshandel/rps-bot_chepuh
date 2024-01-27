from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot import types
markup = types.InlineKeyboardMarkup(row_width=2)

item1 = types.InlineKeyboardButton("Твой результат🍾", callback_data='your_score')
markup.add(item1)
markup_game = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
rock = KeyboardButton("🗿")
sis = KeyboardButton("✂️")
paper = KeyboardButton("💵")
score  = KeyboardButton("счёт📄")
exit = KeyboardButton("выход❌")
markup_game.add(paper, sis, rock)
markup_game.add(exit, score)

markup_event = ReplyKeyboardMarkup(resize_keyboard=True)
markup_event.add(KeyboardButton('да'), ('ДА!'), ('нет'))

markup_my = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
rps = KeyboardButton("/game_rps")
cha = KeyboardButton("/my_chanel")
help = KeyboardButton("/help")
infobot = KeyboardButton("/info_about_bot")
ys = KeyboardButton("/your_score")
markup_my.add(help, cha, rps)
markup_my.add(infobot, ys)

markup_quest_1 = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
quest_1 = KeyboardButton("1")
quest_2 = KeyboardButton("2")
markup_quest_1.add(quest_1, quest_2)

markup_quest_2 = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
quest_12 = KeyboardButton("да")
quest_22 = KeyboardButton("нет, я слишком крут")
markup_quest_2.add(quest_12, quest_22)

markup_quest_22 = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
quest_122 = KeyboardButton("да")
quest_222 = KeyboardButton("нет")
markup_quest_22.add(quest_122, quest_222)


#x = "🤕"

