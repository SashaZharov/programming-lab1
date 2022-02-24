import copy

# Возведение в квадрат
def sqrMatrix(matrix):
    answ = [[0]*len(matrix) for i in range(len(matrix[0]))]
    if len(matrix) == len(matrix[0]):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                for k in range(len(matrix)):
                    answ[i][j] += matrix[i][k] * matrix[k][j]
    else:
        print("Невозможно возвести в квадрат матрицу, т.к она не квадратная")
    print(answ)


# Транспонирование матрицы
def transMatix(matrix):
    answ = [[0]*len(matrix) for i in range(len(matrix[0]))]
    if len(matrix) == len(matrix[0]):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                answ[i][j] = matrix[j][i]
        print(answ)
    else:
        print("Невозможно транспонировать матрицу, т.к она не квадратная")


# поиск определителя
def detMatrix(matrix):
    def minor(matrix, i, j):
        M = copy.deepcopy(matrix)
        del M[i]
        for i in range(len(matrix[0]) - 1):
            del M[i][j]
        return M

    def detM(matrix):
        m = len(matrix)
        n = len(matrix[0])
        if m != n:
            return None
        if n == 1:
            return matrix[0][0]
        k = 1
        det = 0

        for j in range(n):
            det += matrix[0][j]*k*detM(minor(matrix, 0, j))
            k *= -1
        return det

    if detM(matrix) == None:
        print("Матрица не квадратная")
    else:
        print(detM(matrix))


# Создаем путсую матрицу
m, n = map(int, input("Введите кол-во строк и столбцов матрицы: ").split())
print(n, m)
matrix = [[0]*n for i in range(m)]
print(matrix)

# Значения
elem_count = m*n
elements = list(map(int, input().split()))
if len(elements) == m*n:
    print(elements)
else:
    print("Количество елементов не совпадает с размером матрицы")

# заполнение матрицы
a = 0
while a < len(elements):
    for i in range(m):
        for j in range(n):
            matrix[i][j] = elements[a]
            a += 1
print(matrix)

action = int(
    input("Введите действие (квадрат - 1, детерминант - 2, транспонировать - 3) "))
print(action)
if action == 1:
    sqrMatrix(matrix)

elif action == 2:
    detMatrix(matrix)

elif action == 3:
    transMatix(matrix)

else:
    print("Введено неизвестное действие")
