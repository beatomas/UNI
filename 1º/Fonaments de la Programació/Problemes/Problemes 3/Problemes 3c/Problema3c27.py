
print("Introdueix dos valors: ")
n1 = int(input())
n2 = int(input())

if ((n1)%2 != 0):
    n1 = n1 + 1 


suma = 0
producte = 1
mitjana = 0
comp = 0

for x in range (n1,n2+1,2):
    suma += x
    producte *= x
    comp += 1
    
mitjana = suma/comp

    
print("Suma:",suma," - Producte:",producte,"- Mitjana:",mitjana)
    