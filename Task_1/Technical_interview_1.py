"""
def read_floats():
    return map(float, input().split(','))

n,m = [int(i) for i in input().split(',')]

if n == m:
    array = []
    for i in range(n):
        array.append(list(read_floats()))
    print(array) #удалить

    #Рассчет определителя
    ## вычисление определителя методом Гаусса 
    ## 1 привести матрицу к треугольному виду
    ## 2 перемножить значения диагонали 

else:
    print("Неккоректная размерность матрицы")

"""

import copy

def gauss1(a): 
    ''' приведение матрицы к ступенчатому виду '''
    # не переживает ноль в матрице
    am = copy.deepcopy(a)
    for k in range(len(a) - 1):
        at = copy.deepcopy(am)
        for i in range(len(a)):
            for j in range(len(a)):
                if(i <= k): 
                    am[i][j] = at[i][j]
                elif(i > k and j > k and at[k][k] != 0): #придумать что-то с делением на ноль
                    am[i][j] = round(at[i][j] - (at[i][k] / at[k][k]) * at[k][j], 4)
                elif(i > k and j <= k):
                    am[i][j] = 0
    return am

def gauss2(a):
    #не правильно считает для 4 ранговых матриц
    n = len(a)
    am = copy.deepcopy(a)
    for i in range(n):
        # выбираем опорный элемент
        j = max(range(i,n), key=lambda k: abs(am[k][i]))
        if i != j:
            am[i],am[j] = am[j],am[i]
        # убеждаемся, что матрица не вырожденная
        if am[i][i] == 0:
            return 0
        # "обнуляем" элементы в текущем столбце
        for j in range(i+1,n):
            b = am[j][i] / am[i][i]
            am[j] = [am[j][k]-b*am[i][k] for k in range(n)]
    return am

def gauss(a):
    n = len(a)
    mat = copy.deepcopy(a)
    temp = [0]*n  # temporary array for storing row
    total = 1

    # loop for traversing the diagonal elements
    for i in range(0, n):
        index = i  # initialize the index
 
        # finding the index which has non zero value
        while(index < n and mat[index][i] == 0):
            index += 1
 
        if(index == n):  # if there is non zero element
            # the determinant of matrix as zero
            continue
 
        if(index != i):
            # loop for swapping the diagonal element row and index row
            for j in range(0, n):
                mat[index][j], mat[i][j] = mat[i][j], mat[index][j]

        # storing the values of diagonal row elements
        for j in range(0, n):
            temp[j] = mat[i][j]
 
        # traversing every row below the diagonal element
        for j in range(i+1, n):
            num1 = temp[i]     # value of diagonal element
            num2 = mat[j][i]   # value of next row element
 
            # traversing every column of row
            # and multiplying to every row
            for k in range(0, n):
                # multiplying to make the diagonal
                # element and next row element equal
                 mat[j][k] = (num1*mat[j][k]) - (num2*temp[k])
            total = total * num1  # Det(kA)=kDet(A);
    mat[0][0] /= total
    return mat 	

def determinant(a): 
    ''' рассчет определителя для ступенчатой матрицы '''
    step_matrix = gauss(a)
    delta = 1 
    for i in range(len(a)):
        delta *= step_matrix[i][i]
    return delta
    
def addition_minor(k,t,a): 
    ''' возвращает матрицу без k-ый строки и t столбца '''
    m = []
    for i in range(len(a)):
        if i != k:
            tmp = []
            for j in range(len(a)):
                if j != t:
                    tmp.append(a[i][j])
            m.append(tmp)
    return m

def addition(k,t, a):
    ''' определение алгебраического дополнения '''
    minor = addition_minor(k,t,a)
    if len(minor) == 2:
        ad = (-1)**(k + t) * (minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0])
    else:
        ad = (-1)**(k + t) * determinant(minor)
    return ad

def transpose(a):
    ''' транспонирование матрицы '''
    for i in range(len(a)): 
        j = 0
        while(j < i):
            a[j][i],a[i][j] = a[i][j],a[j][i]
            j +=1

def inverse(a):
    ''' нахождение обратной матрицы '''
    inv_matrix = []
    delta = determinant(a)
    if delta == 0:
        print('Обратной матрицы не существует')
        return None
    transpose(a)
    for i in range(len(a)):
        tmp = []
        for j in range(len(a)):
            tmp.append(addition(i,j,a)/delta)
        inv_matrix.append(tmp)
    return inv_matrix

matrix0 = [[-1, 0,-2], 
           [ 2,-1, 5], 
           [ 3,-2, 4]]

matrix1 = [[ 5, 2,-2], 
           [ 2, 0, 3], 
           [ 1,-2, 4]]

matrix2 = [[ 2, 7, 3],
            [ 3, 9, 4],
            [ 1, 5, 3]]

matrix3 = [[ 2, 7, 3, 4],
           [ 3, 9, 4, 5],
           [ 1, 5, 3, 6],
           [ 3, 1, 3, 1]]

matrix4 =  [[0,0],
            [0,0]]

matrix = [[-1, 2,-2], 
          [ 2,-1, 5], 
          [ 3,-2, 4]]

matrix = inverse(matrix)
if matrix != None:
    print('\n')
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print('{:.4f}'.format(matrix[i][j]),end = ' ')
        print()


"""
3,3
-1,2,-2
2,-1,5
3,-2,4

a = 10
"""