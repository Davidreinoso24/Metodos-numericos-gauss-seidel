# -*- coding: utf-8 -*-
"""
Created on Mon May  8 19:14:29 2023

@author: herna
"""
#x1 x2 b
#4x-3y=-1
#x+4y=2

import numpy as np 

Matriz = np.array([[4,-1,0,0],[-1,4,-1,0],[0,-1,4,-1],[0,0,-1,4]])
Result = np.array([[1],[1],[1],[1]])
inicia_x0 = np.array([[0.],[0.],[0.],[0.]])
margen_error = 0.00001
cant_iteraciones = 10
tamaño = np.shape(Matriz)

k = tamaño[0]
z = tamaño[1]
X = np.copy(inicia_x0)
diferencia = np.ones(k, dtype=float)
error = 2*margen_error
iteracion = 0


X_resultados = np.empty((cant_iteraciones, k))

while not (error<=margen_error or iteracion>cant_iteraciones):
    print("iteracion #", iteracion+1)
    for i in range(0, k, 1):
        suma = 0
        for j in range(0, z, 1):
            if i != j:
                suma = suma - Matriz[i,j] * X[j]
        nuevo = (Result[i] + suma) / Matriz[i,i]
        diferencia[i] = np.abs(nuevo - X[i])
        X[i] = nuevo
        print("\tx", i+1, ".", X[i])

    X_resultados[iteracion,:] = X.flatten()
    error = np.max(diferencia)
    iteracion = iteracion + 1


print("Matriz de resultados:")
print(np.round(X_resultados, 6))
    
        











   









