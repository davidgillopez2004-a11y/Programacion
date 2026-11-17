"""
Ejercicio 1
"""

import random as libreria_aleatoria
"""
def generar_numeros_aleatorios(cantidad, limite_superior):

    listas = []

    for i in range(10):
        listas.append(libreria_aleatoria.randint(1, limite_superior))

lista = generar_numeros_aleatorios(10,100)
"""

'''
Apartado A
'''

"""
def obtener_mayor_pares(numeros):
    mayor = 0

    for numero in numeros:
        if numero%2==0 and numero>mayor:
            mayor = numero

    return mayor

assert(obtener_mayor_pares([1,3,5,6,8,10, 1])==10)
assert(obtener_mayor_pares([1,12,5,6,8,10, 1])==12)
"""

'''
Apartado B
'''

"""
def obtener_menor_impares(numeros):
    menor = 0

    for numero in numeros:
        if numero%2!=0 and numero<menor:
            menor = numero
    return menor

assert(obtener_mayor_pares([1,3,5,6,8,10, 1])==1)
assert(obtener_mayor_pares([12,5,6,8,10, ])==5)
"""

'''
Apartado c
'''

"""
def calcular_sumatorio(numeros):
    #sum(numeros)
    suma = 0
    for n in numeros:
        suma+=n
    return suma
"""

'''
Apartado E
'''
"""
lista = [1,2,1,2,3,4,5]

def es_sustituir(lista,antiguo,nuevo):
    for i in range(len(lista)):
        if lista[i]==antiguo:
            lista[i]=nuevo
    
    return lista

print(lista)
es_sustituir(lista,2,3)
print(lista)
"""

'''
Apartado F
'''

def es_eliminacion(lista,elemento_a_eliminar):
    while elemento_a_eliminar in lista:
        lista.remove(elemento_a_eliminar)
    return lista
lista = [1,2,1,2,3,4,5]

assert(len(es_eliminacion(2,5)))
