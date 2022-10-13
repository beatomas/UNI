

def BuscarPosicio(llista,num):
    n = 1
    i = 0
    posicio = 0
    while n != 0 or i == (len(llista)-1):
        if llista[i] > num:
            i += 1
        else:
            n = 0
            posicio = i
    if n == 1:
        return -1
    else:
        return posicio
  
    
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
for x in range(5):
    num = int(input("Introdueix un enter: "))
    llista.append(num)

valor = OrdenadaDecreixent(llista)
if valor == 1:
    n = int(input("Introdueix un valor: "))
    posicio = BuscarPosicio(llista,n)
    if posicio == -1:
        print("Tots els valors de la llista són més grans que",n)
    else:
        print("El valor ha d'anar a la posició",posicio)

else:
    print("La llista no està correctament ordenada")



