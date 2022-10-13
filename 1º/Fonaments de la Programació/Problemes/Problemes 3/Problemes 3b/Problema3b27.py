

num1 = int(input("Introdueix un nombre enter: "))
num2 = int(input("Introdueix un nombre enter: "))
num3 = int(input("Introdueix un nombre enter: "))
num4 = int(input("Introdueix un nombre enter: "))

num_comp = 0

if (num1 > num2):
    num_comp = num_comp + 1 
    if (num1 > num3):
        num_comp = num_comp + 1 
        if(num1 > num4):
            num_comp = num_comp + 1 
            print("El número més gran de la sèrie és " + str(num1) + ". Comparacions:", num_comp)
        else: 
            num_comp = num_comp + 1
            print("El número més gran de la sèrie és " + str(num4) + ". Comparacions:", num_comp)
    else:
        num_comp = num_comp + 1
        if(num3 > num4):
            num_comp = num_comp + 1 
            print("El número més gran de la sèrie és " + str(num3) + ". Comparacions:", num_comp)
        else:
            num_comp = num_comp + 1 
            print("El número més gran de la sèrie és " + str(num4) + ". Comparacions:", num_comp)
else:
    num_comp = num_comp + 1 
    if(num2 > num3):
        num_comp = num_comp + 1 
        if(num2 > num4):
            num_comp = num_comp + 1 
            print("El número més gran de la sèrie és " + str(num2) + ". Comparacions:", num_comp)
        else:
            num_comp = num_comp + 1 
            print("El número més gran de la sèrie és " + str(num4) + ". Comparacions:", num_comp)
    else:
        num_comp = num_comp + 1 
        if(num3 > num4):
            num_comp = num_comp + 1 
            print("El número més gran de la sèrie és " + str(num3) + ". Comparacions:", num_comp)
        else:
            num_comp = num_comp + 1 
            print("El número més gran de la sèrie és " + str(num4) + ". Comparacions:", num_comp)
