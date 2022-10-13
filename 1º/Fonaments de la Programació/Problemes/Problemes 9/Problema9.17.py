def cicle(x):
    if ((type(x) is not list) and (type(x) is not str)):
        raise TypeError("Tipus Incorrecte")
    while True:
        for i in x:
            yield i
       