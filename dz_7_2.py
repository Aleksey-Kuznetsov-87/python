import re
import os

dirs_list = 'list-of-folders.yaml'    # структура своя, так что как-то так выходит (файл в комплекте)
number_of_spaces = 1
with open(dirs_list, 'r', encoding='utf-8') as file_1:
    for line in file_1:
        line_new = re.sub("[-|\n]", "", line)    # вычищаем всё лишнее из имён (и один первый пробел)
        counter = line_new.count(' ')
        line_new = re.sub("[ ]", "", line_new)    # теперь чистим от пробелов совсем
        if counter == number_of_spaces:    # для одного уровня
            if line_new.count('.') == 1:    # если файл, то создадим его
                text_file = open(line_new, "w", encoding='utf-8')
            else:    # иначе создадим папку
                if not os.path.exists(line_new):
                    os.mkdir(line_new)    # создадим папку
                    os.chdir(line_new)    # перейдём в папку
        elif counter > number_of_spaces:    # если уровнем ниже
            if line_new.count('.') == 1:    # если файл, то создадим его
                text_file = open(line_new, "w", encoding='utf-8')
            else:    # иначе создадим папку
                if not os.path.exists(line_new):
                    os.mkdir(line_new)    # создадим папку
                    os.chdir(line_new)    # перейдём в папку
            number_of_spaces = counter
        elif counter < number_of_spaces:    # если уровнями/уровнем выше
            for _ in range(number_of_spaces - counter):    # перейдём на уровень/уровни выше
                os.chdir('..')    # хз как это сделать по-другому
            if line_new.count('.') == 1:    # если файл, то создадим его
                text_file = open(line_new, "w", encoding='utf-8')
            else:    # иначе создадим папку
                if not os.path.exists(line_new):
                    os.mkdir(line_new)    # создадим папку
                    os.chdir(line_new)    # перейдём в папку
            number_of_spaces = counter
