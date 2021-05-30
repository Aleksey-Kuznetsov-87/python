import requests
import os


# эту часть кода слизал с 4 или 5 ДЗ :)
def currency_rates(url):

    response = requests.get(url)
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    return content


# задаём данные переменной по ссылке
page = currency_rates("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs")

# # создаём файли и пишем в него данные (можно было под функцию записать)
with open('append_text.txt', 'w', encoding='utf-8') as f:
    f.write(page)

ad_ip = []    # будет отдельный список с ip (по нему и искать будем спамера и максимальное вхождение)

# открываем созданный файл и ищем в нём ip, метод пеердачи и url (точнее ресурс) (можно было под функцию записать)
with open('append_text.txt', 'r', encoding='utf-8') as f:
    for i in f:
        line_new = i.split()
        ip, met, url, = (line_new[0], line_new[5], line_new[6])    # а вот индексы у преподавателя подсмотрел
        ad_ip.append(ip)
        met = met.strip('\'\"')    # убираем лишние знаки
        print(ip, met, url)
    max_ip = max(set(ad_ip), key=ad_ip.count)    # ищем значение с максимальным вхождением
    quantity_ip = ad_ip.count(max_ip)    # считаем количество повторяющихся значений в списке
    print("Главный спамер - ", "'", max_ip, "'.", " Количество запросов - ",  quantity_ip, sep='')

# намудрил, аж стыдно... иногда
