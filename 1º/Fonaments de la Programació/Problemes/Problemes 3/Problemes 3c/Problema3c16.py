
nota = float(input("Introdueix una nota: "))

suspes = 0
aprovat = 0
notable = 0
excel·lent = 0
matricula = 0


while (nota >= 0 and nota <= 10):
    if (nota < 5):
        suspes += 1
        nota = float(input("Introdueix una nota: "))
    if (nota >= 5 and nota < 7):
        aprovat += 1
        nota = float(input("Introdueix una nota: "))
    if (nota >= 7 and nota < 9):
        notable += 1
        nota = float(input("Introdueix una nota: "))
    if (nota >= 9 and nota < 10):
        excel·lent += 1
        nota = float(input("Introdueix una nota: "))
    if (nota == 10):
        matricula += 1
        nota = float(input("Introdueix una nota: "))
        
print ("S:",suspes,"- A:",aprovat,"- N:",notable,"- E:",excel·lent,"- MH:",matricula)