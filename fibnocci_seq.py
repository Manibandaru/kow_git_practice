def fab_seq(n):
    print(n)
    res = []
    a,b=0,1
    for i in range(n):
        res.append(a)
        a,b=b,a+b
    print("successfully executed")
    return res


print(fab_seq(10))