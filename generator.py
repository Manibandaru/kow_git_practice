# generator

def fabnocci(n):
    a,b=0,1
    if n>0:
        for i in range(n):
            yield a
            a,b = b,a + b
generator=fabnocci(10)
print(next(generator))
print(next(generator))

