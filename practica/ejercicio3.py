"""
Dos jugadores juegan al mejor de 5 rondas. En cada ronda, cada jugador introduce el valor
de su dado (1 a 6), validando que sea correcto.
● Gana la ronda el valor más alto. Si hay empate, la ronda no puntúa, pero sí cuenta
como ronda jugada.
● Si un jugador consigue 3 victorias antes de terminar las 5 rondas, la partida acaba
en ese momento.
● Al final, muestra quién ganó, con qué marcador y cuántas rondas se jugaron.
"""

#<>
#Dos jugadores
#Gana al mejor de 5 rondas
#Dado 1 a 6

jugador_1 = int(input("Introduce un numero valido del dado (1 al 6)"))
jugador_2 = int(input("Introduce un numero valido del dado (1 al 6)"))
rondas = 5

