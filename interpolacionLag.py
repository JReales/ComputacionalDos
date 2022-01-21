"""
Created on Thu Dec 16 20:44:39 2021

@Title:  Interpolacion de Lagrange

@Author: Julian David Reales de la Ossa

Abstract
Realize el metodo de interpolacion de Lagrange, para hallar un valor
interpolado para un dato "xinter", que se encuentra entre un conjunto
de datos (x,y).
El programa presentara como resultado el valor interpolado o f(xi),
el polinomio obtenido y una grafica que representa esos datos.
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

VALUE = True
while VALUE:
    try:
        # """ Datos """
        xi = []
        fi = []
        ndatos = int(input("Digite el numero de datos:\t"))
        for i in range(0,ndatos):
            xn = float(input(f"\n x{i+1}\t"))
            yn = float(input(f"y{i+1}\t"))
            xi.append(xn)
            fi.append(yn)

        # Dato a interpolar.
        xinter = float(input("\n Dato a interpolar:\t"))

        N = len(xi)
        x = sym.Symbol("x")  # x como variable simbolica
        POLINOMIO = 0  # POLINOMIO objetivo

        # """ Terminos de Lagrange """
        for i in range(0, N, 1):
            NUMERADOR = 1  # terminos del NUMERADOR
            DENOMINADOR = 1  # terminos de DENOMINADOR

            for j in range(0,N,1):
                if i!=j:
                    NUMERADOR = NUMERADOR*(x-xi[j])
                    DENOMINADOR = DENOMINADOR*(xi[i]-xi[j])

                ### Expresion f(xi)*((x - xj)/(xi - xj))
                termino = (NUMERADOR/DENOMINADOR)*fi[i]
            POLINOMIO = POLINOMIO + termino  # creacion del POLINOMIO

        # """ Simplificacion del POLINOMIO para la muestra """
        Polisimple = sym.expand(POLINOMIO)
        print(Polisimple)

        # """ Para evaluar datos en el POLINOMIO """
        Px = sym.lambdify(x, POLINOMIO)

        a = np.min(xi)
        b = np.max(xi)
        MUESTRAS = 101

        p_xi = np.linspace(a, b, MUESTRAS)
        pfi = Px(p_xi)

        # """ Evaluacion del dato a interpolar """
        pxinter = Px(xinter)
        print(f"\n El valor interpolado de {xinter} es {pxinter}")

        # """ Grafica de los resultados """
        plt.plot(xinter, pxinter, "ro", markersize=10, linewidth=4)  # dato a interpolar
        plt.plot(xi, fi, "o")  # puntos (x,y)
        plt.plot(p_xi, pfi)  # funcion

        plt.title("Interpolacion de Lagrange")
        plt.xlabel(r"$x$")
        plt.ylabel(r"$f(x)$")
        plt.grid(True)

        plt.show()

        VALUE = False
    except ValueError:
        print("Error: Debe ingresar un numero entero")
