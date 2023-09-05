# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

n = int(input('Введите количество элементов массива N: '))
arrN = list()
result = list()
for i in range(n):
    arrN.append(int(input(f'Введите {i+1} элемент: ')))
    result.append(arrN[i])
print(arrN)
m = int(input('Введите количество элементов массива M: '))
arrM = list()
for i in range(m):
    arrM.append(int(input(f'Введите {i+1} элемент: ')))
print(arrM)
for i in range(len(arrN) - 1):
    for j in range(len(arrM) - 1):
        if arrN[i] == arrM[j]:
            result.remove(arrN[i])
print(result)