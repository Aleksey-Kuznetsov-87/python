# структуру (точнее только расположение классов и вывод ЗП) безбожно слизал с видео, но понял как работает :)
class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):
    def get_full_name(self):    # получим полное имя
        return f'{self.name} {self.surname}'

    def get_total_income(self):    # а тут посчитаем зп и плюшки
        return self._income["wage"] + self._income["bonus"]


position_example = Position("Джон", "Байден", "президент США",    # пишем Имя, Фамилию, занимаемую должность
                            {"wage": 100, "bonus": 48})    # вот тут можно зп и плюшки прописывать
print("Зарплата некоего поца с именем ", position_example.get_full_name(), " - ",
      position_example.get_total_income(), " вечнозелёных", sep='')    # ну, напишем кого-нибудь :)
