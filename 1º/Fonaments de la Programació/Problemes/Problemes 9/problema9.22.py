
def palindrom(l):
    llista2 = []
    llista2 = list(filter(lambda x: x == x[::-1],l))
    return llista2