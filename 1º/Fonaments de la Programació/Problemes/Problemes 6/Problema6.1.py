
nameHandle = open("Fitxer.txt","w")
nameHandle.write("Hola\nBenvinguts al curs\n")
nameHandle.write("Espero que us agradi\n")
nameHandle.close()

nameHandle = open("Fitxer.txt","r")
print(nameHandle.read())
nameHandle.close()

nameHandle = open("Fitxer.txt","r")
i = 1
for linia in nameHandle:
    print(i,linia)
    i += 1
nameHandle.close()


nameHandle = open("Fitxer.txt","r")
for linia in range(3):
    print(nameHandle.readline()[:-1])
nameHandle.close()


