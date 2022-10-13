
nameHandle = open("Fitxer.txt","r")
nameHandle.seek(19)
print(nameHandle.read(6))
print(nameHandle.tell())
nameHandle.close()


