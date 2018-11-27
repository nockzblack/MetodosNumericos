"""
# Bairstow

Este algoritmo obtiene las raíces de un polinomio de cualquier grado haciendo uso de la
diivisión sintetica par air bajando el grando del polinomio y así llegar un polinomio
grado 2 y ir aplicando la formula general para ecuaciones cuadrática y de ahí conociendo
2 raíces ir subiendo hasta llegar a la riaz de grado superior del polinomio.

f(x) = x^5 - 3.5x^4 +2.75x^3 +2.125x^2 -3.875x + 1.25
"""

"""
# Ejemplo Bairstow
# f(x) = x^5 - 3.5x^4 +2.75x^3 +2.125x^2 -3.875x + 1.25
# 1.25, -3.875, 2.125, 2.75, -3.5, 1

def bn(coeficientes):
    return coeficientes[-1]

def bn1(a, b, r):
    return a[-2] + r*b

# (n1, bn)
def bi(i, a,r, s,b):
    return a[i] + r*b[0] + s*b[1]

def cn(b):
    return b[-1]


def cn1(b,c,r):
    return bn1(b,c,r)

def ci(i,b,r,s,c):
    return bi(i,b,r,s,c)
    

r = -1
s = -1
for i in range (100):
    b = []
    c = []
    b.append(bn([1.25, -3.875, 2.125, 2.75, -3.5, 1]))
    b.insert(0, bn1([1.25, -3.875, 2.125, 2.75, -3.5, 1], b[0], r))

    print(b)

    for i in reversed(range(0,4)):
        print(i)
        b.insert(0, bi(i,[1.25, -3.875, 2.125, 2.75, -3.5, 1], r,s,b))


    c.append(cn(b))
    c.insert(0, cn1(b,c[0],r))
    for i in reversed(range(0,4)):
        c.insert(0, ci(i,b,r,s,c))


    #print(b)
    #print(c)

    def deltaS(b,c):
        return (-b[1]/c[2] + b[0]/c[1]) / (c[3]/c[2] - c[2]/c[1])

    def deltaR(b,c,dS):
        return -1*b[0]/c[1] - (c[2]/c[1])*dS

    dS = deltaS(b,c)
    dR = deltaR(b,c,dS)


    if abs(dS) < 0.01  and abs(dR) <0.01:
        break

    r = r + dR
    s = s + dS

print(b)
print(dS)
print(dR)

"""


#Ejemplo Bairstow 
# f(x) = x^4 -8.6x^3 -351.51x^2 + 464x - 998.46
# [-998.46, 464, -351.51, -8.6, 1]
import math

def cuadratica(a,b,c):
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        rdiscriminante = math.sqrt(discriminante)
        x1 = (-b + rdiscriminante )/(2*a)
        x2 = (-b - rdiscriminante )/(2*a)
        return [(x1,0),(x2,0)]
    if discriminante == 0:
        x = -b / (2*a)
        return [(x,0),(x,0)]
    xr = -b / (2*a)
    xi = math.sqrt(abs(discriminante)) / (2*a)
    return [(xr,xi),(xr,-xi)]

def bn(a):
    return a[-1]
def bn1(a,b,r):
    return a[-2] + r*b

def bi(i,a,r,s,b):
    return a[i] + r*b[0] + s*b[1]

def cn(b):
    return bn(b)
def cn1(b,c,r):
    return bn1(b,c,r)
def ci(i,b,r,s,c):
    return bi(i,b,r,s,c)

r = -1
s = -1
b = []
raices = []
a = [-998.46, 464, -351.51, -8.6, 1]
while True:
    for i in range(100):
        b = []
        c = []
        b.append(bn(a))
        b.insert(0, bn1(a,b[0],r))
        limit = len(a) - 2
        for i in reversed(range(0,limit)):
            b.insert(0,bi(i,a,r,s,b))

        c.append(cn(b))
        c.insert(0,cn1(b,c[0],r))
        for i in reversed(range(0,limit)):
            c.insert(0,ci(i,b,r,s,c))

        def deltaS(b,c):
            return ((-b[1]/c[2]) + (b[0]/c[1])) / ((c[3]/c[2]) - (c[2]/c[1]))

        def deltaR(b,c,dS):
            return (-b[0]/c[1]) - ((c[2]/c[1])* dS)

        dS = deltaS(b,c)
        dR = deltaR(b,c,dS)

        if abs(dS) < 0.01 and abs(dR) < 0.01:
            break
        r = r + dR
        s = s + dS

    raices.insert(0,cuadratica(1,-r,-s))

    
    a = b[2:]
    grade = len(a)
    if grade == 3: 
        raices.insert(0,cuadratica(a[2],a[1],a[0]))
        break
    if grade == 2: 
        raices.insert(0,-a[0]/a[1])
        break

print(raices)