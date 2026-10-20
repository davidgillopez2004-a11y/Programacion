'''
Ejercicio 1
''' 

#Escribe un programa que pida dos números por teclado y luego muestre en pantalla los números comprendidos entre ellos. 
# Por ejemplo, si se introducen el 5 y el 3, mostrará: 3, 4, 5. Utiliza bucles for y while [for/while].
"""
numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))

for i in range (numero1,numero2):
    print(i+1)

#While
if numero1 <= numero2:
    while numero1 <= numero2:
        print(numero1)
        numero1+=1
elif numero2 <= numero1:
    while numero2 <= numero1:
        print(numero2)
        numero2+=1
else:
    print("fallo del sistema")
""" 

'''
Ejercicio 2
'''

# Crea un programa que reciba un número y luego muestre la tabla de multiplicar de dicho número, utilizando únicamente bucles while.
"""
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
"""
numero = int(input("Introduce un numero: "))
contador = 0
max = numero
suma = 0

while numero >= 0 and numero <= 10000:
    contador+=1
    suma+=numero
    print(numero)
    if numero > max:
        print(f"El numero {numero} es mayor que el numero maximo que ha puesto {max}")
    else:
        print(f"El numero {numero} es menor que el numero maximo que ha puesto {max}")
    numero=int(input("Introduce un numero entre el 0 y el 10000: "))
    if contador > 0:
        resultado = suma/contador
        print(f"Se ha introducido un total de {contador} numeros, con el valor maximo de {max} y una media de {resultado}")
    else:
        print("Numero no valido")
"""
'''
Ejercicio 6
'''
# 6. Escribe un programa que pida un entero positivo n y devuelva la suma de los números entre 1 y n. 
# Si el número no es un entero positivo, debe informar del error y volver a pedirlo. 
# Desarróllalo utilizando ambos tipos de bucles y también sin bucles.

#FOR
"""
n = int(input("Introduce un numero: "))
contador = 0

for i in range(1,1+n):
    contador+=i
if contador >= 0:
    print(f"La suma es positiva: {contador}")
else:
    print(f"La suma no es positiva: {contador}")
"""
#While
"""
n = int(input("Introduce un numero: "))
contador = 0

while n <= 0:
    print("Introduce un numero positivo")
    n = int(input("Introduce un número: "))
for i in range(1,1+n):
    contador+=i
if contador >= 0:
    print(f"La suma es positiva: {contador}")
else:
    print(f"La suma no es positiva: {contador}")
"""

#Sin bucles
"""
n = int(input("Introduce un numero: "))
contador = 0

resultado = (n*(n+1)) //2
print(f"La suma da un total de {resultado}")
"""

# 7. Crea un programa similar al anterior, pero que reciba dos enteros positivos n y m, 
# y devuelva la suma de los números entre n y m. Verifica que los datos de entrada sean válidos.
#FOR
"""
n = int(input("Introduce un numero: "))
m = int(input("Introduce un numero: "))
contador = 0

for i in range(n,m+1):
    contador+=i
if contador >= 0:
    print(f"La suma es positiva: {contador}")
else:
    print(f"La suma no es positiva: {contador}")
"""

# 8. Crea un programa que reciba dos números numero_1 y numero_2 y devuelva su producto 
# sin utilizar el operador de multiplicación (*). Los números pueden ser enteros positivos o negativos.
"""
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
"""
# 9. Diseña un programa que realice la operación módulo (%) de dos números, 
# sin utilizar ni el operador módulo ni la división.
"""
dividiendo = int(input("Introduce el dividiendo: "))
divisor = int(input("Introduce el divisor: "))

resultado = dividiendo-divisor
if divisor == 0:
    print("No se puede dividir entre cero")
else:
    resultado = dividiendo

while resultado >= divisor:
    resultado -= divisor
print(f"El resto es: {resultado}")
"""
# 10. Escribe un programa que pregunte al usuario cuántos números positivos desea introducir y luego se los pida por consola. 
# Si el usuario introduce un número no válido, se le volverá a pedir (el número no válido no cuenta para el total). 
# Una vez introducidos todos los números, mostrará el promedio, el máximo y el mínimo.
"""
numero = int(input("¿Cuántos números positivos quieres introducir? "))

contador = 0
suma = 0

while contador < numero:
    numero = int(input("Introduce un número positivo: "))

    if numero > 0:
        suma = suma + numero
        contador = contador + 1

        if contador == 1:
            maximo = numero
            minimo = numero
        else:
            if numero > maximo:
                maximo = numero

            if numero < minimo:
                minimo = numero
    else:
        print("Número no válido. Inténtalo de nuevo.")

promedio = suma / numero

print(f"El promedio es: {promedio}")
print("El máximo es:", maximo)
print("El mínimo es:", minimo)
"""

#11.Escribe un programa que reciba un valor y cree una pirámide de asteriscos de esa altura (cada línea contiene un número impar de asteriscos). 
#Por ejemplo, para el valor 3 tendrías:
"""
altura = int(input("Introduce la altura de la piramide: "))

for i in range(1, altura + 1):
  espacios = " " * (altura - i)
  asteriscos = "*" * (2 * i - 1)
  print(espacios + asteriscos)
"""
#12.Crea un programa que reciba un número entero positivo mayor que 0 y luego informe si es un número perfecto, 
# considerando que un número es perfecto si es igual a la suma de todos sus divisores.
"""
numero = int(input("Introduce un número mayor que 0: "))
contador = 0

for i in range(1, numero):
    if (numero%i == 0):
        contador += i
while numero < 0:
    numero = int(input("Intentalo de nuevo: "))
if (contador == numero):
    print(f"El {numero} es perfecto.")
else:
    print(f"El {numero} no es perfecto.")
"""

#13.Escribe un programa para mostrar los n términos de una serie armónica y su suma.
#La serie armónica contiene términos 1/1 + 1/2 + 1/3 + 1/4 + 1/5 \dots 1/n. Entrada de número de términos: 5   
# Salida esperada: $1/1 + 1/2 + 1/3 + 1/4 + 1/5$   
#Suma de la serie hasta 5 términos: 2.283334
"""
numero = int(input("Introduce un numerin: "))
contador = 0
armonica = ""

for i in range(1,numero+1):
    contador=contador + 1 / i
    if i == 1:
        armonica = "1/" + str(i)
    else:
        armonica = armonica + " + 1/" + str(i)
print(armonica)
print(f"La suma total de los 5 primeros numeros {numero} = {contador}") 
"""
#14.Escribe un programa en Python para mostrar un patrón en forma de diamante
"""
altura = int(input("Introduce la altura de la piramide: "))

for i in range(1, altura + 1):
  espacios = " " * (altura - i)
  asteriscos = "*" * (2 * i - 1)
  print(espacios + asteriscos)

for i in range(altura - 1, 0, -1):
  espacios = " " * (altura - i)
  asteriscos = "*" * (2 * i - 1)
  print(espacios + asteriscos)
"""

#15. Dado un número, escribe un programa para calcular su factorial, considerando que el factorial de un número se define como 1 * 2 * 3 * ... * número. 
# Además, para el caso en que el número sea 0, el factorial es 1.
"""
numero = int(input("Introduce un numero: "))
factorial = 1

for i in range (1,numero+1):
    factorial*=i
print(f"El factorial del numero que has asignado {numero} el factorial es {factorial}")
"""
