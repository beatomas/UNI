
def is_anagram(s1,s2):
    cadena1 = sorted(s1)
    cadena2 = sorted(s2)
    if (cadena1 == cadena2):
        anagrama = True
    else:
        anagrama = False
    return anagrama

cadena_1 = input("Introdueix la primera cadena: ")
cadena_2 = input("Introdueix la segona cadena: ")

resultat = is_anagram(cadena_1,cadena_2)

if resultat:
    print("És un anagrama")
else:
    print("No és un anagrama")
    
    