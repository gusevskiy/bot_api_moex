# coding: utf-8
import requests
import os

from dotenv import load_dotenv
import telegram
from telegram.ext import Updater, MessageHandler, Filters


load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

updater = Updater(token=TELEGRAM_TOKEN)


def check_tokens() -> bool:
    """Check variables(TOKENS) в .env"""
    # logging.info("Checking tokens")
    return all([TELEGRAM_TOKEN, TELEGRAM_CHAT_ID])


def search_ticker_name_close_prise(name: str) -> list:
    """
    This function search ticker, name, price
    name: here in Cyrillic
    """
    data = []
    url = "https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR" \
          "/securities.json?iss.meta=off&iss.only=securities&securities" \
          ".columns=SECID,PREVADMITTEDQUOTE,SECNAME"
    all_tickers = requests.get(url).json().get('securities')['data']
    for ticker in all_tickers:
        if name.lower() in ticker[2].lower():
            data.append(ticker)
    return data


# def send_message(bot: telegram.bot.Bot, message: str) -> None:
#     """Send message in telegram."""
#     bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)


def main(update, context):
    chat = update.effective_chat
    text_ticker = update.message.text
    data = list(search_ticker_name_close_prise(text_ticker))
    for message in data:
        context.bot.send_message(
            chat_id=chat.id,
            text=f'{message[2]}, Цена 1й акции = {message[1]} руб.')


updater.dispatcher.add_handler(MessageHandler(Filters.text, main))

updater.start_polling()
updater.idle()

# if __name__ == '__main__':
#     main('Сбер')
    # print(search_ticker_name_close_prise('Сбер')[0][2])
