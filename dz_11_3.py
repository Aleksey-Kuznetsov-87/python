class NumbersOnly:
    def __init__(self, meaning_user):    # пусть так - ибо нам нужен доступ к методу с переменной
        self.meaning_user = meaning_user

    def checking_the_number(self):    # всё, что ниже - из методички, только переменную вызвал уровнем выше
        while self.meaning_user != 'stop':    # пока не будет введено stop, цикл будет крутиться
            try:
                self.meaning_user = int(self.meaning_user)    # преобразуем значение в число
            except ValueError:    # если не число, то
                print("Некорректное значение")
            else:    # если число, то
                user_list.append(self.meaning_user)    # добавим число в список
                print(f"Все хорошо. Продолжаем")
            self.meaning_user = input("Введите целое число ")    # вновь просим ввести значение
        print("Список введённых ранее числовых значений: ", user_list)    # при завершении цикла будет показан список


user_list = []    # объявляем пустиой список (будем туда числа записывать)

numbers_user = input("Введите целое число ")
my_number = NumbersOnly(numbers_user)    # цифра передброшена в NumbersOnly
my_number.checking_the_number()    # вызаваем метод
