user_with = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
""" задаём список """
for elem in user_with:
    plus_str = ""
    """ пустая переменная, для добавления знака + перед градусами """
    # добавил сюда - вдруг захочу в будущем ещё цифры со знаком + в список добавить
    # переменная будет всегда обнулена и + появится только в нужном момент
    if "+" in elem:
        # если найден +, то
        elem = elem.replace("+", "")
        # удаляем знак + в значении переменной
        plus_str = "+"
        # и присваиваем его (+) переменной plus_str - добавится при выводе
    if elem.isnumeric():    # определяем есть ли в значении переменной числа
        print('"', plus_str, str(elem).rjust(2, "0"), '"', sep='', end=' ')
        # str(elem).rjust(2, "0") - добавляются нули, если нужны, до двух целочисленных разрядов
    else:
        print(elem, end=' ')
