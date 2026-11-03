#Palabra a la inversa

palabra = input("Introduce una palabra:")

def cadenainversa (inversa):
    return inversa[::-1]
resultado = cadenainversa(palabra)
print(resultado)

#Primer ejemplo
cadena = "Llamaron a Paco para cobrar"

print("1. Imprimimos la última letra de dos formas diferentes", cadena[-1], cadena[len(cadena)-1])

#Segundo ejemplo
cadena = "Llamaron a Paco que no hay comida"

print("2. Imprimimos la primera letra de dos formas diferentes", cadena[0], cadena[-len(cadena)])

#Tercer ejemplo
cadena = "A Paco le gusta comer Chocolate"

print("3. Imprimimos un rango: ", cadena[2: 20])

#Cuarto ejemplo
cadena = "Joselito se parece a un pez gota"

print("4. Imprimimos desde la quinta posición hasta el final: ", cadena[4:])

#Quinto ejemplo
cadena = "Ivan esta estresado"

print("5. Imprimimos desde la antepenúltima posición hasta el final: ", cadena[-3:])

#Sexto ejemplo
cadena = "Abel le ha tocado el ticket de la tienda pirata"

print("6. Imprimimos hasta la antepenúltima posición: ", cadena[:-2])

#Septimo ejemplo
cadena = "Alejandro juega al fortnite"

print("7. Lo imprimimos todo: ", cadena[:])

#Acesso indexado
palabra = "Cadena de ejemplo"

for i in range(len(palabra)):
    print(palabra[i])

print("-"*7)

# Acceso elemento a elemento
for i in palabra:
    print(i)

#Comprobacion si hay algun caracter
print('a' in "Buenos dias")
print('a' not in "Buenas noches")