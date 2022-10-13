

def bubble(x):
    for i in range(len(x)):
        for j in range(len(x)-1-i):
            if x[j] > x[j+1]:
                a = 0
                a = x[j]
                x[j]=x[j+1]
                x[j+1] = a
    return x
    