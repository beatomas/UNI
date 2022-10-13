
class Personal():
    def __init__(self,Nom,Cognom,Domicili):
        self.n = Nom
        self.c = Cognom
        self.d = Domicili

class Estudiant(Personal):
    def __init__(self,Nom,Cognom,Domicili,Carrera,Any_Inici,Taxa):
        Personal.__init__(self,Nom,Cognom,Domicili)
        self.ca = Carrera
        self.a = Any_Inici
        self.t = Taxa

class PAS(Personal):
    def __init__(self,Nom,Cognom,Domicili,Facultat,Salari):
        Personal.__init__(self,Nom,Cognom,Domicili)
        self.f = Facultat
        self.s = Salari
        
class Professorat(PAS):
    def __init__(self,Nom,Cognom,Domicili,Facultat,Salari,Assignatures):
        PAS.__init__(self,Nom,Cognom,Domicili,Facultat,Salari)
        self.ass = Assignatures