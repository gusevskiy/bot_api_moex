# coding: utf-8
import requests
import os
from datetime import date, timedelta
from pprint import pprint

from dotenv import load_dotenv
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
)
from telegram.ext import (
    Updater,
    MessageHandler,
    Filters,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler
)


updater = Updater(token='5891863496:AAGYFOD5XMc5IZCJl92tjxlaBDG_DNNXC9w')


def ticker_search(update, context) -> list:
    """
    This function search ticker, name, price
    name: here in Cyrillic
    """
    chat = update.effective_chat
    name = update.message.chat.first_name
    word = update.message.text
    list_tikers = []
    url = "https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR" \
          "/securities.json?iss.meta=off&iss.only=securities&securities" \
          ".columns=SECID,SECNAME"
    all_names = requests.get(url).json().get('securities')['data']
    for names in all_names:
        if word.upper() in names[1].upper():
            list_tikers.append(names)
    print(f'{word} нашли по слову', list_tikers)
    create_buttom(update, list_tikers)
    return list_tikers


def create_buttom(update, data):
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
    tikers_name_price = []
    for ticker in tickers:
        ticker = ticker.get('SECID')
        print(ticker)
        
        start = 0
        stop_while = 0
        while stop_while <= 100:
            # Документация  https://iss.moex.com/iss/reference/825
            url = (
                f'https://iss.moex.com/iss/history/'
                f'engines/stock/'
                f'markets/shares/'
                f'session/TQBR/'
                f'boardgroups/57/'
                f'securities.json?'
                f'iss.meta=off'
                f'&data=2023-01-31'
                f'&security_type_id=3,1'
                f'&tradingsession=1'
                f'&start={start}'
                f'&iss.only=history'
                f'&history.columns=SECID,LEGALCLOSEPRICE'
            )
            list_data = requests.get(url).json().get('history')['data']
            stop_while = len(list_data)
            keys = ['SECID', 'LEGALCLOSEPRICE']
            for name in list_data:
                if name[1] == ticker:
                    tickers = dict(zip(keys, name))
                    tikers_name_price.append(tickers)
            if stop_while < 100:
                break
            start += 100
    return tikers_name_price


# async def show_ticker(update, context):
#     chat = update.effective_chat
#     text_ticker = update.message.text
#     data = list(ticker_search(text_ticker))
#     for message in data:
#         await context.bot.send_message(
#             chat_id=chat.id,
#             text=message)


# async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     chat = update.effective_chat
#     name = update.message.chat.first_name
#     await context.bot.send_message(
#         chat_id=chat.id,
#         text=(f'Привет {name}! \n' 
#         f'бот ищет по названию все совпадения в названиях компаний которые '
#               f'торгуются на ММВБ в режиме TQBR (T+2) и предоставляет цены '
#               f'за предыдущую торговую сессию'
#               f'закрытия предыдущей торговой сессии, также доходность за '
#               f'текущий год и доходность от момента покупки год назад.\n '
#               f'Введи любое название которое знаешь, например: "Сбер".'))

# тестовая ф-я потом удалить
def input(update, context):
    chat = update.effective_chat
    message = update.callback_query.data
    context.bot.send_message(chat_id=chat.id, text=message)

if __name__ == '__main__':
    load_dotenv()

    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    # application = ApplicationBuilder().token('5891863496:AAGGUZiQbs_r80c-3TfJ2t-UUM1stkN2_3I').build()
    # CommandHandler должен находится выше
    help_handler = CommandHandler('help', help)
    updater.dispatcher.add_handler(MessageHandler(Filters.text, ticker_search))
    updater.dispatcher.add_handler(CallbackQueryHandler(input))
    # application.add_handler(massage_handler)



    updater.start_polling()
    updater.idle()
    
    # print(main)
    # r = ticker_search('Яку')
    # print(r)
    # print(search_ticker_price(r))
