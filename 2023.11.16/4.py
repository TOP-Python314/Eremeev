# ПЕРЕИМЕНОВАТЬ: переменным требуется давать имена по смыслу, так чтобы код можно было удобнее и быстрее читать — имена w, t, b, c, z, r ничего не говорят о том, какие значения ассоциированы с данными переменными — вместо них стоило назвать переменные number, digit1, digit2, digit3, total, product
w = int(input())
t = w % 10
b = w % 100 // 10
c = w // 100
z = t + b + c
r = t * b * c
print(f'Сумма цифр = {z}')
print(f'Произведение цифр = {r}')


# ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробелы после символа # — в большинстве редакторов кода, включая Notepad++, это делает команда "Вкл./Выкл. комментарий" или аналогичная
# 333
# Сумма цифр = 9
# Произведение цифр = 27

# 432
# Сумма цифр = 9
# Произведение цифр = 24

