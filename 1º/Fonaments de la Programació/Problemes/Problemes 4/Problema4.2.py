
tupla = ("Gener", "Febrer", "Març", "Abril", "Maig", "Juny", "Juliol", "Agost", "Setembre", "Octubre", "Novembre", "Desembre")

data = input("Introdueix una data en format DD/MM/AAAA: ")

dia = int (data [0:2])
anys = int (data [6:10])
mes = int (data [3:5])

if (mes > 12 or mes < 1):
    print ("Error: Mes incorrecte")

else:    
    mes = mes -1
    print (str (dia) + " de " + str(tupla [mes]) + " de " + str (anys))

