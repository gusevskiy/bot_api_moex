# coding: utf-8
import requests
import os
from datetime import date, timedelta

from dotenv import load_dotenv
import telegram 
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler


load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

updater = Updater(token=TELEGRAM_TOKEN)


def check_tokens() -> bool:
    """Check variables(TOKENS) в .env"""
    # logging.info("Checking tokens")
    return all([TELEGRAM_TOKEN, TELEGRAM_CHAT_ID])


def ticker_search(secname: str) -> list:
    """
    This function search ticker, name, price
    name: here in Cyrillic
    """
    list_tikers = []
    keys = ['SECID', 'PREVADMITTEDQUOTE', 'SECNAME', 'PREVDATE']
    # tickers = {}
    url = "https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR" \
          "/securities.json?iss.meta=off&iss.only=securities&securities" \
          ".columns=SECID,PREVADMITTEDQUOTE,SECNAME,PREVDATE"
    # print(requests.get(url).text)
    all_names = requests.get(url).json().get('securities')['data']
    for names in all_names:
        if secname.lower() in names[2].lower():
            tickers = dict(zip(keys, names))
            list_tikers.append(tickers)
    return list_tikers


def old_price(tikers, trading_date=date.today()-timedelta(days=360)):
    # print(trading_date)
    ticker_price = []
    for tiker in tikers:
        # print(tiker)
        url = (f"https://iss.moex.com/iss/history/engines/stock/markets/shares/"
               f"boards/TQBR/securities/{tiker.get('SECID')}/.json?"
               f"iss.meta=off&"
               f"iss.only=history&"
               f"history.columns=TRADEDATE,SHORTNAME,CLOSE&"
               f"from={trading_date}&till={trading_date}")
        all_tickers = requests.get(url).json().get('history')['data']
        ticker_price.append(all_tickers)
    return ticker_price


def profitability(ticker):
    ...


def main(update, context):
    chat = update.effective_chat
    text_ticker = update.message.text
    data = list(ticker_search(text_ticker))
    for message in data:
        context.bot.send_message(
            chat_id=chat.id,
            text=f'{message[2]}, Цена 1й акции = {message[1]} руб.')


def say_hi(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    context.bot.send_message(
        chat_id=chat.id,
        text=(f'Привет {name}! \n' 
        f'бот ищет по названию все совпадения в названиях компаний которые '
              f'торгуются на ММВБ в режиме TQBR (T+2) и предоставляет цены '
              f'за предыдущую торговую сессию'
              f'закрытия предыдущей торговой сессии, также доходность за '
              f'текущий год и доходность от момента покупки год назад.\n '
              f'Введи любое название которое знаешь, например: "Сбер".'))


if __name__ == '__main__':
    # CommandHandler должен находится выше
    # updater.dispatcher.add_handler(CommandHandler('help', say_hi))
    # updater.dispatcher.add_handler(MessageHandler(Filters.text, main))
    #
    # updater.start_polling()
    # updater.idle()
    # print(main)
    r = ticker_search('Сбер')
    print(r)
    print(old_price(r))
