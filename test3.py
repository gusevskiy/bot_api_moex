import requests


tikers = [{'SECID': 'SBER', 'PREVADMITTEDQUOTE': None, 'SECNAME': 'Сбербанк России ПАО ао', 'PREVDATE': '2023-02-01'}, {'SECID': 'SBERP', 'PREVADMITTEDQUOTE': None, 'SECNAME': 'Сбербанк России ПАО ап', 'PREVDATE': '2023-02-01'}]

def search_ticker_price(tickers):
    tikers_name_price = []
    for ticker in tickers:
        ticker = ticker.get('SECID')
        start = 383
        stop_while = 0
        while stop_while <= 100:
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
            list_data = requests.get(url).json().get('history')['data']
            stop_while = len(list_data)
            keys = ['SECID', 'LEGALCLOSEPRICE']
            for name in list_data:
                if name[0] == ticker:
                    tickers = dict(zip(keys, name))
                    tikers_name_price.append(tickers)
            if stop_while < 100:
                break
            start += 100
    return tikers_name_price

if __name__ == '__main__':
    print(search_ticker_price(tikers))


    # pprint(r)