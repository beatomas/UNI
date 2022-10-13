

num = int(input("Introdueix un nombre: "))

if (num < 0):
     print("No hi ha nombres a la seqüència.")

suma = 1
maxim = num
minim = num

     
while (num > 0) and (suma < 10):
    num = int(input("Introdueix un nombre: "))
    suma = suma + 1
    if num < 0:
        print("Màxim:",maxim,"- Mínim:",minim)
    else:
        if (num > maxim):
            maxim = num
        if (num < minim):
            minim = num
        print("Màxim:",maxim,"- Mínim:",minim)
    

