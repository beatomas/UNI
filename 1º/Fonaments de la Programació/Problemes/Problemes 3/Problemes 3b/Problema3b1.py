

número = int(input("Introdueix un nombre: "))

missatge = "El nombre " +str(número)

if ((número < 0) or (número > 10)):
    missatge = missatge + " NO"

missatge = missatge + " està en l'interval."

print(missatge)