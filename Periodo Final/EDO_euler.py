"""
Ecuaciones Diferenciales por el metodo de Euler

Este metodo calcula la pendiente de una curva que se desconoce pero satisface la
ecucacion diferencial dada. De tal forma que la ecuacion es una formula que nos da
la pendiente de la recta tangente en cualquier punto de la curva.
Para esto es necesario una condicion inicial.

"""


# EDO dx/dy = e**x condiciones iniciales y(0) = 1
# tarea dx/dy
import numpy as np
import math
import matplotlib.pyplot as plt
n = 50
a = 0
b = 5 # este es propuesto
h = abs(a-b)/(n-1)
x = np.linspace(a,b,n)
y0 = 1


def fprima(x,y):
    return math.exp(x)

def euler(h,x, y0):
    y = []
    y.append(y0)
    for i in range(1,len(x)):
        y.append(y[i-1] + h*y[i-1])
    return y

y = euler(h,x,y0)
print(y)

plt.plot(x,y,'b')
plt.plot(x,[math.exp(xi) for xi in x],'r')