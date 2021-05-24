int_user = int(input("Введите целое число, для итерации квадрата нечётных чисел от 1 "))

nums_gen = (num for num in range(1, int_user + 1, 2))
print(*nums_gen, sep=', ')
