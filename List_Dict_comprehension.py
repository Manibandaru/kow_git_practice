# list_comprehension

l=[1,3,4,6,7]
l_c=[i**2 for i in l]
l_c1=[i**2 for i in l if i%2==0]

print(l_c)
print(l_c1)

D=range(10)
D_C={i:i**2 for i in D}
D_C1={i:i**2 for i in D if i%2==0}
print(D_C)
print(D_C1)