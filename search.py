import requests
from pprint import pprint


def search_tiker(name: str) -> tuple:
    """this function searches for the stock ticker"""
    url = ("https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/"
           "securities.json?"
           "iss.meta=off&"
           "iss.only=securities&"
           "securities.columns=SECID,SECNAME")
    all_tickers = requests.get(url).json().get('securities')['data']
    for list_of_number in all_tickers:
        if name in list_of_number[1]:
            return list_of_number


print(search_tiker("Сбер"))