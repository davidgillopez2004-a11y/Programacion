'''
Ejercicio 6
'''
'''
altura = int(input("¿Cuantos centimetros mides? : "))
peso = int (input("¿Cuanto pesas? : "))

print (0< altura , peso <0)
'''

'''
Ejercicio 7
'''
'''
nota = int(input("Ingresa un numero valido entre 0 y 10"))

print(0 <= nota <= 10)
'''

'''
Ejercicio 8
'''
'''
x = int(input("Ingresa un numero: "))
y = int(input("Ingresa un numero: "))
z = int(input("Ingresa un numero: "))

print (x + y + z == 100)
'''

'''
Ejercicio 9
'''
'''
hour = int(input("Ingresa una hora entre 0 y 23: "))

print (0 <= hour <= 23)
'''

'''
Ejercicio 10
'''
'''
minutes = int(input("Ingresa unos minuos entre 0 y 59: "))

print (0 <= minutes <= 59)
'''

'''
Ejercicio 11
'''

color_semaforo =  "Rojo"
color_semaforo1 =  "Ambar"
color_semaforo2 =  "Verde"


print (color_semaforo)
print (color_semaforo1)
print (color_semaforo2)


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Producto",
  "type": "object",
  "properties": {
    "id": { "type": "string", "pattern": "^PROD-[0-9]{3}$" },
    "disponible": { "type": "boolean" },
    "nombre": { "type": "string" },
    "precio": {
      "type": "object",
      "properties": {
        "valor": { "type": "number", "minimum": 0 },
        "moneda": { "type": "string", "minLength": 3, "maxLength": 3 }
      },
      "required": ["valor", "moneda"]
    }
  },
  "required": ["id", "disponible", "nombre", "precio"]
}
