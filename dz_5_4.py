src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
numb_max = []


def max_number():

    for i in range(len(src)):
        if i == len(src) - 1:
            break
        else:
            if src[i] < src[i + 1]:
                numb_max.append(src[i + 1])
    yield numb_max


print(*max_number())
