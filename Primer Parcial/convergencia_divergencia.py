"""
# Convergencia
La diferiencia entre los valores actuales y anteriores tienden a un valor en especifico.
Divergencia: los valores no llevan a un punto en contreto, sino que se dispersan sin seguir un patrón en específico.
"""

# Ejemplo de convergencia
import matplotlib.pyplot as plt

def xnew(xprev):
    return (2*xprev**2 + 3)/5

x0 = 1.4
iteraciones = 1

x0 = 0
x1 = 0 

x0Array = []
x1Array = []

for i in range(100):
    x1 = xnew(x0)
    x0Array.append(x0)
    x1Array.append(x1)
    if abs(x1 - x0) < 0.0000001:
        break
    x0 = x1
    iteraciones += 1
    
    
print("La raiz es %.5f" % x1)
print("Con %d iteraciones" % iteraciones)

plt.plot(x0Array,x1Array)
plt.grid()
plt.show()





