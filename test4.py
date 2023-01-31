import requests
from pprint import pprint


# Получить историю по одной бумаге на рынке за интервал дат.
# Документация  https://iss.moex.com/iss/reference/817
url = (
    f'https://iss.moex.com/iss/history/'
    f'engines/stock/'
    f'markets/shares/'
    f'session/TQBR/'
    # f'boardgroups/57/'
    f'securities/SBER/.json?'
    f'iss.meta=off'
    f'&from=2023-01-31'
    f'&=2023-01-31'
    f'&security_type_id=3, 1'
    f'&tradingsession=1'
    f'&limit={start}'
    f'&iss.only=history'
    f'&history.columns=SECID,LEGALCLOSEPRICE'

)



r = requests.get(url).json().get('history')['data']

for i in r:
    if i[0] == 'SBER':
        print(i[1])
        start += 100

# pprint(r[0][0])