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

'''
Ejercicio 8
Diseña una función llamada palindrome que tenga una cadena de caracteres como parámetro de entrada y devuelva True si es un palíndromo o False en los demás casos. 
Una palabra es un palíndromo si se puede leer igual de izquierda a derecha que de derecha a izquierda, ignorando los espacios en blanco. 
Por ejemplo: "reconocer", "se es o no se es" o "Sé verlas al revés". Para simplificar el problema, puedes suponer que se utilizan caracteres simples, es decir, sin tildes ni diéresis.
'''
"""
def es_palindromo(cadena):
    cadena = cadena.lower()
    cadena_sin_espacios = ""

    for caracter in cadena:
        if caracter !=" ":
            cadena_sin_espacios+=caracter

    return cadena_sin_espacios == cadena_sin_espacios[::-1]

assert(es_palindromo("Radar")==True)
assert(es_palindromo("Rotor")==True)
assert(es_palindromo("Ojo")==True)
assert(es_palindromo("Oso")==True)
assert(es_palindromo("folio")==False)
"""
'''
Ejercicio 10
'''
"""
def es_armstrong(numero):
    numero_como_cadena=str(numero)
    longitud=len(numero_como_cadena)

    suma=0
    for digito in numero_como_cadena:

        suma+=int(digito)**longitud

    return(suma == int(numero))

assert(es_armstrong(153))
assert(es_armstrong(371))
"""
'''
Ejercicio 11
Escribe un programa para encontrar todos los números de Armstrong en el rango de 0 a 999.
'''
"""
def encontrar_Armstrong(numero):
    texto_numero = str(numero)
    longitud = len(texto_numero)
    
    suma = 0
    for digito in texto_numero:
        suma += int(digito) ** longitud
        
    return suma == numero

assert (encontrar_Armstrong(153)==True)
assert (encontrar_Armstrong(370)==True)
assert (encontrar_Armstrong(407)==True)
assert (encontrar_Armstrong(10)==False)
"""

'''
Ejercicio 15
'''
"""
def son_vocales(palabra):
    contador = 0
    encontrada = ""
    vocales = "aeiou"

    palabra = palabra.lower()

    for vocal in "aeiou":
        if vocal in palabra:
            contador+=1

    return contador
       
assert (son_vocales("Abaco")==2)
assert (son_vocales("Murcielago")==5)
assert (son_vocales("PROGRAMACION")==3)
"""

'''
Ejercicio 16
'''
"""
def son_diferentes(palabra):
    contador = 0
    encontrada = ""
    abecedario = "abcdefghijklmñopqrstuvwxyz"

    palabra = palabra.lower()
    for abecedario in "abcdefghijklmñopqrstuvwxyz":
        if abecedario in palabra:
            contador+=1

    return contador
       
assert (son_diferentes("Abaco")==4)
assert (son_diferentes("Murcielago")==10)
assert (son_diferentes("PROGRAMACION")==9)
"""

'''
Ejercicio 17
'''

def son_ordenadas(palabra):
    vocal = "aeiou"
    consonantes = "bcdfghjklmnñpqrstvwxyz"

    vocales = "" 
    consonantes_min = ""

    palabra = palabra.lower()

    for caracter in palabra:
        if caracter in vocal:
            vocales+=caracter
        elif caracter in consonantes:
            consonantes_min+=caracter
    resultado = consonantes_min + vocales 
    return resultado

assert(son_ordenadas("curso de programacion")=="crsdprgrmcnuoeoaaio")
assert(son_ordenadas("Hola Mundo 123!") == "HlMndoaUo")
