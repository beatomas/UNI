
anys = int(input("Introdueix un any: "))

if (((anys % 4 == 0 ) and (anys % 100 != 0)) or (anys % 400 == 0)):
    print("A l'any",anys,"febrer té 29 dies")
else:
     print("A l'any",anys,"febrer té 28 dies")
    