"""
Elminación Gaussiana

Es un metdodo para resolver sistemas de ecuaciones lineales 
La complejidad en tiempo de ejecución de este algoritmo es n^3

"""


#Eliminacion gaussiana

def createMatrix(m,n,v):
    C = []
    for i in range(m):

        C.append([v]*n)

    return C



MA = createMatrix(4,5,0)

MA[0] = [1,-1,2,-1,-8]

MA[1] = [2,-2,3,-3,-20]

MA[2] = [1,1,1,0,-2]

MA[3] = [1,-1,4,3,4]



for i in range(4):
    pivote = MA[i][i]

    if pivote == 0:
        for j in range(i+1,4):
            if MA[j][i] != 0:
                T = MA[j]
                MA[j] = MA[i]
                MA[i] = T
                pivote = MA[i][i]
                break

    for k in range(5):
        MA[i][k] = (1/pivote)*MA[i][k]
    for j in range(i+1,4):
        C = -1* MA[j][i]
        T = createMatrix(1,5,0)

        for k in range(5):
            T[0][k] = C*MA[i][k]

        for k in range(5):
            MA[j][k] += T[0][k]

print(MA)

B = createMatrix(4,1,0)

for i in range(3, -1, -1): # the 3 depends of the size
    B[i][0] = MA[i][4]
    for j in range(3,-1, -1):
        if (i == j):
            break
        B[i][0] -= MA[i][j]*B[j][0]

print(B)