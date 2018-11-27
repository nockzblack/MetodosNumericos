"""
Errores
Debido a que se van obteniendo aproximaciones hasta llegar a un resultado. Es necesario calcular el
error en cada iteración ya que este nos dice que tan exacto es nuestro resultado.

Vr = VE + Error 

Error = Vreal - VEstimado

E% = (Vreal - VEstimado) / Vreal

#Precision vs Exactitud

La precisión se logra cuando al repetir un evento se obtienen resultadaos similares aunque sin obtener el correcto.
Y la exactitud se busca obtener el resultado mas cercano al correcto.

Como ingeniero se busca la precisión


y = x^3 -7x^2 + 8x + 0.35
x = 1.37

y = (x^2 -7x +8) x + 0.35

"""

def y(p):
    return p**3 - 7*p**2 + 8*p + 0.35

y(1.37)