prime=[]
def prime_numbers(n):
    if n>1:
        for i in range(2,n+1):
            for j in range(2,i):
                if i%j == 0:
                    prime.append(i)
        return prime
print(prime_numbers(23))

