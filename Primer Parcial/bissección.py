"""
Bissección

Este método busca encontrar la raíz de un polinomio, para ello necesita
un rango inicial donde haya un cambio de signo y va dividiendo el rango por mitad
hasta encontrar la solución.

La limitante es que la solución tiene que encontrarse dentro del rango inicial
y solo encuntra una raíz dentro de este rango.
"""

import math
import numpy as np
import matplotlib.pyplot as plt

"""
xarray=np.linspace(X0,X1,100)
yarray=np.zeros(100)


for i in range(100):
    yarray[i]=fun(xarray[i])


plt.plot(xarray,yarray)
plt.grid()
"""


# f(x) = x^3 - 7x^2 + 14x - 6
def fun(c):
    return c**3 - 7*(c**2) + 14*c - 6

#Elegir valores iniciales x0 y x1
#donde haya un cambio de signo
x0 = 3.2
x1 = 4

for i in range (100):
    f0 = fun(x0)
    f1 = fun(x1)
    if f0*f1 > 0:
        print("No hay raíz en este rango")
        break
        
    x = (x0+x1)/2
    fx = fun(x)

    if fx*f1 < 0:
        x0 = x
    else:
        x1=x
    if abs(fx) < 0.00001:
        break
        
print("la raiz es %.5f"%x0)


# f(y) = 1 - 400*(3+y) / 9.81*(3y+y^2/2)^3 
def fun(y):
    return 1 - (400*(3+y))/(9.81*(3*y + y**2/2)**3)

#Elegir valores iniciales x0 y x1
#donde haya un cambio de signo
x0 = 0.5
x1 = 2.5
iterations = 0
for i in range (100):
    f0 = fun(x0)
    f1 = fun(x1)
    if f0*f1 > 0:
        print("No hay raíz en este rango")
        break
        
    x = (x0+x1)/2
    fx = fun(x)

    if fx*f1 < 0:
        x0 = x
    else:
        x1=x
    if abs(fx) < 0.01:
        break
    if iterations == 10:
        break
    iterations += 1
        
print("la raiz es %.5f"%x0)