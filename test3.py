import requests
from pprint import pprint

def rrrrr():
    result = []
    start = 0
    while True:
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
        r = requests.get(url).json().get('history')['data']
        for i in r:
            if i[0] == 'SER':
                return i
        start += 100
    # return result

if __name__ == '__main__':
    print(rrrrr())


    # pprint(r)