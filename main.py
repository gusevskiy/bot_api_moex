import requests


def search_ticker(name: str) -> tuple:
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


tiker = search_ticker("Сбер")[0]



url = f"https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/" \
      f"securities.json?iss.meta=off&iss.only=marketdata&marketdata." \
      f"columns=SECID,LAST&tradingsession=1&securities={tiker}"


r = requests.get(url).json().get('marketdata')['data'][0][1]

print(r)
