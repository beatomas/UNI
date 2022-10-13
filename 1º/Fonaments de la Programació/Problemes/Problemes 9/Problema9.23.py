

def majuscules(llista):
    return [list(x.upper()) for x in llista if len(x) > 3 and x[len(x)-1] in 'aeiouAEIOU']
