
anys = int(input("Introdueix et teu any de naixement: "))

edat = 2019 - anys

if (edat >= 18):
    print("Tens",edat,"anys i ets major d'edat.")
    if (edat <67):
        print("Estàs en edat de treballar.")
    else:
        print("Estàs en edat de jubilació.")

else:
    print("Tens",edat,"anys i ets menor d'edat.")
    if (edat <= 12):
        print("Encara no has acabat primària.")
    else:
        print("Has acabat primària.")