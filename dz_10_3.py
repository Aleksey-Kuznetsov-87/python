class Cell:
    def __init__(self, number_of_cells):
        self.number_of_cells = int(number_of_cells)

    def __add__(self, other):    # сложение
        return f'{"сложение равно"} {self.number_of_cells + other.number_of_cells}'

    def __sub__(self, other):    # вычитание
        subtraction_cell = self.number_of_cells - other.number_of_cells
        if subtraction_cell > 0:
            return f'{"разность равна"} {subtraction_cell}'
        else:
            return "Вычитание невозможно"

    def __mul__(self, other):    # умножение
        return f'{"умножение равно"} {self.number_of_cells * other.number_of_cells}'

    def __floordiv__(self, other):    # деление без остатка
        return f'{"деление без остатка равно"} {self.number_of_cells // other.number_of_cells}'

    def make_order(self, cell_row):    # переведём ячейки в ряды
        list_of_cells_in_a_row = []
        division_without_remainder = self.number_of_cells // cell_row    # деление без остатка
        remainder_of_the_division = self.number_of_cells % cell_row    # остаток от деления
        if remainder_of_the_division > 0:    # если остаток от деления больше нуля
            for i in range(division_without_remainder):
                add_to_list = "*" * cell_row + "\n"
                list_of_cells_in_a_row.append(add_to_list)
            add_to_list = "*" * remainder_of_the_division    # а тут высчитаем клетки, если их не хватает на полный ряд
            list_of_cells_in_a_row.append(add_to_list)
        elif remainder_of_the_division == 0:    # если остаток от деления равен нулю
            for i in range(division_without_remainder):
                add_to_list = "*" * cell_row + "\n"
                list_of_cells_in_a_row.append(add_to_list)
        return f'{"количество ячеек по рядам"} {list_of_cells_in_a_row}'


cell_1 = Cell(30)    # количество ячеек в первой клетке
cell_2 = Cell(10)    # количество ячеек во второй клетке
print(cell_1 + cell_2)    # тут пишем любое математическое из: //, *, -, +
print(cell_1.make_order(7))    # задаём количество ячеек в ряду
