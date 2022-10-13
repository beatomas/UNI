
suma = 0

limit = int(input("Introdueix un nombre: "))

while (limit <= 0):
    print("Error: el valor ha de ser més gran que zero")
    limit = int(input("Introdueix un nombre: "))
    
for num in range (1,limit+1,1): 
    suma = suma + num
    
print("El sumatori de",limit,"és:",suma)