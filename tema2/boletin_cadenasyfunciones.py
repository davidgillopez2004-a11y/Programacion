'''
Ejercicio 1
'''
"""
def es_acronimo(acronimo):
    resultado = ""
    for i in range(len(acronimo)): # Lo recorre
        if acronimo[i].isupper(): # Validar que haya alguna mayuscula
            resultado+=acronimo[i]

    return resultado

assert(es_acronimo("Instituto Nacional de Tecnologia Industrial")=="INTI")
assert(es_acronimo("Instituto Nacional de Tecnologia Industrial")!="INTIS")
assert(es_acronimo("Instituto Nacional de Tecnologia Industrial")!="inti")
"""

'''
Ejercicio 2
'''
"""
def es_camelcase(camelcase):
    resultado=""
    for i in range(len(camelcase)):
        if camelcase[i] != " ":
            if camelcase[i - 1] == " ":
                resultado+=camelcase[i].upper()
            else:
                resultado+=camelcase[i].lower()
    return resultado

assert(es_camelcase("hola mundo cruel")=="holaMundoCruel")
assert(es_camelcase("hola mundo cruel")!="HolaMundoCruel")
assert(es_camelcase("hola mundo cruel")!="holamundoCruel")
"""

'''
Ejercicio 4
'''
"""
#no me sale
def es_rotacion(palabra,n):
    resultado = palabra
    for i in range(len(n)):
        resultado+= palabra[::-1]
    return resultado
assert(es_rotacion("python")=="onpyth")
assert(es_rotacion("java")=="avaj")
assert(es_rotacion("ola")!="alo")
"""

'''
Ejercicio 5

Diseña una función llamada charactersInString que tenga una cadena de caracteres y 
un carácter como parámetros de entrada y devuelva cuántas veces aparece ese carácter en la cadena 
(sin distinguir entre mayúsculas y minúsculas)
'''
"""
def es_charactersInString(cadena,caracter):
    contador = 0

    cadena=cadena.lower()
    caracter=caracter.lower()

    for i in cadena:
        if i == caracter:
            contador+=1
    return contador

assert (es_charactersInString("Moto","o")==2)
assert (es_charactersInString("Banana", "b")==1)
assert (es_charactersInString("Valorant", "c")==4)
"""
'''
Ejercicio 6

Diseña una función llamada lowCaseInString que tenga una cadena de caracteres 
como parámetro, devolviendo cuántos de esos caracteres son letras minúsculas.
'''
"""
def lowCaseInString(cadena):
    contador = 0

    for i in cadena:
        if i.islower():
            contador+=1
    return contador

assert (lowCaseInString("HolaMundo")==7)
assert (lowCaseInString("Caracol")==6)
assert (lowCaseInString("PIZZA")==5)
"""
'''
Ejercicio 7

Diseña una función llamada numberInString que reciba una cadena de caracteres 
como parámetro y devuelva cuántos de ellos son números
'''
"""
def numberInString(cadena):
    contador = 0

    for i in cadena:
        if i.isdigit():
            contador+=1
    return contador

assert (numberInString("63426")==5)
assert (numberInString("1111")==4)
assert (numberInString("ab325op")==3)
assert (numberInString("abce")==6)
"""

"""
Ejercicio 15
"""

def son_vocales(palabra,letra,vocal):
    contador = 0
    encontrada = ""
    vocales = "aeiou"

    palabra = palabra.lower()

    for i in vocales:
        if letra == vocal:
            encontrada = vocal

    if encontrada != "":
        contador +=1
    return contador
       
assert (son_vocales("Abaco")==2)
