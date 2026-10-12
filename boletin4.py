'''
Ejercicio 1
''' 
"""
#Escribe un programa que pida dos números por teclado y luego muestre en pantalla los números comprendidos entre ellos. 
# Por ejemplo, si se introducen el 5 y el 3, mostrará: 3, 4, 5. Utiliza bucles for y while [for/while].

numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))

for i in range (3,6):
    print(i)

#While
while numero1 <= numero2 :
    print(numero1)
    numero1+=1
"""

'''
Ejercicio 2
'''
"""
# Crea un programa que reciba un número y luego muestre la tabla de multiplicar de dicho número, utilizando únicamente bucles while.
numero = int(input("Introduce por el numero que quieras multiplicar: "))
contador=0

while contador<=10:
    resultado=numero*contador
    print(f"El resultado de la tabla de multiplicar es {numero} X {contador} = {resultado} ")
    contador+=1
"""
'''
Ejercicio 3
'''
# 3. Escribe un programa que pida dos números y muestre en pantalla todos los números de ese rango que sean múltiplos de 11 [for/while].
"""
numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))

for i in range(numero1, numero2+1 ):
    if i%11==0:
        print(f"El rango del primer numero {numero1} y el segundo numero {numero2} son:{i} ")
"""
"""
contador = numero1 #Para el while

while contador <= numero2:
    if contador%11==0:
        print(f"El rango del primer numero {numero1} y el segundo numero {numero2} son:{contador} ")
    contador+=1
"""

'''
Ejercicio 4
'''
# 4. Crea un programa que lea una serie de números por teclado hasta que se introduzca un número menor que 100. 
# Cuando esto ocurra, debe mostrar el número más grande que se haya introducido.
"""
numero = int(input("Introduce el primer numero: "))
max = numero

while numero >= 100:
    if numero > max:
        max = numero
    numero = int(input("Introduce otro numero: "))
print(f"El numero mas grande es: {max}")
"""
'''
Ejercicio 5
'''
# 5. Crea un programa que reciba números hasta que se introduzca un número fuera del rango [0, 10.000]. 
# En ese momento, informará de cuántos números se han introducido, así como de su valor máximo y su media.  
# "Se han introducido 50 números, con un máximo de 27 y un promedio de 3,28."
""" #no se hacerlo 
numero = int(input("Introduce un numero: "))

while 0 <= numero <= 10000:
    max = numero
"""

'''
Ejercicio 6
'''
# 6. Escribe un programa que pida un entero positivo n y devuelva la suma de los números entre 1 y n. 
# Si el número no es un entero positivo, debe informar del error y volver a pedirlo. 
# Desarróllalo utilizando ambos tipos de bucles y también sin bucles.
""" #no se hacerlo
n = int(input("Introduce un numero: "))
contador = 0

for i in range(1+n):
    contador+=1
    if contador >= 0:
        print("La suma es positiva")
    else:
        print("La suma no es positiva")
"""

# 7. Crea un programa similar al anterior, pero que reciba dos enteros positivos n y m, 
# y devuelva la suma de los números entre n y m. Verifica que los datos de entrada sean válidos.


# 8. Crea un programa que reciba dos números numero_1 y numero_2 y devuelva su producto 
# sin utilizar el operador de multiplicación (*). Los números pueden ser enteros positivos o negativos.

numero_1 = int(input("Introduce el primer numero: "))
numero_2 = int(input("Introduce el segundo numero: "))
contador = 0

if numero_2 < 0:
    for i in range(-numero_2):
        contador -= numero_1
else:
    for i in range(numero_2):
        contador += numero_1

print(f"El producto es {contador}")

# 9. Diseña un programa que realice la operación módulo (%) de dos números, 
# sin utilizar ni el operador módulo ni la división.


# 10. Escribe un programa que pregunte al usuario cuántos números positivos desea introducir y luego se los pida por consola. 
# Si el usuario introduce un número no válido, se le volverá a pedir (el número no válido no cuenta para el total). 
# Una vez introducidos todos los números, mostrará el promedio, el máximo y el mínimo.