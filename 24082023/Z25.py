# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

stroka = "a a a b c a a d c d d"
stroka = stroka.split()
vihod = ""
for i in range(len(stroka)):
    lastone = stroka[:i]
    if lastone.count(stroka[i])<1:
        vihod += stroka[i] + " "
    else:
        vihod += stroka[i] + "_" + str(lastone.count(stroka[i])) + " "
print(vihod)