

num = int(input("Introdueix el número d'unitats venudes: "))
preu = float(input("Introdueix el preu del producte: "))

preu2 = preu*num

preu_IVA = (preu*num)*1.07

if (preu_IVA > 1000):
    preu_final = preu_IVA - preu_IVA*0.10
else:
    if (preu_IVA > 500):
        preu_final = preu_IVA - preu_IVA*0.05
    else:
        preu_final = preu_IVA
        
print("L'import final de la compra són",preu_final,"euros.")