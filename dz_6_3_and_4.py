from itertools import zip_longest


def users_and_hobbies():
    with open('hobby.csv', 'r', encoding='utf-8') as hobbi_f, \
         open('users.csv', 'r', encoding='utf-8') as user_f, \
         open('conclusion.csv', 'w', encoding='utf-8') as out_f:

        for name, hobbies in zip_longest(user_f, hobbi_f):
            if name is None:
                exit(1)
            else:
                name = name.strip()
                if hobbies is not None:
                    hobbies = hobbies.strip()
                out_f.write(f'{name}: {hobbies}\n')
                print(f'{name}: {hobbies}')


users_and_hobbies()
