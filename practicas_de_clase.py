'''
Se practica la concatenacion. 
Los comodines %s sirve como para declarar las variables
de una manera mas breve
'''
'''
estacion = (input("Dime la estacion: "))
temperatura_media = float(input("Dime la temperatura: "))

print ("La temperatura media de " + estacion+ " ha sido de "+ str(temperatura_media)+ "ºC")

#Se utiliza %s para poder declarar despues la variable y hacer la llamada
print ("La temperatura media de %s ha sido de %sºC" %(estacion, temperatura_media))

#El .format hace la llamada a los {}
print ("La temperatura media de {0} ha sido de {1}ºC" .format(estacion, temperatura_media))

#La f hace como la llamada y en los {} se pone el nombre de las variables que les hemos asigando
print (f"La temperatura media de {estacion} ha sido de {temperatura_media}ºC")
'''
'''
CONDICIONAL IF
'''
"""
saldo = 500

if saldo < 1000:
    print("saldo insuficiente")
print("Fin de programa")

"""
"""
encender_aire, encender_ventilador, encender_calefaccion = False, False, False

temperatura = 30

if temperatura >15 and temperatura <=25:
    encender_calefaccion = True
    print("Calentando habitacion")
elif temperatura <=25:
    encender_ventilador = True
    print("Ventilando habitacion")
else:
    encender_aire = True
    print("Refirgerando habitacion")
"""

"""
BUCLES FOR
"""
"""
for i in range (0, 10, 1):
    print(i, "Hola")

range (10) ------> 0......9 n-1
range(3,10) -------> 3,4,5,6,7,8,9 n-1 (3-1)
range(3,10,2) --------> 3,5,7,9 n-1
"""

"""
Tabla de multiplicacion
"""
"""
numero = int(input("Introduce un numero: "))
contador = 0

for i in range (0,11) :
    print(numero *i *1)


for i in range (0,11):
    contador += numero
    print(contador)
"""

"""
Bucle WHILE
"""
'''
numero = 3

while numero < 15 :
    print("Hola")
    numero+=1
'''
"""
a = 1
while a < 5 :
    print("a")
    a+=1
"""

i = 10
while i>-1:
    print(i)
    i-=1

"""
for i in range (10,1,-1):
    print(f"La cuenta atras es...{i}")
"""
