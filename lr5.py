from math import cos, sin

def f(x):
    return x * cos(x) - x

def dY(x):
    return -x * sin(x) + cos(x) - 1 

def MP3(x1, h, epsilon = 0.0001):
    d1 = dY(x1)

    if d1 < 0:
        h = -h

    x2 = x1 + h

    d2 = dY(x2)

    if (d2 - d1) / h < 0:
        print("Начальное приближение выбрано неверно")   

        return None  

    y1 = f(x1)
    y2 = f(x2)

    z1 = x1 - x2

    p = (d1 - d2 - 2 * (y1 - y2 - d2 * z1) / z1) * (z1 ** 2)
    q = (d2 - d1 + 3 * (y1 - y2 - d2 * z1) / z1) * z1

    r = d2

    zm = (-q + (q ** 2 - 3 * p * r) ** 0.5) / (3 * p)

    iterations = 1

    while abs(zm) > epsilon:
        z1 = x1 - x2

        p = (d1 - d2 - 2 * (y1 - y2 - d2 * z1) / z1) / (z1 ** 2)
        q = (d2 - d1 + 3 * (y1 - y2 - d2 * z1) / z1) / z1

        r = d2

        zm = (-q + (q ** 2 - 3 * p * r) ** 0.5) / (3 * p)

        x1 = x2
        y1 = y2
        d1 = d2

        x2 = x2 + zm

        y2 = f(x2)
        d2 = dY(x2)

        iterations += 1

    MP3 = x2 + zm

    return [MP3, iterations] 



a = 2
b = 18
m = 50
step = (b - a) / 50
h = [10 ** -2, 10 ** -3, 10 ** -4, 10 ** -5, 10 ** -7, 10 ** -10, 10 ** -15]   

approxPoints = [2.5, 9, 15]

for i in h:
    iterations = 0
    localMin = []

    for j in approxPoints:
        rez = MP3(j, step, i)
        localMin.append(rez[0])
        iterations += rez[1]

    print(f"Точность = {i}")

    for k in range(len(localMin)):
        print(f"Точка минимума {k + 1} - ({localMin[k]}, {f(localMin[k])})")

    print(f"Число итераций: {iterations}")    
    print("----------------------------------------------") 
