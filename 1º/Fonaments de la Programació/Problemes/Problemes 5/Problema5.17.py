
def funcio(x,y):
    i = 1
    operacio = x
    text = ""
    
    while x**i < y:
        operacio = x**i
        text += str(operacio) + " "
        i+=1
        
    print(text)
        
num1 = int(input("Introdueix un valor: "))
num2 = int(input("Introdueix un valor: "))

if num1 <= 1 or num2 < num1:
     print("Error: Valors incorrectes")
     
else:
    resultat = funcio(num1,num2)
