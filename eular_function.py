import math

def isPositiveInt(n):
    try:
        val = int(n)
        if val <= 0:  # if not a positive int print message and ask for input again
            exit()
    except ValueError:
        exit()

def eular_fhi_func(n):
    p = prime_factorization(n)  # prime factor list
    q = len(p)  # numbers of prime factor
    
    for x in p:
        n = n * (1-1/x)
    return int(n)

def prime_factorization(n):
    factors=[]
    i = 2
    while n >= i:
        if n%i == 0: 
            if i not in factors:
                factors.append(i) 
            n = n//i
            i=2 
        else:
            i = i+1 
    return factors

if __name__ == "__main__":
    
    n = int(input())
    isPositiveInt(n)

    while (n>0):
        x = int(input())
        isPositiveInt(x)
        print(eular_fhi_func(x))
        n-=1
