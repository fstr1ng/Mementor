import json
import logging

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

class Action:
    defaults = {
        "create": ["text", "name"],
        "read": ["rowid"],
        "update": ["text", "name", "rowid"],
        "delete": ["rowid"],
    }

    def __init__(self, command):
        self.command = command
        self.required_fields = Action.defaults[self.command]
        self.request = str()
        self.data = dict()

class User:
    def __init__(self):
        ...

with open('config.json') as f:
    config = json.load(f)

logger = telebot.logger
telebot.logger.setLevel(config['log']['level'])

bot = telebot.TeleBot(config['bot']['token'])

users = {}

def create_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    for b in Action.defaults.keys():
        markup.add(InlineKeyboardButton(b, callback_data = b))
    return markup

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.reply_to(message, 'Select an action:', reply_markup=create_markup())

@bot.callback_query_handler(func=lambda call: True)
def create_action(call):
    cid = call.message.chat.id
    user = users.get(cid, User())
    #bot.answer_callback_query(call.id, f'Action {call.data} is selected')
    user.action = Action(call.data)
    users[cid]=user
    reply = field_required(user, cid)
    bot.register_next_step_handler(reply, collect_data)

def field_required(user, cid):
    text =  f'Selected action: {user.action.command.upper()}\n' 
    text += f'Please enter {user.action.required_fields[-1].upper()}'
    return bot.send_message(cid, text)

def collect_data(message):
    cid = message.chat.id
    user = users[cid]
    data = message.text
    requesting = user.action.required_fields.pop()
    user.action.data[requesting] = data
    if any(user.action.required_fields):
        reply = field_required(user, cid)
        bot.register_next_step_handler(reply, collect_data)
    else:
        user.action = None
        reply = bot.reply_to(message, 'Data collected')

def execute_action()

bot.polling()
