

teoria = float(input("Introdueix la teva nota de teoria: "))
seminaris = float(input("Introdueix la teva nota de seminaris: "))
practiques = float(input("Introdueix la teva nota de practiques: "))

nota_final = teoria*0.4 + seminaris*0.3 + practiques*0.3

if (0.00 <= nota_final < 4.99):
    print("La nota final és",nota_final,"- SUSPES")
else:
    if(nota_final < 6.99):
        print("La nota final és",nota_final,"- APROVAT")
    else:
        if(nota_final < 8.99):
            print("La nota final és",nota_final,"- NOTABLE")
        else:
            if(nota_final < 9.99):
                print("La nota final és",nota_final,"- EXCEL.LENT")
            else:
                print("La nota final és",nota_final,"- MATRICULA D'HONOR")
        
