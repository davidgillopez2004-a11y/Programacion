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

saldo = 500

if saldo < 1000:
    print("saldo insuficiente")
print("Fin de programa")