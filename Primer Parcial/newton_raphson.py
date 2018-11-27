"""
Metodo de Newton - Raphason

Este aloritmo necesita de un valor inicial que esto lo suficientemente cercano a la solución,
ya que de lo contrario puede diverger. El metodo calcula la tangente del valor actual y se
actualiza con el valor de la intersección en el eje x.

f' = fx0 / (x0 -x1)
x0 - xr = fxo / f'x0

xr = x0 - (fxo / f'x0)


Encontrar la derivada y usar la ecuación para el siguiente punto
2x^2 -5x +3

"""

# f(x) = x^4 -8.6x^3 -351.51x^2 + 464x - 998.46
# f'(x) = 4x^3 - 25.8 x^2 - 703.02 x + 464
def f(x):
    return x**4 -8.6*x**3 -351.51*x**2 + 464*x - 998.46

def fprima(x):
    return 4*x**3 -25.8*x**2 -703.02*x +464

x0 = 7
itera = 0
for i in range(100):
    itera += 1
    xr = x0 - (f(x0)/fprima(x0))
    fxr = f(xr)
    
    if abs(fxr) < 0.000001:
        break
    x0 = xr
    
print("El valor de la raiz es %0.5f" % x0)
print("Numero de itretaciones %i" % itera)