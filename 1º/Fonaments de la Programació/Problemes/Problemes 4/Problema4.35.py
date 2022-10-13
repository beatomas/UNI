
llista = []
i = 0
while i < 10:
    valor = int(input("Introdueix un nombre enter: "))  
    llista.append(valor)
    i += 1
    
i = 0  

ordenada = True
while i < 9:
    if llista [i] > llista[i+1]:
        ordenada = False
        i = 11
    else:
        i += 1
    
if ordenada:
    print("La llista està ordenada.")
else:
    print("La llista no està ordenada.")