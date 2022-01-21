"""
Title:  Interpolacion de Newton
Author: Julian David Reales de la Ossa

Abstract
Realize el metodo de interpolacion de Newton, para hallar un valor interpolado para un dato xi, que se encuentra entre un conjunto de datos (x,y).
El programa presentara como resultado el valor interpolado o f(xi).

Note: Este programa solo regresa el valor que deseamos conocer mediante el metodo de interpolacion de newton.

"""
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd     # no usada
import math

x = []
y = []
ndatos = int(input("Digite el numero de datos:\t"))
for i in range(0,ndatos):
    xn = float(input(f"\n x{i+1}\t"))
    yn = float(input(f"y{i+1}\t"))
    x.append(xn)
    y.append(yn)

xi = float(input(f"\n Dato a interpolar:\t"))

### --- Creacion de la matriz de las diferencias divididas --- ###
def getDiffTable(X, Y):
    n = len(X)
    A = np.zeros([n, n])
    for i in range(0, n):           
        A[i][0] = Y[i]
    for j in range(1, n):
        for i in range(j, n):
            A[i][j] = (A[i][j - 1] - A[i - 1][j - 1]) / (X[i] - X[i - j])
    return A

difDiv = getDiffTable(x, y)         # matriz de las diferencias divididas

### --- Creacion de vector con los valores de los coeficientes --- ###
def valoresCoeficientes(valor):
    n = len(valor)
    B = np.zeros([1,n])
    for i in range(0,n):
        B[0][i-1] = difDiv[i-1,i-1]
    return B    

coef = valoresCoeficientes(x)       # matriz de coeficientes en orden

### --- Valor interpolado --- ###
def interpolarValor(Xi):
    difX = 1                        # guarda las diferencias (xi-x0)*...*(xi-xn-2)
    n = len(Xi)
    P = 0
    for i in range(0,n):
        if i == 0:
            P = coef[0,0]
        else:
            s = xi-x[i-1]           # (xi-xn)
            difX = difX*s           # suma valores a xx
            P = P+coef[0, i]*difX
    return P

resInterp = interpolarValor(x)
print(f"\n El valor interpolado de {xi}, es {resInterp}")

print(difDiv)
