

def OrdenadaDecreixent(llista):
    x = 1
    for i in range(len(llista)-1):
        if llista[i] > llista[i+1]:
            res = 1
        else: 
            x = 0
            res = 0
            return res
    if x == 1:
        return res
    
    
llista = []
valor = int(input("Introdueix el nombre de valors que vols a la llista: "))
for i in range(valor): 
    nombre = int(input("Introdueix un nombre enter: "))
    llista.append(nombre)
res = OrdenadaDecreixent(llista)
print(res)