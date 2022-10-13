

class Estudiant():
    def __init__(self,niu,nom,cognoms,nota):
        self.niu = niu
        self.nom = nom
        self.cognoms = cognoms
        self.nota = nota
    def __str__(self):
        return (str(self.niu) + " "
                + str(self.nom) + " "
                + str(self.cognoms) + " "
                + str(self.nota))
        
class Assignatura():
    def __init__(self,codi,nom,llista):
        self.codi = codi
        self.nom = nom
        self.llista = llista
        
    def esta_en_llista(self,niu):
        for n in self.llista:
            if niu in n.niu:
                return True
            else:
                return False
    def afegir_estudiants(self,estudiant):
        self.llista.append(estudiant)
        
    def llistar_estudiants(self):
        for x in self.llista:
            print(x)
            
codi = input("Introdueix el codi de l'assignatura: ")
nom = input("Introdueix el nom de l'assignatura: ")
llista = []
assignatura = Assignatura(codi,nom,llista)

opcio = "S"

while opcio == "S" or opcio == "s":
    niu = input("Introdueix el niu: ")
    if assignatura.esta_en_llista(niu) == True:
        print("Error: Estudiant existent")
    else:
        noms = input("Introdueix el nom: ")
        cognom = input("Introdueix els cognoms: ")
        while True:
            try:
                nota = float(input("Introdueix la nota: "))
            except ValueError:
                print("Error: Tipus d'entrada incorrecte")
            else:
                break
    estudiant = Estudiant(niu,noms,cognom,nota)
    assignatura.afegir_estudiants(estudiant)
    opcio = input("Vols introduïr més estudiants? (S/-)")
    
assignatura.llistar_estudiants()
    
    
    
    
    
    
    
    
    