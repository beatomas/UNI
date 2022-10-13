

npos = 0
nneg = 0
x = 0

for x in range (0,5,1):
    num = float(input("Introdueix un nombre: "))
    x += 1
    
    if (num > 0):
        npos += 1
        
    if (num < 0):
        nneg += 1

print("")    
print("Positius:",npos,"- Negatius:",nneg)