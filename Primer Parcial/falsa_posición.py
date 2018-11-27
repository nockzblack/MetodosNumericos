"""
Falsa Posición

Con este metódo tambien es neceario un rango incial de signos opuestos donde se encuentre la raiz.
con cada iteración el rango se aproxima a la solución obteniendo la interseción en el eje x de la recta
que se forma entre los 2 puntos del rango actual.
"""


import math
import numpy as np
import matplotlib.pyplot as plt

"""
#Elegir valores iniciales x0 y x1
#donde haya un cambio de signo
xarray=np.linspace(10,25,100)
yarray=np.zeros(100)

for i in range(100):
    yarray[i]=fun(xarray[i])

plt.plot(xarray,yarray)
plt.grid()
"""

# f(x) = x^2 - 10 = 0
def fun(c):
    return c**2 -10

x0 = 3
x1 = 3.2

for i in range (100):
    f0 = fun(x0)
    f1 = fun(x1)
    if f0*f1 > 0:
        print("N hay raíz en este rango")
        break
        
    x = x1 - (fun(x0)*(x0-x1))/(fun(x0)-fun(x1))
    fx = fun(x)
    if fx*f1 < 0:
        x0=x
    else:
        x1=x
    if abs(fx) < 0.05:
        break
        
print("la raiz es %.5f"%x0)



# f(y) = 1 - 400*(3+y) / 9.81*(3y+y^2/2)^3 
def fun(y):
    return 1 - (400*(3+y))/(9.81*(3*y + y**2/2)**3)

x0 = 0.5
x1 = 2.5
iter = 0
for i in range (100):
    f0 = fun(x0)
    f1 = fun(x1)
    if f0*f1 > 0:
        print("No hay raíz en este rango")
        break
        
    x = x1 - (fun(x0)*(x0-x1))/(fun(x0)-fun(x1))
    fx = fun(x)
    if fx*f1 < 0:
        x0=x
    else:
        x1=x
    if abs(fx) < 0.05 or iter == 10:
        break
    iter += 1
   
        
print("la raiz es %.5f"%x0)
