
def fib(x):
    if (x <= 2):
        if x == 1:
            yield 0
        else:
            yield 0
            yield 1
            
    else:
        res_2=0
        res_1=1
        yield 0
        yield 1
        i = 2
        while (i < x):
            res=res_2+res_1
            yield res
            res_2=res_1
            res_1=res
            i+=1
        
fib(2)
    
    



    