

tupla = ("dilluns", "dimarts", "dimecres", "dijous", "divendres", "dissabte", "diumenge")


nombre = -1
while (nombre != 0):
   nombre = int(input("Introdueix un nombre enter: "))
   if (1<=nombre and nombre <=7):
       print(tupla[nombre-1])
   else:
        print("Error: Dia incorrecte")
        
