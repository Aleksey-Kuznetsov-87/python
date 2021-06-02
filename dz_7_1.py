import os

root_folder = 'my_project'
list_of_folders = ('settings', 'mainapp', 'adminapp', 'authapp')

if not os.path.exists(root_folder):
    os.mkdir(root_folder)
    os.chdir(root_folder)    # изменяем папку назначения дальнейшей работы скрипта
    for folders_of_list in list_of_folders:    # создаём поочерёдно папки из списка внутри родительской
        dir_path = os.path.join(folders_of_list)
        if not os.path.exists(dir_path):    # проверяем отсутстсвуют ли папки с такими именами
            os.makedirs(dir_path)
else:
    print("Мой лорд, такая директория уже существует")
