
vocal = input("Introdueix una vocal: ")

if (vocal not in "aeiouAEIOU"):
    print("Error: El caràcter introduït no és una vocal")
    
if (vocal == "a" or vocal == "A"):
    print("Vocal:",vocal,"- Codi Morse: .-")
    
if (vocal == "e" or vocal == "E"):
     print("Vocal:",vocal,"- Codi Morse: .")
     
if (vocal == "i" or vocal == "I"):
     print("Vocal:",vocal,"- Codi Morse: ..")
     
if (vocal == "o" or vocal == "O"):
     print("Vocal:",vocal,"- Codi Morse: ---")
     
if (vocal == "u" or vocal == "U"):
     print("Vocal:",vocal,"- Codi Morse: ..-")