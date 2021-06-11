class Clothes:
    def __init__(self, size_v, height_h):
        self.size_v = size_v
        self.height_h = height_h

    def coat(self):
        coat_v = (self.size_v / 6.5 + 0.6)
        return coat_v

    def suit(self):
        suit_h = (self.height_h / 100 * 2 + 0.3)
        return suit_h

    @property
    def sum_size(self):
        arc = (self.size_v / 6.5 + 0.6) + (self.height_h / 100 * 2 + 0.3)
        # с помощью super() не вышло вызвать значения, потому и написал их вновь. недочёт
        yield arc


size_height = Clothes(52, 180)  # первое - размер, второе значение - рост
print("Расход ткани на пальто - ", size_height.coat(), " кв.м.", "\n",
      "Расход ткани на костюм - ", size_height.suit(), " кв.м.", sep='')
print("Расчёт суммарного расхода ткани на производство одежды - ",
      *size_height.sum_size, " квадратных метров", sep='')
