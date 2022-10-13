
def area_quadrat(costat):
     if costat>0:
          area=costat*costat
          return 0,area
     else:
          return 1,None


def area_rectangle(base,altura):
     if (base>0)and(altura>0):
          area=base*altura
          return 0,area
     else:
          return 1,None


def area_triangle(base,altura):
     if (base>0)and(altura>0):
          area=base*altura/2
          return 0,area
     else:
          return 1,None
      
def menu_seleccio():
    print("----- MENÚ -----\n")
    print("1.-Àrea quadrat")
    print("2.-Àrea rectangle")
    print("3.-Àrea triangle")
    print("4.-Sortir\n")
    print("Tria una de les opcions: ")
      
menu_seleccio()
opcio = int(input(""))
while opcio != 4:
    if opcio == 1:
        costat = float(input("Introdueix la mida del costat: "))
        cor,area = area_quadrat(costat)
        if cor == 1:
            print("Error: Dimensions incorrectes")
        else: 
            print("Àrea:",area)
        menu_seleccio()
        opcio = int(input(""))
    if opcio == 2:
        base = float(input("Introdueix la mida de la base: "))
        altura = float(input("Introdueix la mida de l'altura: "))
        cor,area = area_rectangle(base,altura)
        if cor == 1:
            print("Error: Dimensions incorrectes")
        else: 
            print("Àrea:",area)
        menu_seleccio()
        opcio = int(input(""))
    if opcio == 3:
        base = float(input("Introdueix la mida de la base: "))
        altura = float(input("Introdueix la mida de l'altura: "))
        cor,area = area_triangle(base,altura)
        if cor == 1:
            print("Error: Dimensions incorrectes")
        else: 
            print("Àrea:",area)
        menu_seleccio()
        opcio = int(input(""))
    if opcio == 4:
        break 
    if opcio != 1 and opcio != 2 and opcio != 3 and opcio != 4:   
        print("Error: Opció incorrecta")
        menu_seleccio()
        opcio = int(input(""))
        
    
    
    
    
    