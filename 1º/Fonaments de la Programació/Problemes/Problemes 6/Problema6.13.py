
def Columna (var,pos):

    ok=""

    if (len(var)==pos):

        ok = var

    elif (len(var)<pos):

        ok = var

        for i in range (pos-len(var)):
            ok =ok + " "

    else:
        ok= var[:pos]

    return ok

def escriure_dades_estudiant (NIA, nom, primer_cognom, segon_cognom, nota):
    NIA_ok=Columna (str(NIA), 7)
    nom_ok = Columna (nom, 12)
    primer_cognom_ok = Columna(primer_cognom, 12)

    segon_cognom_ok = Columna (segon_cognom, 12)

    if (nota != 10):
        nota_ok=" "+str(nota)
        if len(nota_ok)==4:
            nota_ok=nota_ok+" "

    else:

        nota_ok=str(nota)+" "

    nameHandle=open("DadesEstudiants.txt", "a")
    nameHandle.write(NIA_ok+" "+nom_ok+" "+primer_cognom_ok+" "+segon_cognom_ok+" "+nota_ok+"\n")
    nameHandle.close