input_number = input("Введите прописью число на английском от 0 до 10 ")    # вводим данные


def number_translate(num):
    """ возвращает значение на русском языке заданного слова """

    words_list = {
        "zero": "ноль",
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять",
    }
    result = ""    # новая переменная, пустая
    if num.istitle():    # проверяем на заглавную при вводе
        num = num.lower()    # переводим введённые символы в нижний регистр
        result = words_list.get(num.title())    # если на вводе заглавная, то на выводе будет слово с заглавной буквы
    else:
        result = words_list.get(num)    # get - вернёт None, если нет значения в словаре
    return result


print(number_translate(input_number))
