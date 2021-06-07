import time
# вызовем модуль time, ниже будет функция time.sleep()

color_red = 7    # задаём время таймера красного света (в сек)
color_yellow = 2    # задаём время таймера жёлтого света (в сек)
color_green = 5    # задаём время таймера зелёного света (в сек)


class TrafficLight:    # TrafficLight - класс
    def __init__(self):
        self.__color = None    # __color - приватный атрибут

    def running(self):    # running - метод
        self.__color = "Сигнал светофора - 'Красный'"
        print(self.__color, ". Оставшееся время сек:")
        for time_sec in range(color_red, 0, - 1):    # тут циклом отсчитываем время (чтобы вывести его)
            time.sleep(1)
            print(time_sec, end=' | ')
        print("Уже почти зелёный...")    # переход на новую, а то всё в кучу будте
        self.__color = "Сигнал светофора - 'Жёлтый'"
        print(self.__color, ". Оставшееся время сек:")
        for time_sec in range(color_yellow, 0, - 1):    # тут циклом отсчитываем время (чтобы вывести его)
            time.sleep(1)
            print(time_sec, end=' | ')
        print("Тапок в пол!!!")    # переход на новую, а то всё в кучу будте
        self.__color = "Сигнал светофора - 'Зелёный'"
        print(self.__color, ". Оставшееся время сек:")
        for time_sec in range(color_green, 0, - 1):    # тут циклом отсчитываем время (чтобы вывести его)
            time.sleep(1)
            print(time_sec, end=' | ')
        print()    # переход на новую, а то всё в кучу будте


traffic_lights = TrafficLight()    # создаём экземпляр
traffic_lights.running()    # вызываем метод
