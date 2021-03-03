# Задание 5
# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп.
# Например:
# 57 руб 08 коп, 46 руб 51 коп, 97 руб 00 коп, ...
#
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
#
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
#
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
#
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?


# def the_prices_tag(rub,penny):
#     for n in prices:
#         rub = int(n)
#         penny = int(n * 100) % 100
#         print(f' {rub} руб {penny :02} коп')
#         return
# Попытался сделать функцию чтобы избавится от дублирования,она не работает(

prices = [54.34, 34.4, 53.23, 86.4, 85.74, 93.67, 12.23, 90.76, 89.7, 69.9, 45.65, 43.50, 74.67]

for n in prices:
    rub = int(n)
    penny = int(n * 100) % 100
    print(f' {rub} руб {penny :02} коп')

# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
print('<<<<<<<<<<<< 2 >>>>>>>>>>>>>')
print(prices, id(prices))
prices_1 = prices
prices_1.sort()
for n in prices_1:
    rub = int(n)
    penny = int(n * 100) % 100
    print(f' {rub} руб {penny :02} коп')

print(prices_1, id(prices_1))

# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
print('<<<<<<<<<<<< 3 >>>>>>>>>>>>>')

print(id(prices), prices)
prices_reversed = list(reversed(prices))

for n in prices_reversed[:5]:
    rub = int(n)
    penny = int(n * 100) % 100
    print(f' {rub} руб {penny :02} коп')

print(id(prices), prices)
print(id(prices_reversed), prices_reversed)

# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
print('<<<<<<<<<<<< 4 >>>>>>>>>>>>>')
for n in prices[8:]:
    rub = int(n)
    penny = int(n * 100) % 100
    print(f' {rub} руб {penny :02} коп')



