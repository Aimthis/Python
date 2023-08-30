a = 3
b = 5


def f(a, b):
    if b == 1:
        return a
    if b != 1:
        return a * f(a, b - 1)


print(f(a, b))
