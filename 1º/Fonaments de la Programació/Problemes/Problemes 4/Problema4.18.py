
files = int(input("Introdueix el número de files: "))
columnes = int(input("Introdueix el número de columnes: "))

matriu = []
tupla = []


for i in range(files):
    for index in range(columnes):
        tupla.append(int(input("Introdueix un valor: ")))
    tmp = tupla[:]
    tupla.clear()
    matriu.append(tmp)
    
print(matriu)