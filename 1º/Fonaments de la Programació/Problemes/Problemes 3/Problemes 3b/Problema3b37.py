
print("")
print("   MENÚ")
print("1.-Suma")
print("2.-Resta")
print("3.-Producte")
print("4.-Divisió")
print("5.-Sortir")
opcio = int(input("Selecciona una de les opcions: "))

if (opcio == 1):
    op1 = float(input("Introdueix un operand: "))
    op2 = float(input("Introdueix un segon operand: "))
    resultat = op1 + op2
    print(op1,"+",op2,"=",resultat)
    
elif (opcio == 2):
    op1 = float(input("Introdueix un operand: "))
    op2 = float(input("Introdueix un segon operand: "))
    resultat = op1 - op2
    print(op1,"-",op2,"=",resultat)
    
elif (opcio == 3):
    op1 = float(input("Introdueix un operand: "))
    op2 = float(input("Introdueix un segon operand: "))
    resultat = op1 * op2
    print(op1,"*",op2,"=",resultat)
    
elif (opcio == 4):
    op1 = float(input("Introdueix un operand: "))
    op2 = float(input("Introdueix un segon operand: "))
    if op2 == 0:
        print("Error: Divisió per zero")
    else:
        resultat = op1/op2
        print(op1,":",op2,"=",resultat)
        
elif (opcio == 5):
    print("Sortint de la calculadora...")

else:
    print("Error. Opció no vàlida")
    
