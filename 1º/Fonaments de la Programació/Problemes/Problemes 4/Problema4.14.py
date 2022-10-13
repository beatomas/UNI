
aprovats=[]
suspesos=[]

num_est=int(input("Introdueix el número d'estudiants: "))

for compt in range(num_est):
    niu=int(input("Introdueix el NIU: "))
    nota=float(input("Introdueix la nota: "))
    if (nota>=5):
        aprovats.append(niu)
    else:
        suspesos.append(niu)

print("Aprovats",len(aprovats),aprovats)
print("Suspesos",len(suspesos),suspesos)
