

llista = input("Introdueix una frase: ")


i = 0
X1 = 0
while i < len(llista):
    if (llista[i] == "a" or llista[i] == "A"):
        X1 += 1
        i += 1
    else: 
        i += 1
        
        
i = 0  
X2 = 0  
while i < len(llista):
    if (llista[i] == "e" or llista[i] == "E"):
        X2 += 1
        i += 1
    else: 
        i += 1
        
i = 0  
X3 = 0  
while i < len(llista):
    if (llista[i] == "i" or llista[i] == "I"):
        X3 += 1
        i += 1
    else: 
        i += 1
        
i = 0  
X4 = 0  
while i < len(llista):
    if (llista[i] == "o" or llista[i] == "O"):
        X4 += 1
        i += 1
    else: 
        i += 1
        
i = 0  
X5 = 0  
while i < len(llista):
    if (llista[i] == "u" or llista[i] == "U"):
        X5 += 1
        i += 1
    else: 
        i += 1
        
print("A:",X1,"- E:",X2,"- I:",X3,"- O:",X4,"- U:",X5)
        