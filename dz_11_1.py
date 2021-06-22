import re    # да прибудет с нами валидация (в дальнейшем)


class Date:
    @classmethod
    def convert_to_a_number(cls, string_date):
        day, month, year = map(int, string_date.split('-'))    # преобразование в число, разделение по тире
        my_date = (day, month, year)    # запихаем всё в одну переменную
        return my_date

    @staticmethod
    def date_validation(date_valid):
        date_valid = [date_valid]    # костыль. переводим значение переменной в список
        re_date = re.compile(r'^(\d{2}.){2}\d{4}$')    # валидация на количество символов :)
        for date in date_valid:
            assert re_date.match(date), f'wrong date {date}'
        else:
            return "валидация прошла успешно"


my_date = '10-05-1980'    # вот тут и пишем дату в формате 'ДД-ММ-ГГГГ'
print("конвертирование в число проведено, результат ", Date.convert_to_a_number(my_date), sep='')
print(Date.date_validation(my_date), ", дата: ", my_date, sep='')
# не совсем понял задание, сделал как понял
