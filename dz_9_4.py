class Car:    # созадём класс
    def __init__(self, speed, color, name, is_police, to_to):    # атрибуты класса
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.to_to = to_to

    @staticmethod
    def go():    # метод
        print("Машинко поехало.")

    @staticmethod
    def stop():    # метод
        print("Оно остановилось?")

    def turn(self):    # метод
        print("Машинко повернулсо куда-то ", self.to_to, sep='')

    def show_speed(self):    # метод
        print("Скорость пепелаца ", self.speed, " чего-то в чём-то.")


class TownCar(Car):    # дочерний класс
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Ахтунг! Первая космическая скорость достигнута!")


class WorkCar(Car):    # дочерний класс
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Ахтунг! Вторая космическая скорость достигнута!"
                  " Отрыв колёс!!!")


car_word = WorkCar(70, "Белый", "пепелац", False, "направо, налево, прямо и строго на Альфа-Центавру")
car_word.go()
car_word.turn()
car_word.show_speed()
car_word.stop()
