import xlsxwriter

from prettytable import PrettyTable
from math import sin, cos

def func(x):
    return 0.1 * x ** 3 + x ** 2 - 10 * sin(x)

def integral(a, b):
    return 0.1 * (b ** 4 - a ** 4) / 4 + (b ** 3 - a ** 3) / 3 + 10 * (cos(2) - cos(-4))

def simpsonMethInteg(a, b, m):
    h = (b - a) / (2 * m)

    x = [(a + i * h) for i in range(0, 2 * m + 1)]
    y = [func(i) for i in x]

    temp = y[0] + y[len(y) - 1] 

    for i in y[1:len(y) - 1:2]:
        temp += 4 * i

    for i in y[2:len(y) - 1:2]:
        temp += 2 * i


    return (h / 3) * temp   

def dYexact(x):
    return 0.3 * x ** 2 + 2 * x - 10 * cos(x)

def dYapproximate(a, b, x, h):
    if x == a:
        return -(3 * func(x) - 4 * func(x + h) + func(x + 2 * h)) / (2 * h)
    elif x == b:
        return (func(x - 2 * h) - 4 * func(x - h) + 3 * func(x)) / (2 * h)
    else:
        return (func(x + h) - func(x - h)) / (2 * h)

def dY2exact(x):
    return 0.6 * x + 10 * sin(x) + 2

def dY2approximate(a, b, x, h):
    if x == a or x == b:
        return 0
    else:
        return (func(x + h) - 2 * func(x) + func(x - h)) / h ** 2


b = 2
a = -4

hp = float()
varHP = int()

while not varHP in [1, 2, 3]:
    varHP = int(input("Выберите hp:\n1 - 0.2\n2 - 0.1\n3 - 0.005\n"))

    if varHP == 1:
        hp = 0.2
    elif varHP == 2:
        hp = 0.1
    elif varHP == 3:
        hp = 0.005
    else:
        print("Нет такого варианта, попробуй ещё раз\n")


m = float()
varM = int()

while not varM in [1, 2, 3]:
    varM = int(input("Выберите m:\n1 - 10\n2 - 20\n3 - 40\n"))

    if varM == 1:
        m = 10
    elif varM == 2:
        m = 20
    elif varM == 3:
        m = 40
    else:
        print("Нет такого варианта, попробуй ещё раз\n")

N = int(((b - a) / hp) + 1)

print(N)

x = [round(a + i * hp, len(str(hp).split(".")[1])) for i in range(0, N)]
y = [func(x[i]) for i in range(0, len(x))]


th = ["X", "Y", "Точная производная 1-го порядка", "Приближённая производная 1-го порядка", "Погрешност", "Точная производная 2-го порядка", "Приближённая производная 2-го порядка", "Погрешность"]

table = PrettyTable(th)

"""
excel_grafik = xlsxwriter.Workbook('lr3_grafik.xlsx')

worksheet = excel_grafik.add_worksheet()

worksheet.write('A1', 'X')
worksheet.write('B1', 'Y')
worksheet.write('C1', 'Точная производная 1-го порядка')
worksheet.write('D1', 'Приближённая производная 1-го порядка')
worksheet.write('E1', 'Погрешност')
worksheet.write('F1', 'Точная производная 2-го порядка')
worksheet.write('G1', 'Приближённая производная 2-го порядка')
worksheet.write('H1', 'Погрешность')

startIndex = 2
"""

for i in x:
    dYex = round(dYexact(i), 3)
    dYappr = round(dYapproximate(a, b, i, hp), 3)
    pogrDY = round(abs(dYex - dYappr), 3)

    dY2ex = round(dY2exact(i), 3)
    dY2appr = round(dY2approximate(a, b, i, hp), 3) 
    pogrDY2 = round(abs(dY2ex - dY2appr), 3) 

    xi = i
    y = round(func(xi), 3)

    table.add_row([xi, y, dYex, dYappr, pogrDY, dY2ex, dY2appr, pogrDY2])
"""
    worksheet.write(f'A{startIndex}', xi)
    worksheet.write(f'B{startIndex}', y)
    worksheet.write(f'C{startIndex}', dYex)
    worksheet.write(f'D{startIndex}', dYappr)
    worksheet.write(f'E{startIndex}', pogrDY)
    worksheet.write(f'F{startIndex}', dY2ex)
    worksheet.write(f'G{startIndex}', dY2appr)
    worksheet.write(f'H{startIndex}', pogrDY2)

    startIndex += 1
"""    

#excel_grafik.close()

print(table)    

simpsomInteg = simpsonMethInteg(a, b, m)
exactIntegral = integral(a, b)

print(f"Значение интеграла методом Симпсона: {simpsomInteg}")
print(f"Точное значение интреграла {exactIntegral}")
print(f"Погрешность: {abs(exactIntegral - simpsomInteg)}")

