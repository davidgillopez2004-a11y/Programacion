"""
Duración orientativa: 2 horas. Reglas: sin ayuda, solo input, print, int, while, for,
if y range. Sin listas ni funciones.
"""

"""
Pide al usuario notas de un alumno entre 0 y 10. Si introduce una nota fuera de rango,
vuelve a pedirla hasta que sea válida. El programa termina cuando el usuario escribe -1. Al
terminar, muestra:
● cuántas notas válidas se introdujeron, la media,
● cuántas fueron aprobados (≥ 5) y cuántas suspensos.
Si no se introdujo ninguna nota, el programa debe indicarlo en lugar de calcular la media.
"""

notas = float(input("Introduce la nota que tienes: "))
aprobados = 0
suspensos = 0
resultado = 0
cantidad_aprobados = 0

#and si hay uno falso todos son falsos
#or si hay uno verdadero todos son verdaderos
#<>

while notas <0 or notas >10 :
    notas = float(input("Introduce la nota que tienes: "))

while notas!=-1:
    
    if notas >=0 or notas<=10 :
        resultado = notas+resultado
        cantidad_aprobados+=1

        if notas >=5:
            aprobados+=1
        else:
            suspensos+=1
    else:
        print("La nota debe estar entre 0 y 10")
    notas = float(input("Introduce la nota que tienes: "))
    
resultado = aprobados/notas
print(f"Las notas validas fueron {cantidad_aprobados}")
print(f"La media es {resultado}")
print(f"Han aprobado {aprobados}")
print(f"Han suspendido {suspensos}")
