

def Text2Morse(paraula,dic):
    par = paraula.upper()
    final = ""
    a = 0
    while a < len(paraula):
        codi = dic[par[a]]
        final += codi
        a += 1
    return final   
      
