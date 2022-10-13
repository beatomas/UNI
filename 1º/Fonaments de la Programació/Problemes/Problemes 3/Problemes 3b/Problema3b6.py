
salari_base = float(input("Introdueix el salari base en euros: "))
antiguitat = int(input("Introdueix l'antiguitat: "))

if (antiguitat < 3):
    salari = salari_base + (salari_base/100)
    
else:
    if (antiguitat < 5):
        salari = salari_base + ((salari_base*2)/100)
    else:
        salari = salari_base + ((salari_base*3.5)/100)
    
print("El salari final és:",salari)