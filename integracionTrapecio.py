import math

# ingreso de datos
a = float(input('limite inferior: '))
b = float(input('limite superior: '))
n = int(input('numero de intervalos: '))

# funcion
def tfuncion(x):
    return math.exp(x*x)

# longitud de los intervalos
Dx = (b-a)/n
print('longuitud de los intervalos: ', Dx)

# valor en los extremos
xi = []
i = 0
while i<=n:
    cal = a+i*Dx
    xi.append(cal)
    i += 1
print('valor en los extremos: ', xi)

# calculo de los trapecios
area = 0
for i in range(0, n):
    aT = (tfuncion(xi[i])+tfuncion(xi[i+1]))/2
    T = Dx*aT
    area = area + T

print(area)