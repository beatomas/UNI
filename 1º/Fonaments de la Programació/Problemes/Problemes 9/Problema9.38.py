

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
    
def Uniques(llista):
    conjunt = set(llista)
    llist = list(conjunt)
    return llist

def Lyrics2frequencies(llista):
    myDict = {}
    for word in llista:
        if word in myDict:
            myDict[word]+=1
        else:
            myDict[word]=1
    return myDict

def Most_common_words(frequencies):
    values = frequencies.values()
    best = max(values)
    words = []
    for k in frequencies:
        if frequencies[k] == best:
            words.append(k)
        
    return(words,best)
    
    
    
    
    
    