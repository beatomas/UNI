
s = input("Introdueix una cadena: ")

vocal = 0

for element in s:
    if (element in "aeiouAEIOU"):
        vocal += 1
        
print("El string",s,"té",vocal,"vocals")