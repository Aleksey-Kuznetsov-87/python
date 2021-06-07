
class Stationery:
    def __init__(self, title):    # title - атрибут (название)
        self.title = title

    @staticmethod
    def draw():
        return "Начало великого, мой господин! Отрисовка!"


class Pen(Stationery):    # дочерний класс
    @staticmethod
    def draw():    # если в скобках пустота, втыкаем @staticmethod сверху. draw - метод
        return "Ручко"


class Pencil(Stationery):    # дочерний класс
    @staticmethod
    def draw():    # если в скобках пустота, втыкаем @staticmethod сверху. draw - метод
        return "Карандаш"


class Handle(Stationery):    # дочерний класс
    @staticmethod
    def draw():    # если в скобках пустота, втыкаем @staticmethod сверху. draw - метод
        return "Маркёр!"


painting = Stationery
pen = Pen("карандаш")    # вместо Pen строчим любые другие дочерние классы
print(painting.draw(), "Берём лапками ", pen.draw(), " и адово рисуем!", end='')
