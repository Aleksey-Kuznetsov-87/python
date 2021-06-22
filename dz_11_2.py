class Numb:
    def __init__(self, num_user):    # пусть так - ибо нам нужен доступ к методу с переменной
        self.num_user = num_user

    def division_by_zero(self):    # всё, что ниже - из методички, только переменную вызвал уровнем выше
        try:
            res = 100 / self.num_user
        except ZeroDivisionError:
            print("На ноль делить нельзя")
        else:
            print(f"Все хорошо. Результат: {res}")
        finally:
            print("Программа завершена")


numbers_user = int(input("Введите целое число "))
my_number = Numb(numbers_user)    # цифра передброшена в Numb
my_number.division_by_zero()    # вызаваем метод
