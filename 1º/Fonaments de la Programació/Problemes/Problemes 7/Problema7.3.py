
def OperStrings(cadena,operador):
        if (operador == "&"):
            try:
                res = float(cadena)
            except:
                raise ValueError("La cadena no conté un número")
        elif (operador == "#"):
            try:
                index = int(input("Index del caràcter a extreure: "))
            except:
                raise ValueError("Valor no enter en l'índex")
            else:
                res = cadena[index]
        elif (operador == "*"):
            try:
                rep = int(input("Nombre de repeticions: "))
            except: 
                raise ValueError("Valor no enter en el nombre de repeticions")
            else:
                res = cadena*rep
        else: 
            raise SyntaxError("Operació no definida")
        return res
            
#programa principal
try: 
    cadena = input("Introdueix una cadena: ")
    operador = input("Introdueix un operador: ")
    res = OperStrings(cadena,operador)
except SyntaxError as missatge:
    print("ERROR:",missatge)
except ValueError as missatge: 
    print("ERROR:",missatge)
except IndexError:
    print("ERROR: Intent d'accés a fora de la cadena")
else:
    print("Resultat de l'operació:",res)
    
        