src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def not_repeated():

    for elem in src:
        if src.count(elem) == 1:
            yield elem


print(*not_repeated())

# или вот так првильнее (разкоментить)
# not_repeated = [elem for elem in src if src.count(elem) == 1]
# print(not_repeated)
