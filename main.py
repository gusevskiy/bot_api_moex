# coding: utf-8
import requests
import os
from datetime import date

from dotenv import load_dotenv
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Updater,
    MessageHandler,
    Filters,
    CommandHandler,
    CallbackQueryHandler
)


def ticker_search(update, context) -> list:
    """
    This function search ticker, name, price in list everyone tickers
    name: here in Cyrillic in application telegram
    """
    word = update.message.text
    list_tikers = []
    url = "https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR" \
          "/securities.json?iss.meta=off&iss.only=securities&securities" \
          ".columns=SECID,SECNAME"
    all_names = requests.get(url).json().get('securities')['data']
    for names in all_names:
        if word.upper() in names[1].upper():
            list_tikers.append(names)
    create_buttom(update, list_tikers)


def create_buttom(update, data):
    """This function created buttom"""
    word = update.message.text
    keyboard = []
    for x in data:
        keyboard.append(
            [
                InlineKeyboardButton(
                    text=x[1], callback_data=x[0]
                )
            ]
        )
    reply_markup = InlineKeyboardMarkup(keyboard)
    return update.message.reply_text(
        f"По слову <b>{word}</b> есть такие эмитенты:", parse_mode='html',
        reply_markup=reply_markup
    )


def search_ticker_price(tickers):
    """
    Получает цены по всем бумагам в заданной секции на дату.
    По тикеру ищет его цену закрытия дневной сессии.
    Документация на ссылку https://iss.moex.com/iss/reference/825
    """
    tikers_name_price = {}
    start = 0
    stop_while = 0
    while stop_while <= 100:

        url = (
            f'https://iss.moex.com/iss/history/'
            f'engines/stock/'
            f'markets/shares/'
            f'session/TQBR/'
            f'boardgroups/57/'
            f'securities.json?'
            f'iss.meta=off'
            f'&data={date.today()}'
            f'&security_type_id=3,1'
            f'&tradingsession=1'
            f'&start={start}'
            f'&iss.only=history'
            f'&history.columns=SECID,SHORTNAME,LEGALCLOSEPRICE,TRADEDATE'
        )
        list_data = requests.get(url).json().get('history')['data']
        stop_while = len(list_data)
        keys = ['SECID', 'SHORTNAME', 'LEGALCLOSEPRICE', 'TRADEDATE']
        for name in list_data:
            if name[0] == tickers:
                tickers = dict(zip(keys, name))
                tikers_name_price.update(tickers)
                return tikers_name_price
        if stop_while < 100:
            break
        start += 100


def help(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    context.bot.send_message(
        chat_id=chat.id,
        text=(
            f'Привет {name}! \n' 
            f'бот ищет по названию все совпадения в названиях компаний которые'
            f' торгуются на ММВБ в режиме TQBR (T+2) и предоставляет цены '
            f'за предыдущую торговую сессию. \n'
            f'Введи любое название которое знаешь, например: "Сбер".'
        )
    )


def push_buttom(update, context):
    chat = update.effective_chat
    ticker = update.callback_query.data
    data = search_ticker_price(ticker)
    message = f"На дату {data.get('TRADEDATE')} цена акции " \
              f"'{data.get('SHORTNAME')}' =" \
              f" {data.get('LEGALCLOSEPRICE')}р."
    context.bot.send_message(chat_id=chat.id, text=message)


def main():
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN')
    updater = Updater(token=token)
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, ticker_search))
    updater.dispatcher.add_handler(CallbackQueryHandler(push_buttom))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
