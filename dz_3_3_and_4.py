list_employee = (
    "Иван Иванов", "Никита Хрущёв", "Андрей Нефёдов", "Анна Яровая",
    "Марина Варра", "Антон Санин", "Игорь Нарышкин", "Ярослава Дягтерёва",
    "Иван Сергеев", "Инна Серова"
)


def thesaurus_adv(full_name):
    registry = {}

    for i in full_name:
        first_name, surname = i.split()
        surname_reg = registry.setdefault(surname[0], {})
        name_reg = surname_reg.setdefault(first_name[0], [])
        name_reg.append(i)
    return registry


print(thesaurus_adv(list_employee))
