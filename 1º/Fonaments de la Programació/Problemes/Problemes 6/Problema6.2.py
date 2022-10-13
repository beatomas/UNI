

nameHandle = open("Fitxer.txt","w")
nameHandle.write("Hola\nBenvinguts al curs\n")
nameHandle.write("Introducció al Python\n")
nameHandle.close()

nameHandle = open("Fitxer.txt","a")
nameHandle.write("Espero que us agradi\n")
nameHandle.close()

nameHandle = open("Fitxer.txt","r")
print(nameHandle.read())
nameHandle.close()



