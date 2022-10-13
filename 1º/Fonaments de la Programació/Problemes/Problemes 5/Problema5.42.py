

def OrdenarLlista(llista):
    llista.sort()
    
    
    
llista = []
for i in range(8):
    nombre = int(input("Introdueix un nombre enter: "))
    llista.append(nombre)
OrdenarLlista(llista)
print("Llista ordenada: ",llista)
    