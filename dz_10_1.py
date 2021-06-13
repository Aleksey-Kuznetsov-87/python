class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):    # в этом методе превращаем многомерный список в матрицу (масло маслянное)
        matrix_str = ''    # объявим пустую переменную для будущей матрицы ('' потому что строки)
        for line in self.matrix:    # порно какое получится - работаем со строками, а не числами :)
            for column in range(len(line)):    # для столбцов по индексам счёт (от длины строки - количество значений)
                matrix_meaning = str(line[column])    # переводим число в строковый формат
                matrix_str = matrix_str + matrix_meaning + " "   # пробел для красоты (всё равно str, а не int)
            matrix_str = matrix_str + "\n"    # переносим строку, а то не матрица будет )
        return matrix_str    # вернём полученное значение

    def __add__(self, other):    # тут сложить две матрицы
        matrix_sum = []    # вот сюда и засунем сумму матриц
        for index_m1_row in range(len(self.matrix)):    # индекс строки
            for index_m1_cols in range(len(self.matrix[index_m1_row])):    # индекс столбца
                # выводим сумму по индексам от каждой переменной
                sum_intermediate = self.matrix[index_m1_row][index_m1_cols] + other.matrix[index_m1_row][index_m1_cols]
                matrix_sum.extend([sum_intermediate, " "])    # добавляем в список
            matrix_sum.append("\n")    # засунем сюда же перенос (чтоб точно матрица получилась)
        return matrix_sum    # возвращаем сумму матриц


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])    # рандомные списки, одинаковый размер
matrix_2 = Matrix([[4, 5, 6], [8, 9, 10], [1, 2, 3]])    # рандомные списки, одинаковый размер
print("матрица m1", "\n", matrix_1, sep='')    # выводим первую матрицу
print("матрица m2", "\n", matrix_2, sep='')    # выводим вторую матрицу
print("сумма матриц - новая матрица", "\n", *matrix_1 + matrix_2, sep='')
# print(*m1 + m2, sep='')    # чтобы юзать сложение в классах, надо задействовать функцию "def __add__(self, other):"
# внимание! print(*m1 + m2, sep='') сработает только при одинаковой длине списков!!!
