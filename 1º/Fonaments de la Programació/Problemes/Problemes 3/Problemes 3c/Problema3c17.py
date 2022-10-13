
op1 = float (input ("Selecciona un primer operand: "))
op2 = float (input ("Selecciona un segon operand: "))

print ("MENÚ \n1.- Suma \n2.- Resta \n3.- Producte \n4.- Divisió \n5.- Sortir")
opcio = int (input ("Selecciona una de les operacions: "))

while (opcio != 5):
        
    if (opcio == 1):
        resultat = op1 + op2
        print (op1, "+" ,op2, "=" ,resultat)
        
    elif (opcio == 2):
        resultat = op1 - op2
        print (op1, "-" ,op2, "=" ,resultat)
        
    elif (opcio == 3):
        resultat = op1 * op2
        print (op1, "*" ,op2, "=" ,resultat)
        
    elif (opcio == 4):
        if (op2 == 0):
            print ("Error: Divisió per zero")
            
        else:
            resultat = op1/op2
            print (op1, ":" ,op2, "=" ,resultat)
        
    elif (str(opcio) not in "12345"):
        print ("Error: Opció no vàlida")
    
    print ("MENÚ \n1.- Suma \n2.- Resta \n3.- Producte \n4.- Divisió \n5.- Sortir")
    opcio = int (input ("Selecciona una de les operacions: "))
    
    
    if (opcio == 5):
        pregunta = input ("Vols operar amb uns altres operands? (S/-)")
        if (pregunta == "S" or pregunta =='s'):
            op1 = float (input ("Selecciona un primer operand: "))
            op2 = float (input ("Selecciona un segon operand: "))            
            print ("MENÚ \n1.- Suma \n2.- Resta \n3.- Producte \n4.- Divisió \n5.- Sortir")
            opcio = int (input ("Selecciona una de les operacions: "))