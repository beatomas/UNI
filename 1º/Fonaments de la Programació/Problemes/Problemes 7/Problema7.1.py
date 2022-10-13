
try:
    operand1 = float(input("Primer operand: "))
    operador = input("Operació: ")
    operand2 = float(input("Segon operand: "))
    
    if (operador == "+"):
        resultat = operand1 + operand2
    elif (operador == "-"):
        resultat = operand1 - operand2
    elif (operador == "*"):
        resultat = operand1 * operand2
    elif (operador == ":"):
        resultat = operand1 / operand2
    else:
        raise SyntaxError ("Operació no definida")
   
except ZeroDivisionError:
    print("ERROR: Divisió per zero")
except ValueError:
    print("ERROR: Operands han de ser nombres")
except SyntaxError as missatge:
    print("ERROR:",missatge)
else: 
    print(operand1,operador,operand2," = ", resultat)