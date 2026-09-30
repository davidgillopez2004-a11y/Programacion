'''
Ejercicio 1
'''

numero_entero = int(input("Dime un numero: "))

if numero_entero %2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")


'''
Ejercicio 2
'''

number1 = int(input("Dame un numero: "))
number2 = int(input("Dame un numero: "))

if number1 == number2:
    print("Son iguales")
elif number1 > number2:
    print("El numero 1 es mayor que el numero 2")
else:
    print("El numero 1 es mas pequeño que el numero 2")


'''
Ejercicio 3
'''

number = int(input("Dime un numero: "))

if number %5 == 0:
    print(f"El numero {number} es multiplo de 5")
elif number %7 == 0:
    print(f"El numero {number} es multiplo de 7")
else:
    print(f"El numero {number} es multiplo de 5 y 7")

'''
Ejercicio 4
'''

years = int(input("Dime tu edad: "))

if years >=0 and years <= 6:
    print(f"En la etapa de los {years} estabas en Educacion infantil")
elif years >= 7 and years <= 11:
    print(f"En la etapa de los {years} estaabs en Educacion primaria")
elif years >= 12 and years <= 16:
    print(f"En la etapa de los {years} estabas en Enseñanza Obligatoria")
elif years >=17 and years  <= 65:
    print(f"En la etapa de los {years} estabas en post-Obligatoria")
else:
    print("Ha ocurrido un error")

'''
Ejercicio 5
'''
number = int(input("Dime el primer numero: "))
number2 = int(input("Dime el segundo numero: "))
number3 = int(input("Dime el tercer numero: "))
number4 = int(input("Dime el cuarto numero: "))

media = (number + number2 + number3 + number4) /4

if number and number2 and number3 and number4 < media:
    print(f"Es menor a la media {media}")
elif number and number2 and number3 and number4 > media:
    print(f"Es mayor a la media {media}")
else:
    print(f"Estas muy por debajo de la media {media}")
