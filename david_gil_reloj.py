hora = int(input("Introduce la hora: (0/23) "))
minutos = int(input("Introduce los minutos: (0/59) "))
segundos = int(input("Introduce los segundos: (0/59) "))

while 0 > hora or hora >23 or 0 > minutos or minutos > 59 or 0 > segundos or segundos >59 :
    print("LA HORA ESTA MAL!!!")

    hora = int(input("Introduce la hora: (0/23) "))
    minutos = int(input("Introduce los minutos: (0/59) "))
    segundos = int(input("Introduce los segundos: (0/59) "))

segundos+=1

if segundos == 60:
    segundos = 0
    minutos+=1

if minutos == 60:
    minutos = 0
    hora+=1

if hora == 24:
    hora = 0

print(f"La hora valida es {hora} : {minutos} : {segundos}")