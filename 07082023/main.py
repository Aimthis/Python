# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
n = input('Введите количество монет :')
revers = input('Введите количество монет лежащих гербом вверх :')
avers = n - revers
if avers > revers:
    print('Минимальное количество монет для переворота: ', revers)
else:
    print('Минимальное количество монет для переворота: ', avers)