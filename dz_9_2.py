# перечислим переменные
asphalt_thickness = 5  # толщина асфальта в сантиметрах - постоянная величина
weight_of_asphalt = 5  # масса асфальта в кг (на 1 см толщины) - постоянная величина
road_width = 20    # ширина дороги в метрах (меняем на своё усмотрение)
road_length = 5000    # длина дороги в метрах (меняем на своё усмотрение)


class Road:
    def __init__(self, _length, _width):    # длина и ширина асфальта в метрах
        self._length = _length
        self._width = _width

    def volume_asphalt(self):
        # считаем по формуле длина*ширина*масса асфальта для покрытия одного кв. метра
        # дороги асфальтом, толщиной в 1 см*число см толщины полотна
        return (self._length * self._width * (weight_of_asphalt * asphalt_thickness) * asphalt_thickness) / 1000


a = Road(road_width, road_length)    # запускаем и передаём атрибуты
print("На полотно площадь ", a._length * a._width, " м.кв. требуется ", a.volume_asphalt(), " т. асфальта", sep='')
