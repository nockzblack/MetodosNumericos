"""
Metodo Gráfico
El método gráfico consiste en evaluar, graficar e ir haciendo acercamientos al valor que se quere llegar.
La presición de este método depende de la escala de la última gráfica resultante.
"""

import numpy as np
import matplotlib.pyplot as pltç


#Dar valores a x y gráficar f(x) = 2x^2 - 5x + 3
def y(x):
    return 2*x**2 - 5*x + 3

auxArray = np.linspace(0, 2, 100)

#print(auxArray)

resultArray = np.zeros(100)

for i in range(len(auxArray)):
    resultArray[i] = y(auxArray[i])
    
#print(resultArray)

plt.plot(auxArray, resultArray)
plt.grid()
plt.show()


# f(y) = 1 - 400*(3+y) / 9.81*(3y+y^2/2)^3 
def x(y):
    return 1 - (400*(3+y))/(9.81*(3*y + y**2/2)**3)

auxArray = np.linspace(0, 5, 10)

#print(auxArray)

resultArray = np.zeros(10)

for i in range(len(auxArray)):
    resultArray[i] = x(auxArray[i])
    
#print(resultArray)

plt.plot(resultArray, auxArray)
plt.grid()
plt.show()