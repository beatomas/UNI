
def suspesos(l):
    l_suspesos = list(filter(lambda x:x[1]<5,l))
    l_nius = list(map(lambda x:x[0],l_suspesos))
    return l_nius

