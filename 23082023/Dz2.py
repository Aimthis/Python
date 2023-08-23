list_1 = [1, 4, 3, 7, 8, 9, 12, 2]
k = 10
mostClose = k - list_1[0]
for i in range(len(list_1)):
    if k - list_1[i] >= 0:
        if mostClose >= k - list_1[i]:
            result = list_1[i]
            mostClose = k - list_1[i]
    if k - list_1[i] < 0:
        if mostClose >= (k - list_1[i]) * -1:
            result = list_1[i]
            mostClose = (k - list_1[i]) * -1
print(result)

m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)