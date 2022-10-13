
data = input("Introdueix la data en format DD/MM/AAAA: ")


DD = int(data[0:2])
MM = int(data[3:5])
AAAA = int(data[6:10])

if MM in (1,3,5,7,8,10,12):
    num_dies = 31
    if (DD > num_dies or DD <= 0):
        print ("Error. Dia incorrecte")
    else:
        print("Data correcta")
   
elif (MM == 2):
    if (((AAAA % 4 == 0 ) and (AAAA % 100 != 0)) or (AAAA % 400 == 0)):
        num_dies = 29
        if (DD > num_dies or DD <= 0):
            print ("Error. Dia incorrecte")
        else:
            print("Data correcta")
    else:
        num_dies = 28
        if (DD > num_dies or DD <= 0):
            print ("Error. Dia incorrecte")
        else:
            print("Data correcta")

elif MM in (4, 6, 9, 11):
    num_dies = 30
    if (DD > num_dies or DD <= 0):
        print ("Error. DIa incorrecte")
    else:
        print("Data correcta")

else:
    print("Error. Mes incorrecte")
    
    
