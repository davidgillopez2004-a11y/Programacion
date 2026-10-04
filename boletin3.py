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


'''
Ejercicio 8
'''
estado_civil = input("Introduce el estado civil (S-Soltero, C-Casado, V-Viudo, D-Divorciado): ")
edad = int(input("Introduce la edad: "))

if edad > 50:
    print(f"Segun su edad {edad} hay un 8,5% como usted")
elif (estado_civil == 'S' or estado_civil == 's' or estado_civil == 'D' or estado_civil == 'd') and edad < 35:
        print(f"Segun su edad {edad} hay un 12% como usted")
elif (estado_civil == 'V' or estado_civil == 'v' or estado_civil == 'C' or estado_civil == 'c') and edad < 35:
        print(f"Segun su edad {edad} hay un 11,3% como usted")
else:
        print(f"Segun su edad {edad} hay un 10,5% como usted")


'''
Ejercicio 9
'''

dia_semana = int(input("Dime el dia de la semana: "))

if dia_semana <= 7 :
    print(f"El dia de la semana es {dia_semana}")
else:
    print(f"Error")


'''
Ejercicio 10
'''
