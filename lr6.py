import xlsxwriter

from prettytable import PrettyTable
from math import exp

def f1(x, u1, u2):
    return (u1 * exp(x)) / (x * u2)

def f2(x, u1, u2):
    return (2 * x / u1) + u2 - 1 

def out(x, u1, U1, u2, U2):
    table.add_row([x, u1, U1, abs(u1 - U1), u2, U2, abs(u2 - U2)])


th = ["x", "u1", "U1", "D(u1 - U1)", "u2", "U2", "D(u2 - U2)"]

table = PrettyTable(th)

a = 3
b = 4
n = 30

h = (b - a) / n


u1_x = [6]
u2_x = [exp(3)]

U1_ls = [6] 
U2_ls = [exp(3)]

x_ls = [a]

out(a, u1_x[0], 2 * a, u2_x[0], exp(a))

for i in range(1, n + 1):
    x = a + i * h

    delta_u1 = h * f1(x, u1_x[i - 1], u2_x[i - 1])
    u1 = u1_x[i - 1] + delta_u1
    U1 = 2 * x

    u1_x.append(u1)

    delta_u2 = h * f2(x, u1_x[i - 1], u2_x[i - 1])
    u2 = u2_x[i - 1] + delta_u2
    U2 = exp(x)

    u2_x.append(u2)

    out(x, u1_x[i], U1, u2_x[i], U2)

    x_ls.append(x)
    U1_ls.append(U1)
    U2_ls.append(U2)
    

print(table)    




excel_grafik = xlsxwriter.Workbook('lr6_grafik.xlsx')

worksheet = excel_grafik.add_worksheet()

worksheet.write('A1', 'X')
worksheet.write('B1', 'u1')
worksheet.write('C1', 'U1')
worksheet.write('D1', 'u2')
worksheet.write('E1', 'U2')

startIndex = 2

for i in range(len(x_ls)):
    worksheet.write(f'A{startIndex}', x_ls[i])
    worksheet.write(f'B{startIndex}', u1_x[i])
    worksheet.write(f'C{startIndex}', U1_ls[i])
    worksheet.write(f'D{startIndex}', u2_x[i])
    worksheet.write(f'E{startIndex}', U2_ls[i])

    startIndex += 1
  
excel_grafik.close()