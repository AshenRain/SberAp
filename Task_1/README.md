![Image alt](https://github.com/AshenRain/SberAp/raw/main/Task_1/1.jpg)

```
import copy

def read_floats():
    return map(float, input().split(','))

def gauss(a):
    ''' приведение матрицы к ступенчатому виду '''
    n = len(a)
    mat = copy.deepcopy(a)
    temp = [0]*n  
    total = 1
    for i in range(0, n):
        index = i        
        while(index < n and mat[index][i] == 0):
            index += 1
        if(index == n):  
            continue
        if(index != i):
            for j in range(0, n):
                mat[index][j], mat[i][j] = mat[i][j], mat[index][j]
        for j in range(0, n):
            temp[j] = mat[i][j]
        for j in range(i+1, n):
            num1 = temp[i]     
            num2 = mat[j][i]   
            for k in range(0, n):
                 mat[j][k] = (num1*mat[j][k]) - (num2*temp[k])
            total = total * num1
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

n,m = [int(i) for i in input().split(',')]

while(n != m):
    print("Неккоректная размерность матрицы \n"
          "Обратная матрица может существовать только для квадратных мартиц \n"
          "Попробуйте ввести размерность еще раз \n")
    n,m = [int(i) for i in input().split(',')]

matrix = []
for i in range(n):
    matrix.append(list(read_floats()))

matrix = inverse(matrix)
if matrix != None:
    print('\n')
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print('{:.4f}'.format(matrix[i][j]),end = ' ')
        print()
```