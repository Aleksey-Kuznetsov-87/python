import os

folder = 'some_data'    # свой положить в папку со скриптом или распаковать тот, что в комплекте идёт
quantity_files = 0    # счёткик для подсчёта количества файлов
degree_of_construction = 20    # степень возведения


for size_filter in range(degree_of_construction):
    size_threshold = 2 ** size_filter
    if size_filter == 0:    # так мы сможем искать файлы нулевого размера
        size_threshold_old = 0
    else:
        size_threshold_old = 2 ** (size_filter - 1)    # ну а тут уже размеры выше нуля задаются
    size_statistics = [item.name
                       for item in os.scandir(folder)
                       if size_threshold_old <= item.stat().st_size <= size_threshold
                       ]    # добавил только второе сравнение и знаки <= и =>
    temporary_lis = []    # нам нужен пустой список
    for i in size_statistics:
        stub = i.split('.')[-1]    # выдергиваем из имени файла его расширенине
        temporary_lis.append(stub)    # и в список его пихаем
    permanent_list = list(set(temporary_lis))    # преобразуем список
    permanent_list.sort(key=temporary_lis.index)    # чтобы убрать все повторения
    if len(size_statistics) > 0:    # так будем выводить данные непустые
        print(f'{size_threshold}: {len(size_statistics)}', *permanent_list, sep=', ')    # так красивее
    quantity_files = quantity_files + len(size_statistics)    # это чтобы посчитать все файлы и вывести вконце
print("всего ", quantity_files)
