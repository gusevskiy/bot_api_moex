import requests


url = "https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR" \
      "/securities.json?iss.meta=off&iss.only=securities&securities.columns" \
      "=SECID,PREVADMITTEDQUOTE,SECNAME"
all_tickers = requests.get(url)#.json().get('securities')['data']


print(all_tickers.json())