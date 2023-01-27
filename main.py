import requests
import os

from dotenv import load_dotenv
import telegram
from telegram import Bot


load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


def check_tokens() -> bool:
    """Check variables(TOKENS) в .env"""
    # logging.info("Checking tokens")
    return all([TELEGRAM_TOKEN, TELEGRAM_CHAT_ID])


def search_ticker_name_close_prise(name: str) -> tuple:
    """
    This function search ticker, name, price
    name: here in Cyrillic
    """
    url = "https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR" \
          "/securities.json?iss.meta=off&iss.only=securities&securities" \
          ".columns=SECID,PREVADMITTEDQUOTE,SECNAME"
    all_tickers = requests.get(url).json().get('securities')['data']
    for ticker in all_tickers:
        if name in ticker[2]:
            return ticker


# print("search_ticker_name_close_prise", search_ticker_name_close_prise("Сбер"))


def send_message(bot: telegram.Bot, ticker: str) -> None:
    """Send message in telegram."""
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=ticker)

