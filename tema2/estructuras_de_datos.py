"""
Ejercicio 1
"""

'''
A,B,C
'''
"""
import random as libreria_aleatoria

listas = []
max_par = 0
min_impar = 0
suma = 0

for i in range(10000):
    listas.append(libreria_aleatoria.randint(1,1000000))

    if i % 2==0 and i > max_par:
        max_par = i
    else:
        if i < min_impar:
            min_impar = i
    suma = suma + i

print(f"La lista es {listas}")
print(f"El numero mayor par es {max_par}")
print(f"El numero menor impar es {min_impar}")
print(f"El total de la suma es {suma}")
"""

import random

