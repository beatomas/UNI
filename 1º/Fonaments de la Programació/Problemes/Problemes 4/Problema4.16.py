
llista = []
for i in range (1,11):
    valor = int(input("Introdueix un valor: "))
    llista.append(valor)

pos_correcta = False
while (pos_correcta == False):
    posicio = int(input("Introdueix una posició de la llista: "))
    if(posicio < 0 or posicio > 9):
        print("Error: Posició no vàlida")
    else: pos_correcta = True
    
llista1 = llista[0:(posicio)]
llista2 = llista[posicio:len(llista)]
    
llista = llista2 + llista1

print(llista)
