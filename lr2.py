import xlsxwriter

from math import sin

def calcX(a, b, m):
    listX = []

    for i in range(1, m + 1):
        xi = a + (i - 1)*(b - a) / (m - 1)

        listX.append(xi)

    return listX

def calcY(listX):
    listY = []

    for x in listX:
        y = fx(x)

        listY.append(y)

    return listY  

def calcXJ(a, b):
    listXJ = []

    for j in range(1, 22):
        xj = a + (j - 1) * (b - a) / 20

        listXJ.append(xj)

    return listXJ

def fx(x):
    return 0.1 * x ** 3 + x ** 2 - 10 * sin(x)

def PNL(xj):
    if x[0] <= xj <= x[len(x) - 1]:
        index = 1
        for i in range(len(x)):
            if xj <= x[i]:
                index = i
                break

        return y[index - 1] + (xj - x[index - 1]) * (y[index] - y[index - 1]) / (x[index] - x[index - 1])         
    else:
        return None

def printRez():
    PNLxj_list = []
    fxj_list = []

    for i in xj:
        PNLxj = PNL(i)
        fxj = fx(i)
        if PNLxj:
            PNLxj_list.append(PNLxj)
            fxj_list.append(fxj)

            print(f"x = {i} N1(Xt) = {PNLxj} F(Xt) = {fxj} F(Xt)-N1(Xt) = {abs(fxj - PNLxj)}")

"""
    excel_grafik = xlsxwriter.Workbook('lr2_grafik.xlsx')

    worksheet = excel_grafik.add_worksheet()

    worksheet.write('A1', 'xj')
    worksheet.write('B1', 'PNL(xj)')
    worksheet.write('C1', 'F(xj)')

    startIndex = 2
    for i in range(len(xj)):
        worksheet.write(f'A{startIndex}', xj[i])
        worksheet.write(f'B{startIndex}', PNLxj_list[i])
        worksheet.write(f'C{startIndex}', fxj_list[i])

        startIndex += 1

    excel_grafik.close()
"""


m = 11
a = -4
b = 2

x = calcX(a, b, m)
y = calcY(x)
xj = calcXJ(a, b)

printRez()