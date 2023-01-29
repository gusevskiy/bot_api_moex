import requests

# Документация  https://iss.moex.com/iss/reference/64
url = 'https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities.xml?iss.meta=off&iss.only=history&history.columns=TRADEDATE,SECID,SHORTNAME,CLOSE&start=0&sort_column=SHORTNAME'



r = requests.get(url)


print(r.text)