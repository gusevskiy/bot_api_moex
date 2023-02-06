import requests
from pprint import pprint


def search_tiker_name(name: str) -> list:
    """this function searches for the stock ticker and name"""
    list_name = []
    url = ("https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/"
           "securities.json?"
           "iss.meta=off&"
           "iss.only=securities&"
           "securities.columns=SECID,SECNAME")
    all_tickers = requests.get(url).json().get('securities')['data']
    for list_of_number in all_tickers:
        if name in list_of_number[1]:
            list_name.append(list_of_number)
    return list_name


# print("search_tiker_name", search_tiker_name("Сбер"))


def search_ticker_name_close_prise(name: str) -> tuple:
    url = "https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR" \
          "/securities.json?iss.meta=off&iss.only=securities&securities" \
          ".columns=SECID,PREVADMITTEDQUOTE,SECNAME"
    all_tickers = requests.get(url).json().get('securities')['data']
    for list_of_number in all_tickers:
        if name in list_of_number[2]:
            return list_of_number


# print("search_ticker_name_close_prise", search_ticker_name_close_prise("Сбер"))


if __name__ == '__main__':
    print(search_tiker_name('Сбер'))
