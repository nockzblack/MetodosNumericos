"""
Opetaciones básicas con matrices
"""

def createMatrix(m,n,v):
    auxMatrix = []
    for i in range(m):
        auxMatrix.append([v]*n)
    return auxMatrix

def getDimensions(A):
    return (len(A), len(A[0]))

def copyMatrix(max):
    m,n = getDimensions(max)
    copyMatrix = createMatrix(m,n,0)
    for i in range(m):
        for j in range(n):
            copyMatrix[i][j] = max[i][j]
    return copyMatrix

def sumaMatrix(A, B):
    Am,An = getDimensions(A)
    Bm,Bn = getDimensions(B)
    
    if Am != Bm or An != Bn:
        print("Error en las dimensiones")
        return []

    C = createMatrix(Am, An, 0)
  
    for i in range(Am):
        for j in range(An):
            C[i][j] = A[i][j] + B[i][j]
    return C

def restaMatrix(A, B):
    Am,An = getDimensions(A)
    Bm,Bn = getDimensions(B)
    
    if Am != Bm or An != Bn:
        print("Error en las dimensiones")
        return []
    
    C = createMatrix(Am, An, 0)
  
    for i in range(Am):
        for j in range(An):
            C[i][j] = A[i][j] - B[i][j]
    return C


def productMatrix(A, B):
    Am,An = getDimensions(A)
    Bm,Bn = getDimensions(B)
    
    if Am != Bm:
        print("Error en las dimensiones")
        return []
    
    C = createMatrix(Am, An, 0)
  
    for i in range(Am):
        for j in range(Bn):
            for k in range(An):
                C[i][j] += A[i][k] * B[k][j]
    return C


def detAdyacente(A, r,c):
    Am,An = getDimensions(A)
    C = createMatrix(Am-1, An-1, 0)

    for i in range(Am):
        if i == r:
            continue
        for j in range(An):
            if j == c:
                continue
            ci = 0
            cj = 0
            if (i<r):
                ci = i
            else:
                ci = i-1

            if (j<r):
                cj = j
            else:
                cj = j-1

            C[ci][cj] = A[i][j]

    return C

    
    def 

    
A = createMatrix(5,4,1)
B = copyMatrix(A)

C = createMatrix(3,3,1)
D = createMatrix(3,3,1)

print(productMatrix(C, D))

