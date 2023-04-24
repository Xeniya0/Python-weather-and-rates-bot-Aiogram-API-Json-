from requests import utils, get


def currency_rates(code):
    response = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))
    content = response.split('<Valute ID=')
    for i in content:
        if code.upper() in i:
            return f"{code.upper()} = {float(i.replace('/', '').split('<Value>')[-2].replace(',', '.'))}"

