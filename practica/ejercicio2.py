"""
Ejercicio 2: Cine con descuentos (2,5 puntos)
Un cine tiene 80 entradas disponibles por sesión.
● Precio: 6 € de lunes a miércoles (L, M, X) y 9 € de jueves a domingo (J, V, S, D).
● Descuento del 20 % si compras exactamente 4 entradas, salvo los domingos.
● Descuento del 40 % si compras más de 8 entradas, todos los días.
● Los dos descuentos no se acumulan.
El programa pide repetidamente el día y el número de entradas. Debe:
● validar el día,
● validar que el número de entradas sea mayor que 0 y no supere las disponibles,
● mostrar el importe de cada compra y las entradas que quedan.
Termina cuando el día es FIN o se agotan las entradas. Al final, muestra la recaudación
total.
"""

#80 entradas
#L/M/X 6€
#J/V/S/D 9€
#20% COMPRAS 4 ENTRADAS menos los domingos
#40% +8 entradas todos los dias
#Validar dia
#entradas mayor que 0 y como maximo 80 entradas
#mostrar el importe de cada compra 


#<>

dia_semana = input("Dime el dia de la semana (L/M/X/J/V/S/D)")
entradas = int(input("Introduce la cantidad de entradas: "))
precio = 0
resultado = 0

while dia_semana=="L" or dia_semana=="M" or dia_semana=="X" or dia_semana=="J" or dia_semana=="V" or dia_semana=="S" or dia_semana=="D" :

    if dia_semana=="L" or dia_semana=="M" or dia_semana=="X":
        if entradas ==4:
            precio=6
            resultado = precio*entradas*0.20
            total = (precio*entradas) -resultado
            print(f"Ha obtenido una rebaja de {total}")
    else:
        precio = 9
        resultado = precio*entradas*0.20
        total = (precio*entradas) -resultado
        print(f"Ha obtenido una rebaja de {total}")

    if dia_semana == "D":
        precio=6
        resultado = precio*entradas
        print(f"Ha obtenido una rebaja de {total}")

           

    dia_semana = input("Dime el dia de la semana (L/M/X/J/V/S/D)")