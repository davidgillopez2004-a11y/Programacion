"""
Realizar una función que reciba como parámetro una cadena que contenga un dni y devuelva un True si el dni es válido y False en caso contrario. 
Para calcular la letra debemos tomar el número completo de hasta 8 cifras de nuestro DNI, 
lo dividimos entre 23 y nos quedamos con el resto de dicha división. El resultado anterior es un número entre 0 y 22.
A cada uno de estos posibles números le corresponde una letra, según la siguiente tabla:

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
T R W A G M Y F P D X B N J Z S Q V H L C K E
"""

def validacion_dni(dni):

    if len(dni) != 9:
        return False

    numero = dni[:8]
    letra = dni[8].upper()

    for caracter in numero:
        if caracter < "0" or caracter > "9":
            return False

    letras = "TRWAGMYFPDXBNJZSQVHLCKE"

    resto = int(numero) % 23

    if letras[resto] == letra:
        return True
    else:
        return False

assert validacion_dni("12345678Z") == True
assert validacion_dni("12345678A") == False
assert validacion_dni("1234567") == False
assert validacion_dni("ABCDEFGHM") == False

dni = input("Introduce tu DNI: ")

print(validacion_dni(dni))



