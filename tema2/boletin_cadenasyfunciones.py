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

def es_camelcase(camelcase):
    resultado=""
    for i in range(len(camelcase)):
        if camelcase[i] != " ":
            resultado+=camelcase[i].upper(camelcase:)
    return resultado


assert(es_camelcase("hola mundo cruel")=="holaMundoCruel")
assert(es_camelcase("hola mundo cruel")!="HolaMundoCruel")
assert(es_camelcase("hola mundo cruel")!="holamundoCruel")
