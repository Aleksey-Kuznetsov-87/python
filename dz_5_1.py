int_user = int(input("Введите целое число, для итерации квадрата нечётных чисел от 1 "))


def nums_generator(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


nums_gen = nums_generator(int_user)
print(*nums_gen, sep=', ')
