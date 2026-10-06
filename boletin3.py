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
    
'''
Ejercicio 9
'''

dia_semana = int(input("Dime el dia de la semana: "))

if 0 <= dia_semana <= 7 :
    print(f"El dia de la semana es {dia_semana}")
else:
    print(f"Error")

'''
Ejercicio 10
'''

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

'''
Ejercicio 11
'''
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

'''
Ejercicio 12
'''

dia_semana = int(input("Introduce el dia de la semana: "))
vacaciones = input("¿Esta de vacaciones?: ")

if (1 <= dia_semana <= 5) and (vacaciones == "No" or vacaciones == "no") :
        print(f"En el dia {dia_semana}  {vacaciones} esta de vacaciones y la alarma suena a las 7:00")
elif (6 <= dia_semana <= 7) and (vacaciones == "No" or vacaciones == "no"):
        print(f"En el dia {dia_semana}  {vacaciones} esta de vacaciones  y la alarma suena a las 10:00")
else:
        print(f"En el dia {dia_semana} {vacaciones} esta de vacaciones  y la alarma esta apagada")

'''
Ejercicio 13
'''

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

'''
Ejercicio 14
'''
#No se como hacerlo
monedas = int(input("¿Cuantas monedas tiene?: "))
contador = 0
#monedas: 2€, 1€, 50c, 20c, 10c, 5c, 2c, 1c

if monedas > 2: 


'''
Ejercicio 15
'''
#Da mal
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

'''
Ejercicio 18
'''
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
