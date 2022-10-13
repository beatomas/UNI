
print("")
print("   MENÚ")
print("1.-Suma")
print("2.-Resta")
print("3.-Producte")
print("4.-Divisió")
print("5.-Sortir")
opcio = int(input("Selecciona una de les opcions: "))


if ((opcio!= 1) and (opcio!= 2) and (opcio!= 3) and (opcio!= 4) and (opcio!= 5)):
    print("Error. Opció no vàlida")
    
    
else:
    op1 = float(input("Introdueix un operand: "))
    op2 = float(input("Introdueix un segon operand: "))
    
    if (opcio == 1):
        resultat = op1 + op2
        print(op1,"+",op2,"=",resultat)
    
    elif (opcio == 2):
        resultat = op1 - op2
        print(op1,"-",op2,"=",resultat)
    
    elif (opcio == 3):
        resultat = op1 * op2
        print(op1,"*",op2,"=",resultat)
    
    elif (opcio == 4):
        if op2 == 0:
            print("Error: Divisió per zero")
        else:
            resultat = op1/op2
            print(op1,":",op2,"=",resultat)
        
    else:
        print("Sortint de la calculadora...")

