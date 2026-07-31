from math import gcd,isqrt
n = int(input())
lista = [int(x) for x in input().split()]
m = 0 
for h in lista:
    m = gcd(m,h)

limite = int(isqrt(m))
resp = 0
for i in range(1, limite + 1):
    if m % i == 0:
        if i == m // i:
            resp += 1
        else:
            resp += 2
print(resp)
