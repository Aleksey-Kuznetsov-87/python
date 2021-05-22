import requests
import os
user_currency = input("Введите международное название валюты ").upper()
"""название валюты"""


def currency_rates(url):

    response = requests.get(url)
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    return content


page = currency_rates("http://www.cbr.ru/scripts/XML_daily.asp")
page = str(page)

try:
    currency_index = page.index(user_currency)
    currency_index_start = page.find("<Value>", currency_index) + len("<Value>")
    currency_index_stop = page.find("</", currency_index_start)
    currency_index_date = page.find("Date")
    data_currency = page[currency_index_date + 6: currency_index_date + 16]
    print("Стоимость", user_currency, "на", data_currency, "составляет",
          page[currency_index_start: currency_index_stop], "руб.")
except ValueError:
    print("Валюта -", user_currency, "- отсутсвует в списке")

os.system('pause')
