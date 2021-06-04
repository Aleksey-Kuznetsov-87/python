
def val_checker(valid):
    def wrapper(func):
        def validation_check(*args):
            if valid(*args):
                result = func(*args)    # вот тут прям волшебство (как оно работает то?)
                return result
            else:
                raise ValueError(f'Wrong value: {args}')

        return validation_check

    return wrapper


@val_checker(lambda x: x > 0)    # проверка - значение должно быть больше нуля
def count_cube(x):
    return x ** 3


print(count_cube(7))
