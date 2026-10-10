'''
Ejercicio 1
'''
"""
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

"""
'''
Ejercicio 3
'''
"""
number = int(input("Dime un numero: "))

if number %5 == 0 and number %7 == 0:
    print(f"El numero {number} es multiplo de 5 y 7")
elif number %5 == 0:
    print(f"El numero {number} es multiplo de 5")
elif number %7 == 0:
    print(f"El numero {number} es multiplo de 7")
else:
    print(f"el numero {number} no es multiplo de 5 y 7")
"""

'''
Ejercicio 4
'''
""""
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
"""

'''
Ejercicio 6
'''
"""
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 == 0 or num2 == 0:
    print("Los números 0 no se consideran para esta comparación de múltiplos.")
elif num1 % num2 == 0 or num2 % num1 == 0:
    print(f"Los números {num1} y {num2} sí son múltiplos.")
else:
    print(f"Los números {num1} y {num2} no son múltiplos .")
"""

'''
Ejercicio 7
'''
"""
caracter = input("Introduce un carácter: ")

if caracter == 'a' or caracter == 'A':
    print("Es la primera vocal (A)")
elif caracter == 'e' or caracter == 'E':
    print("Es la segunda vocal (E)")
elif caracter == 'i' or caracter == 'I':
    print("Es la tercera vocal (I)")
elif caracter == 'o' or caracter == 'O':
    print("Es la cuarta vocal (O)")
elif caracter == 'u' or caracter == 'U':
    print("Es la quinta vocal (U)")
else:
    print("El carácter introducido no es una vocal.")
"""
'''
Ejercicio 8
'''
"""
estado_civil = input("Introduce el estado civil (Soltero, Casado, Viudo, Divorciado): ")
edad = int(input("Introduce la edad: "))

if edad > 50 :
    print ("Retenion del 8,5%")
elif edad > 35:
    print ("Retencion del 10,5%")
elif edad>0:
    if estado_civil=="Soltero" or estado_civil=="Divorciado":
        print("Retencion del 12%")
    elif estado_civil=="Viudo" or estado_civil=="Casado":
        print("Retencion del 11,3%")
"""

'''
Ejercicio 9
'''
"""
dia_semana = int(input("Dime el dia de la semana: "))

if 0 <= dia_semana <= 7 :
    print(f"El dia de la semana es {dia_semana}")
else:
    print(f"Error")
"""

'''
Ejercicio 10
'''
"""
hora = int(input("Introduce la hora: "))
minutos = int(input("Introduce los minutos: "))
segundos = int(input("Introduce los segundos: "))

hora2 = int(input("Introduce la hora: "))
minutos2 = int(input("Introduce los minutos: "))
segundos2 = int(input("Introduce los segundos: "))

if 0 <= hora <= 23 and 0 <= hora2 <= 23 and 0 <= minutos <= 59 and 0 <= minutos2 <= 59 and 0 <= segundos <= 59 and 0 <= segundos2 <= 59:
    
    if hora > hora2:
        print(f"{hora} : {minutos}: {segundos} es mayor que {hora2} : {minutos2}: {segundos2}")
    elif hora < hora2:
        print(f"{hora} : {minutos}: {segundos} es menor que {hora2} : {minutos2}: {segundos2}")
    else:
        if minutos > minutos2:
            print(f"{hora} : {minutos}: {segundos} es mayor que {hora2} : {minutos2}: {segundos2}")
        elif minutos < minutos2:
            print(f"{hora} : {minutos}: {segundos} es menor que {hora2} : {minutos2}: {segundos2}")
        else:
            if segundos > segundos2:
                print(f"{hora} : {minutos}: {segundos} es mayor que {hora2} : {minutos2}: {segundos2}")
            elif segundos < segundos2:
                print(f"{hora} : {minutos}: {segundos} es menor que {hora2} : {minutos2}: {segundos2}")
            else:
                print("Las horas son iguales")
else:
    print("Los datos son erroneos")
"""

'''
Ejercicio 11
'''
"""
cliente = input("Introduce si eres un estudiante o estudiante regular: ")
gastado = float(input("¿Cuanto te has gastado? : "))

if cliente == "estudiante" and gastado >=100:
    print("Tienes un descuento del 15%")
    descuento = 0.15
elif cliente == "estudiante" and gastado < 100:
    print("Tienes un descuento del 10%")
    descuento = 0.10
elif cliente == "estudiante regular" and gastado >= 200:
    print("Tienes un descuento del 12%")
    descuento = 0.12
else:
    print("Tienes un descuento del 5%")
    descuento = 0.05

precio_final = gastado * (1 - descuento)

print("Descuento aplicado:", descuento * 100, "%")
print("El precio final es:", precio_final)
"""

'''
Ejercicio 12
'''
"""
dia_semana = int(input("Introduce el dia de la semana: "))
vacaciones = input("¿Esta de vacaciones?: ")

if (1 <= dia_semana <= 5) and (vacaciones == "No" or vacaciones == "no") :
        print(f"En el dia {dia_semana}  {vacaciones} esta de vacaciones y la alarma suena a las 7:00")
elif (6 <= dia_semana <= 7) and (vacaciones == "No" or vacaciones == "no"):
        print(f"En el dia {dia_semana}  {vacaciones} esta de vacaciones  y la alarma suena a las 10:00")
else:
        print(f"En el dia {dia_semana} {vacaciones} esta de vacaciones  y la alarma esta apagada")
"""
'''
Ejercicio 13
'''
"""
caracter = input("Introduce un comparador: ")
numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))

# Operadores + - * /

if caracter == "+":
    solucion = numero1 + numero2
    print("solucion", solucion)
elif caracter == "-":
    solucion = numero1 - numero2
    print("solucion", solucion)
elif caracter == "*":
    solucion = numero1 * numero2
    print("solucion", solucion)
elif caracter == "/":
    if numero2 != 0:
        solucion = numero1 / numero2
        print("solucion", solucion)
    else:
        print("No se puede dividir entre cero")
"""

'''
Ejercicio 14
'''
"""
#monedas: 2€, 1€, 50c, 20c, 10c, 5c, 2c, 1c
mon2 = int(input("¿Cuantas monedas de 2€ tiene?: "))*2*100
mon1 = int(input("¿Cuantas monedas de 1€ tiene?: "))*100
mon50c = int(input("¿Cuantas monedas de 50c tiene?: "))*50
mon20c = int(input("¿Cuantas monedas de 20c tiene?: "))*20
mon10c = int(input("¿Cuantas monedas de 10c tiene??: "))*10
mon5c = int(input("¿Cuantas monedas de 5c tiene??: "))*5
mon2c = int(input("¿Cuantas monedas  de 2c tiene??: "))*2
mon1c = int(input("¿Cuantas monedas  de 1c tiene??: "))

hucha = (mon2+mon1+mon50c+mon20c+mon10c+mon5c+mon2c+mon1c)/100
print(f"Tiene en la hucha un total de {hucha}€")
"""

'''
Ejercicio 15
'''
"""
dia = int(input("Introduce el dia: "))
mes = int(input("Introduce el mes: ")) 
year = int(input("Introduce el año: "))

if year %4==0 and not (year%100==+0):
    print("Ese año es bisiesto")
else:
    print("No es bisiesto")
    if mes ==1  or mes ==3  or mes ==5 or mes ==7  or mes==8 or mes==10 or mes==12:
        if dia <= 31:
            print(f"La fecha {dia} / {mes} / {year} es valida")
        else:
            print("La fecha es invalida")
    elif mes==4 or mes==6 or mes==9 or mes==11:
        if dia <= 30:
            print(f"La fecha {dia} / {mes} / {year} es valida")
        else:
            print("La fecha es invalida")
"""

'''
Ejercicio 16
'''
"""
base = int(input("Dime la base: "))
exponente = int(input("Dime el exponente: "))

if exponente >0 :
    resultado = base ** exponente
    print(resultado)
elif exponente ==0:
    resultado = 1
    print(resultado)
else:
    resultado = 1/(base**exponente)
    print(resultado)
"""

'''
Ejercicio 17
'''
"""
lado1 = float(input("Introduce el primer lado: "))
lado2 = float(input("Introduce el segundo lado: "))
lado3 = float(input("Introduce el tercer lado: "))

if (lado1 + lado2 > lado3 ) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("El triangulo es valido")
    if lado1 == lado2 == lado3:
        print("Triangulo Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triangulo Isósceles")
    else:
        print("Triangulo Escaleno")
        if lado1**2 + lado2**2 == lado3**2 or lado1**2 +lado3**2 == lado2**2 or lado2**2 + lado3**2 == lado1**2 :
            print("Es un triangulo recto")
else:
    print("Triangulo no valido")
"""

'''
Ejercicio 18
'''
"""
numero1 = int(input("Dime el primer numero: ")) 
numero2 = int(input("Dime el segundo numero: "))

if numero1 >= numero2:
    distancia = numero1 - numero2 
else:
    distancia = numero2 - numero1
print ("La distancia que hay entre los numeros es: " , distancia)
"""

'''
Ejercicio 19
'''
"""
alumno = int(input("Introduce el numero de alumnos: "))

if alumno >= 100:
    importe = 65
    print(f"el importe seria: {importe}€")
elif alumno >= 50 and alumno <=99 :
    importe = 70    
    print(f"el importe seria: {importe}")
elif alumno >= 30 and alumno <=49 :
    importe = 95
    print(f"el importe seria: {importe}€")
elif alumno >=0 and alumno < 30:
    importe = 2500
    print(f"el importe seria: {importe}€")
else:
    print(f"Ponga un numero real de alumnos {alumno}")
"""

'''
Ejercicio 20
'''
"""
telefonica = int(input("Introduzca el tiempo que ha estado: "))
semana = input("Introduzca el dia de la semana que ha realizado la llamada (Domingo/Mañana/Tarde): ")

if telefonica <= 10:
    costo = 0.66*telefonica
    print(f"El importe a paga es de {costo} €")
elif telefonica <= 13:
    resto = telefonica - 10
    costo = 10*0.66 + 0.50*resto 
    print(f"El importe a pagar es de {costo} €")
elif telefonica <= 15:
    resto = telefonica - 13
    costo = 10*0.66 + 3*0.50 + 0.45*resto 
    print(f"El importe a pagar es de {costo} €")
else:
    resto = telefonica -15
    costo = 10*0.66 + 3*0.50 + 2*0.45 + resto*0.35
    print(f"El importe a pagar es de {costo} €" )

if semana == "Domingo":
    impuesto = 0.03
    impuesto_total = impuesto*costo
    impuesto_global = costo + impuesto_total
    print(f"Con el impuesto se le quedaria en {impuesto_global}€")
elif semana == "Mañana":
    impuesto = 0.15
    impuesto_total = impuesto*costo
    impuesto_global = costo + impuesto_total
    print(f"Con el impuesto se le quedaria en {impuesto_global}")
else:
    impuesto = 0.10
    impuesto_total = impuesto*costo
    impuesto_global = costo + impuesto_total
    print(f"Con el impuesto se le quedaria en {impuesto_global}")
"""

'''
Ejercicio 21
'''
"""
matematicas = float(input("Ingrese la calificación de Matemáticas: "))
ingles = float(input("Ingrese la calificación de Inglés: "))
programacion = float(input("Ingrese la calificación de Programación: "))
asistencia = float(input("Ingrese el porcentaje de asistencia: "))

if matematicas >= 60 and ingles >= 60 and programacion >= 60:
    if (matematicas + ingles + programacion) / 3 >= 85:
        print("Admitido con beca")
    elif (matematicas + ingles + programacion) / 3 >= 70:
        if asistencia >= 75:
            print("Admitido sin beca")
        else:
            print("Rechazado")
    elif (matematicas + ingles + programacion) / 3 >= 60:
        print("Lista de espera")
    else:
        print("Rechazado")
else:
    print("Rechazado")
"""
