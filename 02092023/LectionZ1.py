# list = [1,2,3,5,8,15,23,38]
# result = list()
# for i in range(len(list)):
#     if list[i]%2==0:
#         result.append((i,i**2))

# map
# def select(f, col):
#     return [f(x) for x in col]

# filter
# def where(f, col):
#     return [x for x in col if f(x)]


data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x**2), res))
print(res)
