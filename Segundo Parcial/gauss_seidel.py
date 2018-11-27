"""
Gauss-seidel

Este sistema permite resolver sistemas de ecuaciones lineales que produzcan una matriz cuadrada
de coeficientes con elementos no nulos en la diagonal domiante.
Para asegurar la convergencia de este método se tiene que garantizar que la matriz es diagonalmente
dominante. 
"""

def getx1(x2,x3):
    return (8 + 0.2*x2 + 0.5*x3)/3

def getx2(x1,x3):
    return (-19.5 -0.1*x1 - 0.4*x3)/7

def getx3(x1,x2):
    return (72.4 -0.4*x1 + 0.1*x2)/10


#Valores iniciales
x1 = 0
x2 = 0
x3 = 0
error = 0.01
x1a = 0.00001
x2a = 0.00001
x3a = 0.00001

for i in range(100):
    x1 = getx1(x2,x3)
    x2 = getx2(x1,x3)
    x3 = getx3(x1,x2)
    print("itera %d"%i,x1,x2,x3)
    #Calculo de errores
    ex1 = abs((x1a - x1)/x1a)
    ex2 = abs((x2a - x2)/x2a)
    ex3 = abs((x3a - x3)/x3a)
    
    if ex1 < error and ex2 < error and ex3 < error:
        break
    
    x1a = x1
    x2a = x2
    x3a = x3
    
print("Los valores son",x1,x2,x3)