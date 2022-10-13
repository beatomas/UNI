

lletra = input("Introdueix un caràcter: ")

if (lletra >= "A" and lletra <= "Z"):
    if (lletra in "AEIOU"):
        print("Vocal en majúscula")
    else:
        print("Consonant en majúscula")
elif (lletra >= "a" and lletra <= "z"):
    if (lletra in "aeiou"):
        print("Vocal en minúscula")
    else:
        print("Consonant en minúscula")
else:
    print("Caràcter no permès")
    