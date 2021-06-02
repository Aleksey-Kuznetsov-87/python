import os
import shutil

main_folder = 'templates'    # не создавать! скрипт всё сделает
dir_path = 'my_project'    # запустить сначало dz_7_2 или распаковать файл из комплекта в папку со скриптом

if os.path.exists(dir_path):    # проверяем доступна ли папка с именем 'my_project'
    if not os.path.exists(main_folder):    # проверяем отсутстсвует ли папка с именем 'templates'
        os.makedirs(main_folder)
        for root, dirs, files in os.walk(dir_path):    # выводим из папки всё, что есть
            for file in files:
                if file[-5:] == '.html':    # костыль, аж кровь из глаз (но переделывать не хочу)
                    name_dir = os.path.join(main_folder, os.path.basename(root))    # собтраем путь и имя (main_folder)
                    if not os.path.exists(name_dir):    # если папка отсутствует (в main_folder)
                        os.makedirs(name_dir)    # то создадим её
                    shutil.copyfile(os.path.join(root, file), os.path.join(name_dir, file))
                    # выше - копирование с путями и именами файлов. откуда и куда, через заяпятую
        print("Файлы с расширением '.html' скопированы с родительской дерикторией в ", "'", main_folder, "'", sep='')
    else:
        print("Диреткория с именем ", "'", main_folder, "'", " уже есть. УДОЛИ!", sep='')
else:
    print("Директория с именем ", "'", dir_path, "'", " не существует.", sep='')
