input_quantity = int(input("Сколько шуток вы хотите прочитать? "))    # вводим данные

import random


def get_jokes(joke):

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["весёлый", "яркий", "зелёный", "утопичный", "мягкий"]
    list_joke = []
    for _ in range(joke):
        nouns_random = random.choice(nouns)
        adverbs_random = random.choice(adverbs)
        adjectives_random = random.choice(adjectives)
        joke_new_lst = f'{nouns_random} {adverbs_random} {adjectives_random}'
        list_joke.append(joke_new_lst)
    return list_joke


print(get_jokes(input_quantity))
