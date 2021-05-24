tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '11Б'
]


def gen_list():

    for index_tutors in range(len(tutors)):
        if index_tutors < len(klasses):
            yield tutors[index_tutors], klasses[index_tutors]
        else:
            yield tutors[index_tutors], None


generate_list = gen_list()
print(*generate_list)
