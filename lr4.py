from math import sin


def MS(a, b, epsilon):
    x0 = b
    x1 = a
    X = x1 - (f(x1) * (x1 - x0) / (f(x1) - f(x0)))

    while abs(X - x1) >= epsilon:
        x0 = x1
        x1 = X

        X = x1 - (f(x1) * (x1 - x0) / (f(x1) - f(x0)))

        print(f"Предполагаемый корень - {X}")
        print(f"Разность - {abs(X - x1)}")


    return X

def f(x):
    return 0.1 * x ** 3 + x ** 2 - 10 * sin(x) - 8

a = -4.0
b = 4.0
e = 10 ** -6

intervals = [[-4, -2], [-1, 0], [2, 4]]
listX = []


for i in intervals:
    listX.append(MS(i[0], i[1], e))

for i in range(len(listX)):
    print(f"x{i + 1} = {listX[i]}")


