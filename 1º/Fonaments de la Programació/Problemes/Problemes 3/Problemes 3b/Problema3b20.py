
num1 = int(input("Introdueix un nombre: "))
num2 = int(input("Introdueix un nombre: "))
num3 = int(input("Introdueix un nombre: "))

if ((num1 + num2 == num3) or (num1 + num3 == num2) or (num2 + num2 == num1)):
    print("IGUALS")
else:
    print("DIFERENTS")