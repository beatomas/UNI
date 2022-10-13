

class CompteCorrent():
    def __init__(self, nom, capital):
        self.nom = nom
        self.capital=capital
    def rendiment(self,mesos):
        return(0)
        
class CompteRemunerat(CompteCorrent):
    def __init__(self,nom,capital,interes):
        CompteCorrent.__init__(self,nom,capital)
        self.interes=interes
    
    def rendiment(self,mesos):
        r = self.capital * (( (1+(self.interes/100)) **mesos) -1)
        return (r)
    
class CompteFixe(CompteRemunerat):
    def __init__(self,nom,capital,interes,periode):
        CompteRemunerat.__init__(self,nom,capital,interes)
        self.periode = periode

    def rendiment(self,mesos):
        r = self.capital * ((self.interes/100) * mesos)
        return (r)
    
cc = CompteCorrent("Javier Vilajosana", 3000)
cr = CompteRemunerat("Rodolfo Arias", 3000,0.25)
cf = CompteFixe("Guillem Redeu", 3000, 1.25,48)

print("Corrent: ", cc.rendiment(12), "Remunerat: ", cr.rendiment(12), "Fixe: ", cf.rendiment(12))

