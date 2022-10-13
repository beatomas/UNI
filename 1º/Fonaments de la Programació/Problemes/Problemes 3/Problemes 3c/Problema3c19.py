
num = int(input("Introdueix un número: "))

if ((2** (num - 1)) % num) == 1 or num == 2:
    print("PRIMER")
else:
    print("NO PRIMER")