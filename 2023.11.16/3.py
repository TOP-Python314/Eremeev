# ПЕРЕИМЕНОВАТЬ: переменным требуется давать имена по смыслу, так чтобы код можно было удобнее и быстрее читать — имя q очень мало говорит о том, какое значение ассоциировано с данной переменной — вместо него стоило назвать переменную minutes
minutes = int(input())
# ИСПРАВИТЬ: используйте оператор целочисленного деления
print(f'{minutes} мин - {int(minutes // 60)} час {minutes % 60} минут')


# ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробелы после символа # — в большинстве редакторов кода, включая Notepad++, это делает команда "Вкл./Выкл. комментарий" или аналогичная
# 200
# 200 мин - 3 час 20 минут

# 170
# 170 мин - 2 час 50 минут
# 165
# 165 мин - 2 час 45 минут

# ИТОГ: хорошо, но можно лучше — 2/3
