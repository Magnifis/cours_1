# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
def thesaurus(*args):
    dictionary = {}
    for name in args:
        first_letter = name[0]
        dictionary.setdefault(first_letter, [])
        dictionary[first_letter].append(name)
    return dictionary


d = thesaurus("Иван", "Мария", "Петр", "Илья")
for first_letter in sorted(d.keys()):
    print(f'{first_letter}: {d[first_letter]}')


# Подумайте: полезен ли будет вам оператор распаковки? нет
# Сможете ли вы вернуть отсортированный по ключам словарь? нет