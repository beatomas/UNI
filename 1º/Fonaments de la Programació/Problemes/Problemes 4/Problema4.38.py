

llista1 = []


for valor in range (1,7):
    valor = int(input("Introdueix un valor a la llista 1: "))
    llista1.append(valor)

llista2 = []

for valor in range (1,len(llista1) + 1):
    valor = int(input("Introdueix un valor a la llista 2: "))
    llista2.append(valor)
  
    
i = 0
diferents = False
while i < len(llista1):
    if llista1[i] == llista2[i]:
        i += 1
    else: 
        diferents = True
        break
    
if(diferents): 
    print("DIFERENTS")
else:   
    print("IGUALS")