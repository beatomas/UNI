
llista = []
elements = int(input("Introdueix el nombre d'elements: " ))

i = 0
while i < elements:
    valor = int(input("Introdueix un valor: "))
    i += 1
    llista.append(valor)

opcio = -1

while opcio != 6:

    print("1-Afegir element al final la llista")
    print("2-Afegir element en una posició de la llista")
    print("3-Eliminar el darrer element de la llista")
    print("4-Eliminar l'element d'una posició de la llista")
    print("5-Eliminar la primera aparició d'un valor a la llista")
    print("6-Sortir")

    opcio = int(input("Escull una opció: "))
    
    if  0 >= opcio > 6:
        print("Error: Opció no disponible")
    
    if opcio == 1:
        valor1 = int(input("Introdueix un valor a afegir: "))
        llista.append(valor1)
    if opcio == 2:
        valor2 = int(input("Introdueix un valor a afegir: "))
        posicio = int(input("Escull la posició: "))
        if posicio > len(llista):
            print("Error: Posició no vàlida")
        else:
            llista.insert(posicio,valor2)
    if opcio == 3:
        llista.pop()
    if opcio == 4:
        posicio = int(input("Escull la posició: "))
        if posicio > len(llista):
            print("Error: Posició no vàlida")
        else:
            llista.pop(posicio)
    if opcio == 5:
        valor3 = int(input("Introdueix el valor a eliminar: "))
        if valor3 in llista:
            j = 0
            while j < len(llista):
                if llista[j]==valor3:
                    llista.pop(j)
                    j = len(llista)
                else:
                    j+=1
                   
        else:
            print("Error: Valor inexistent a la llista")
    print(llista)
        
        
        
        
        
        
        
        