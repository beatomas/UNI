

def Lyrics2list(lletra):
    aux = []
    for c in lletra:
        if (c>= 'A' and c<= 'Z'):
            aux.append(chr(ord(c)+32))
        else:
            if (c>= 'a' and c<= 'z' or c == ' '):
                aux.append(c)
    new_lletra = "".join(aux)
    out = new_lletra.split()
    
    return(out)