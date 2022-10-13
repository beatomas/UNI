

def CrearIndex(nom_fitxer):
    Dict = {}
    fitxer = open(nom_fitxer,"r")
    num = 1
    for linia in fitxer:
        for paraula in linia.split():
            if (paraula not in Dict):
                Dict[paraula]={num}
            elif (num not in Dict[paraula]):
                Dict[paraula].add(num)
        num += 1
        
    fitxer.close()
    return Dict