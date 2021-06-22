
class ComplexNumber:
    def __init__(self, actual_number, imaginary_number):
        self.complex_number = complex(actual_number, imaginary_number)    # святой яндекс подсказал

    def __add__(self, other):    # сложение
        return self.complex_number + other.complex_number

    def __mul__(self, other):    # умножение
        return self.complex_number * other.complex_number


# для сложения и умножения комплексных чисел, их должно быть минимум два
a = ComplexNumber(-2, 8)    # 1 - действительное число, 2 - мнимая часть
b = ComplexNumber(3.5, -4)    # 1 - действительное число, 2 - мнимая часть
print(a + b)
print(a * b)
