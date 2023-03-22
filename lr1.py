def fillSMat():
    sMat = [[0 for j in range(len(matrix))] for i in range(len(matrix))]
    dMat = [0 for i in range(len(matrix))]

    for i in range(len(matrix)):

        dMat[i] = calcD(i, dMat, sMat)

        for j in range(len(matrix)):
            if i == 0 and j == 0:
                    sMat[i][j] = abs(matrix[i][j]) ** 0.5
            elif i == j:
                sum = 0

                for k in range(0, i):
                    sum += dMat[k] * abs(sMat[k][i]) ** 2

                sMat[i][j] = abs(matrix[i][i] - sum) ** 0.5   
            elif i < j:
                sum = 0

                for k in range(0, i):
                    sum += dMat[k] * sMat[k][i] * sMat[k][j]

                sMat[i][j] = (matrix[i][j] - sum) / (sMat[i][i] * dMat[i])


    return sMat, dMat

def calcD(index, matD, matS):

    sum = 0
    for i in range(index):
        sum += matD[i] * abs(matS[i][index]) ** 2

    return sign(matrix[index][index] - sum)

def transponSMat():
    transSMat = [[0 for j in range(0, len(sMat))] for i in range(len(sMat))]

    for i in range(len(sMat)):
        for j in range(len(sMat)):
            transSMat[j][i] = sMat[i][j]

    return transSMat

def findY():
    matY = [[0 for j in range(len(sMat))] for i in range(len(sMat))]

    for i in range(0, len(sMat)):
        for j in range(0, len(sMat)):
            if i == 0 and j == 0:
                matY[i] = b[i] / (sMat[i][i] * dMat[i])
            else:
                sum = 0

                for k in range(0, i):
                    sum += (sMat[k][i] * matY[k] * dMat[k])
                
                matY[i] = (b[i] - sum) / (sMat[i][i] * dMat[i])


    return matY


def findX():
    matX = []

    for i in range(len(y) - 1, -1, -1):
        if i == len(y) - 1:
            matX.append(y[i] / trSMat[i][i])
        else:
            sum = 0

            for k in range(i + 1, len(y)):
                sum = sum + (trSMat[k][i] * matX[len(y) - k - 1])  

            matX.append((y[i] - sum) / trSMat[i][i])      

    return matX

def calcDiscrepancy():
    rez = []
    for i in range(len(matrix)):

        sum = 0
        for j in range(len(matrix)):
            sum += matrix[i][j] * x[j]

        rez.append(b[i] - sum)

    return max(rez)

def sign(num):
    return -1 if num < 0 else 1 if num > 0 else 0;


def printRezult():
    for i in range(len(x)):
        print(f"x{i + 1} = {x[i]}")

    print(f"Невязка равна: {calcDiscrepancy()}")


d = -8
q = -4.88

matrix = [[-4.88, 1, 0, 0, 0], [1, -2, 1, 0, 0], [0, 1, -2, 1, 0], [0, 0, 1, -2, 1], [0, 0, 0, 1, -4.88]]
b = [0, -8, -8, -8, 0]

sMat, dMat = fillSMat()

trSMat = transponSMat()

y = findY()

x = findX()[::-1]

printRezult()





