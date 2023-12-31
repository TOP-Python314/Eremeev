# ПЕРЕИМЕНОВАТЬ: переменным требуется давать имена по смыслу, так чтобы код можно было удобнее и быстрее читать — имя a очень мало говорит о том, какое значение ассоциировано с данной переменной — вместо него стоило назвать переменную number или num
number = int(input())

# ИСПОЛЬЗОВАТЬ везде: в большинстве случаев PEP 8 рекомендует добавлять пробелы вокруг бинарных операторов (исключения: оператор возведения в степень, операторы умножения и деления в длинных выражениях)
# ИСПРАВИТЬ: один вызов функции print() оптимальнее, чем два — используйте возможности функции print()
print(f'Следующее за числом {number} число: {number + 1}',
        f'Для числа {number} предыдущее число: {number - 1}', sep='\n')                     
# print(f'Для числа {number} предыдущее число: {number - 1}'


# ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробелы после символа # — в большинстве редакторов кода, включая Notepad++, это делает команда "Вкл./Выкл. комментарий" или аналогичная
# 23
# Следующее за числом 23 число: 24
# Для числа 23 предыдущее число: 22

# 25
# Следующее за числом 25 число: 26
# Для числа 25 предыдущее число: 24

# 23
# Следующее за числом 23 число: 24
# Для числа 23 предыдущее число: 22

# 24
# Следующее за числом 24 число: 25
# Для числа 24 предыдущее число: 23

# ИТОГ: хорошо, но можно лучше — 2/3
