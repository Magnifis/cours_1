# Спросить у пользователя размер интервала (в секундах). Вывести на экран строку в зависимости от размера интервала:

# 1) до минуты: <s> сек;
# 2) до часа: <m> мин <s> сек;
# 3) до суток: <h> час <m> мин <s> сек;
# 4) сутки или больше: <d> дн <h> час <m> мин <s> сек

# Например, если пользователь введет 4567 секунд, вывести:
# 1 час 16 мин 7 сек

a = int(input("Введите колличество секунд:"))
days = (a // 86400)
hour = (a // 3600) % 24
minutes = (a // 60) % 60
seconds = a % 60
if hour < 10:
    hour = '0'+str(hour)
else:
    hour = str(hour)
if minutes < 10:
    minutes = '0'+str(minutes)
else:
    minutes = str(minutes)
if seconds < 10:
    seconds = '0'+str(seconds)
else:
    seconds = str(seconds)
print(str(days)+':'+'дней'+','+str(hour)+':'+'час(ов)'','+str(minutes)+':'+'минут'+','+str(seconds)+':'+'секунд')
