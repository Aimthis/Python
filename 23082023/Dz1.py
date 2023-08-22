list_1 = [1, 4, 3, 7, 8, 9, 2, 2]
k = 2
counter = 0
i = 0
while i < len(list_1):
    if k == list_1[i]:
        counter += 1
    i += 1
print(counter)

count = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        count += 1
print(count)