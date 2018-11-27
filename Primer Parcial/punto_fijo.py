"""
Punto Fijo

Este metodo iterativo permite encontrar raíces de funciones f(x) cambiandolas a la forma
x = g(x)

2x^2 -5x + 3 = 0
-2x^2 + 3 = 5x

x1 = (2x0^2 + 3) / 5

x1-x0 aproxime a 0
"""


def xnew(xprev):
    return (2*xprev**2 + 3)/5

x0 = 1.4

iteraciones = 1
for i in range(100):
    x1 = xnew(x0)
    if abs(x1 - x0) < 0.0000001:
        break
    x0 = x1
    iteraciones += 1
  
print("La raiz es %.5f" % x1)
print("Con %d iteraciones" % iteraciones)