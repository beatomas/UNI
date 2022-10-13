
def majuscules(l):
    f = filter(lambda s:len(s)>3, l)
    m = map(lambda s:s.upper(), f)
    l2 = list(m)
    return l2

    return list(map(lambda s:s.upper(), filter(lambda s:len(s)>3, l)))