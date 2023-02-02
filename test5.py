
tikers = [{'SECID': 'SBER', 'PREVADMITTEDQUOTE': None, 'SECNAME': 'Сбербанк России ПАО ао', 'PREVDATE': '2023-02-01'}, {'SECID': 'SBERP', 'PREVADMITTEDQUOTE': None, 'SECNAME': 'Сбербанк России ПАО ап', 'PREVDATE': '2023-02-01'}]


# tikers_keys = ['SECID', 'LEGALCLOSEPRICE']
# for i in tikers:
#     if i[0] == 'SBER':
#         tikers_dict = zip(dict(tikers_keys, i))
#         tikers_name_price.append(tikers_dict)

# if __name__ == '__main__':
#     print(search_ticker_price(tikers))


print(tikers[0].get('SBER'))