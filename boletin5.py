'''
Ejercicio 1
'''
"""

termino = int(input("Introduce la cantidad de numeros que desee: "))
total = 0
contador = 0

for i in range(1,termino+1):
    total+= int(i*numero)
print(f"{total}")
"""

"""
#WHILE
termino = int(input("Introduce la cantidad de numeros que desee: "))
total = 0
contador = 0
indice = 1

while indice <=termino:
    total+= int(indice*9)
    contador+=1
print(total)
"""

'''
Ejercicio 4
'''
"""
numero = "1"
termino = int(input("Introduce la cantidad de numeros que desee: "))
acumlador = 0

for i in range(termino+1):
    print(numero*i)
    resultado = acumulador*10+9
    acumulador+=1
    total = acumulador
print(f"Ha introducido la cantidad de {termino} y la cantidad de numero es {total}")
"""

'''
Ejercicio 5
'''
numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el primer numero: "))
contador = 0

while contador < 10:
    if numero1%numero2==0:
        print(numero1)
        contador+=1
    numero1+=1



'''
Ejercicio 9
'''
"""
longitud = 9
numero_anterior_del_anterior = 0
anterior = 0
siguiente = 1
cadena = ""

for i in range(longitud):
    cadena+=str(siguiente)
    if i < longitud-1:
        cadena+=" , "
    numero_anterior_del_anterior = anterior
    anterior=siguiente
    siguiente = 3*anterior+2*numero_anterior_del_anterior

print(cadena)
"""



'''
Ejercicio 8
'''
"""
longitud = 5
numero_anterior_del_anterior = 0
anterior = 0
siguiente = 1
cadena = ""

for i in range(longitud):
    cadena+=str(siguiente)
    if i < longitud-1:
        cadena+=" , "
    numero_anterior_del_anterior = anterior
    anterior=siguiente
    siguiente = anterior+numero_anterior_del_anterior

print(cadena)
"""     








'''
Ejercicio 10
'''
"""
aniversario = int(input("Introduce el número total de años trabajados:"))
teclado = 1
teclados_nuevos = 0
recompensa = 300
contador = 1
resultado = 0
total = 0

while aniversario >= contador :
    if contador % 2 == 0:
        total += recompensa
        recompensa+=150
    else:
        teclados_nuevos += teclado
        teclado = teclado * 2

    contador+=1 
print(f"Ha recibido la recompensa de {total}€")
print(f"Ha recibido la recompensa de {teclados_nuevos} teclado/s")
print(f"Ha ganado un total de {total}€ y {teclados_nuevos} teclados")
"""dos")
