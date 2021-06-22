import random


class Warehouse:    # класс "склад"
    def __init__(self, product_code, list_class):
        self.product_code = product_code
        self.list_class = list_class

    @staticmethod
    def append_list():    # метод стат (добавит устройство, если выбрать 1)
        print("Дополнить список товаров - 1", "\n",
              "Поиск товара - 2", "\n",
              "Остановить выполнение кода - 3", sep='')
        user_inf = input("Выберете действие ")
        if user_inf == '2':
            Warehouse.distribution_to_divisions(start_list)
        elif user_inf == '1':
            user_inf = input("Выберите номер товара для добавления: сканер(1), принтер(2), ксерокс(3): ")
            user_inf = int(user_inf) - 1    # ну, да - костыль. для работы списка надо отнять единицу, ибо счёт с нуля
            print("вы выбрали", list_user_title[user_inf])    # маркер. не забудь удалить
            user_inf_data = input("Введите марку устройства ", )
            list_user_stamp[user_inf].insert(0, user_inf_data)    # марку добавим на нулевую позицию в списке
            user_inf_data = input("Введите модель устройства ", )
            list_user_model[user_inf].insert(0, user_inf_data)    # модель добавим на нулевую позицию в списке
            user_inf_data = input("Введите количество устройств ", )  # валидация - проверим число или нет
            while not user_inf_data.isdigit():    # так проще, чем регулярные выражения пинать
                user_inf_data = input("Введите количество устройств в виде положительного целого числа ", )
            else:
                user_inf_data = int(user_inf_data)    # преобразуем в числовое значение
                # посчитаем и поместим число на место числа, к которому прибавляли
                list_user_quantity.insert(user_inf, list_user_quantity[user_inf] + user_inf_data)
                # так как будет сдвиг списка чисел вправо, то удаляем одно число справа
                list_user_quantity.pop(user_inf + 1)
            user_inf_data = input("Введите наименование организации или адрес размещения оборудования ", )
            names_of_divisions.append(user_inf_data)
            print("Особенный параметр данного устройства это ", param_special[user_inf], param_all[user_inf])
            user_inf_data = input("Введите параметр, если он отсутствует в вписке ")
            if user_inf_data == '':
                print("Ну нет, так нет")
            else:
                print("Параметр принят и записан")
                param_all[user_inf].insert(0, user_inf_data)    # как обычно на нулевую позицию запишем сие безобразие
            print("Полная запись введённых параметров", '\n',
                  "Наименование: ", list_user_title[user_inf].title(), " ",
                  "Марка: ", list_user_stamp[user_inf][0].title(), " ",
                  "Модель: ", list_user_model[user_inf][0].upper(), " ",
                  "количество: ", list_user_quantity[user_inf], " ", '\n',
                  "Особенный параметр: ", param_special[user_inf].title(), ": ", param_all[user_inf], " ",
                  "наименование организации или адрес размещения оборудования", names_of_divisions[0])
            Warehouse.append_list()    # древнее зло пробуждаеццо!
        elif user_inf == '3':
            print("Наше дело предложить, ваше - отказаться")

    def distribution_to_divisions(self):    # метод экз (выводим инфу по продукту и рандомный адрес)
        print("На складе имеются:")
        for i in self.list_class:
            ind_search = self.list_class.index(i)
            print("наименование товара: ", i, ". ", "код: ", self.product_code[ind_search], sep='')
        user_inf = input("Введите код или наименование товара для поиска ").lower()
        if self.product_code.count(user_inf) > 0 or self.list_class.count(user_inf) > 0:
            sub_us = input("Желаете увидеть информацию по это продукту? (да/нет) ").lower()
            if sub_us == 'да' or sub_us == 'yes' or sub_us == 'y':    # страдание и боль - нафиг бы эти костыли
                if user_inf == '0001' or user_inf == "сканер":    # если совпадёт одно из значений
                    print(Scanner.show_scanner(data_user_scan),    # тут запуститься класс сканера
                          "Адрес/место нахождения: ", random.choice(names_of_divisions))    # рандомный адрес
                    user_inf_transfer = input("Хотите уточнить информацию по какому-либо отдельному устройству?"
                                              "(да, нет) ").lower()
                    if user_inf_transfer == "yes" or user_inf_transfer == "да" or user_inf_transfer == "y":
                        start_list.product_separately(user_inf)
                elif user_inf == '0002' or user_inf == "принтер":    # если совпадёт одно из значений
                    print(Printer.show_print(data_user_print),    # тут запустится класс принтера
                          "Адрес/место нахождения: ", random.choice(names_of_divisions))    # адрес рандомный
                    user_inf_transfer = input("Хотите уточнить информацию по какому-либо отдельному устройству?"
                                              "(да, нет) ").lower()
                    if user_inf_transfer == "yes" or user_inf_transfer == "да" or user_inf_transfer == "y":
                        start_list.product_separately(user_inf)
                elif user_inf == '0003' or user_inf == "ксерокс":    # если совпадёт одно из значений
                    print(Xerox.show_xerox(data_user_xer),    # тут запустится класс ксерокса
                          "Адрес/место нахождения: ", random.choice(names_of_divisions))    # адрес рандомный
                    user_inf_transfer = input("Хотите уточнить информацию по какому-либо отдельному устройству?"
                                              "(да, нет) ").lower()
                    if user_inf_transfer == "yes" or user_inf_transfer == "да" or user_inf_transfer == "y":
                        start_list.product_separately(user_inf)
            elif sub_us == 'нет' or sub_us == 'no' or sub_us == 'n':
                print("ну и ладно, не больно то и хотелось")
            else:
                print("вы ввели какую-то дичь")
        else:
            print("товара с таким кодом/названием ", "'", user_inf, "'", " нет на складе", sep='')

    @staticmethod
    def product_separately(user_inf):
        name_product = list_user_title[distribution_product.index(user_inf)]
        print("Устройство: ", name_product)    # временная метка. убери
        print("Марки устройств: ", *list_user_stamp[distribution_product.index(user_inf)])
        stamp_product = input("Выберете марку устройства ").lower()
        # получим индекс марки в списке
        stamp_product_index = list_user_stamp[distribution_product.index(user_inf)].index(stamp_product)
        print("Спиоск моделей: ", *list_user_model[distribution_product.index(user_inf)])
        stamp_model = input("Выберете модель устройства ").lower()
        # получим индекс модели в списке
        stamp_model_index = list_user_model[distribution_product.index(user_inf)].index(stamp_model)
        print("Устройство: ", name_product.title(), ". ",
              "Марка устройств: ",
              list_user_stamp[distribution_product.index(user_inf)][stamp_product_index].title(), ". ",
              "Модель устройства: ",
              list_user_model[distribution_product.index(user_inf)][stamp_model_index].upper(), ". ",
              "Особый параметр: ",
              param_special[distribution_product.index(user_inf)], ' - ',
              param_all[distribution_product.index(user_inf)][stamp_product_index], ". ", "\n",
              "Адрес/организация: ",
              random.choice(names_of_divisions), ". ",
              "Количество устройств на месте: ",
              random.randint(1, list_user_quantity[distribution_product.index(user_inf)]), sep='')


class OfficeEquipment:    # класс "Оргтехника"
    def __init__(self, title, stamp, model, quantity, param):    # название, марка, модель, количество
        self.quantity = quantity    # количество
        self.title = title    # название
        self.stamp = stamp    # марка (гугл переводил, не факт, что это не почтовая марка)
        self.model = model    # модель
        self.param = param    # вот этот параметр по индексу индивидуален каждому устройству (дочернему классу)


class Printer(OfficeEquipment):    # дочерний класс "принтер"
    def show_print(self):
        ind_i = self.title.index('принтер')    # нам нужен нидекс слова в списке (списки составлены в строгом порядке)
        return f'{"Наименование"}: {"принтер"}. {"Марка/и"}: {", ".join(self.stamp[ind_i]).title()}; ' \
               f'{"модель"}: {", ".join(self.model[ind_i]).upper()}. \n' \
               f'{"Общее количество данных устройств"}: {self.quantity[ind_i]}. ' \
               f'{"Тип принтера"}: {", ".join(self.param[ind_i])}.'


class Scanner(OfficeEquipment):    # дочерний класс "сканер"
    def show_scanner(self):
        ind_i = self.title.index('сканер')    # нам нужен нидекс слова в списке (списки составлены в строгом порядке)
        return f'{"Наименование"}: {"сканер"}. {"Марка/и"}: {", ".join(self.stamp[ind_i]).title()}; ' \
               f'{"модель"}: {", ".join(self.model[ind_i]).upper()}. \n' \
               f'{"Общее количество данных устройств"}: {self.quantity[ind_i]}. \n' \
               f'{"Разрешение сканирования (точек на дюйм)"}: {", ".join(self.param[ind_i])}.'


class Xerox(OfficeEquipment):    # дочерний класс "ксерокс"
    def show_xerox(self):
        ind_i = self.title.index('ксерокс')    # нам нужен нидекс слова в списке (списки составлены в строгом порядке)
        return f'{"Наименование"}: {"ксерокс"}. {"Марка/и"}: {", ".join(self.stamp[ind_i]).title()}; ' \
               f'{"модель"}: {", ".join(self.model[ind_i]).upper()}. \n' \
               f'{"Общее количество данных устройств"}: {self.quantity[ind_i]}. ' \
               f'{"Количество копий в пинуту"}: {", ".join(self.param[ind_i])}.'


# первый параметр для сканера
# второй для принтера
# третий для ксерокса
param_all = [['1200*800', '800*600'],
             ["струйный", "лазерный"],
             ['60', '170']]

# индивидуальные параметры каждому
param_special = ['разрешение при сканировании', 'тип печати', 'количество страниц в минуту']

list_user_title = ["сканер", "принтер", "ксерокс"]    # список наименований устройств
list_user_stamp = [["acer", "samsung"], ["canon", "samsung"], ["xerox"]]    # марки устройств
list_user_model = [["sc-100", "1200"], ["4410", "47-9"], ["xv-8", "fr-853"]]    # модели устройств
list_user_quantity = [2, 5, 2]    # количество устройств
distribution_product = ['0001', '0002', '0003']    # коды продукта
names_of_divisions = ['ООО "Рога и копыта"', 'ОАО Тепловодоканал',
                      'ЗАО МММ']    # наименования подразделений

# присваиваем значение по дочерним классам
# (можно было только в один класс и одну переменную всем, будет работать точно - проверял. но это нехорошо)
data_user_scan = Scanner(list_user_title, list_user_stamp, list_user_model, list_user_quantity, param_all)
data_user_print = Printer(list_user_title, list_user_stamp, list_user_model, list_user_quantity, param_all)
data_user_xer = Xerox(list_user_title, list_user_stamp, list_user_model, list_user_quantity, param_all)
# присваиваем значения для класса "склад"
start_list = Warehouse(distribution_product, list_user_title)
# вызываем Ктулху!
start_list.append_list()
