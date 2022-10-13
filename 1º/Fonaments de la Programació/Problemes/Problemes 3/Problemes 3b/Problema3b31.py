

euros = float(input("Introdueix una quantitat expressada en euros: "))

print("")
print("1-Dòlars(USD)")
print("2-Lliures(GBP)")
print("3-Francs suïssos(CHF)")
print("4-Yens(JPY)")
print("")

opcio = int(input("Prem una tecla per seleccionar l'opció: "))

if (opcio == 1):
    dolars = euros*1.34
    print(euros,"euros són",dolars,"USD")
    
elif(opcio == 2):
    lliures = euros*0.83
    print(euros,"euros són",lliures,"GBP")
    
elif(opcio == 3):
    francs = euros*1.23
    print(euros,"euros són",francs,"CHF")
    
elif(opcio == 4):
    yens = euros*133.11
    print(euros,"euros són",yens,"JPY")
    
else:
    print("Error: moneda no disponible")


