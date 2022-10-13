
llista = []

num = int(input("Introdueix un valor: "))

while (num != 0):
    llista.append(num)
    num = int(input("Introdueix un valor: "))
    
i = 0
trobat = False

while ((i<len(llista)) and (not trobat)):
    if (llista[i]%2 == 0):
        trobat = True
    else:
        i += 1
    
if (trobat):
    print("Hi ha nombre parell")
else:
    print("No hi ha nombre parell")
   