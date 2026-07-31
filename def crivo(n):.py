def crivo(n):
    primos = [True]*(n+1)
    if n >= 0:
        primos[0] = False
    if n >= 1:
        primos[1] = False
    p = 2
    while p*p < n:
        if primos[p]:
            k = p * p
            primos[k] = False
            while k <= n:
                primos[k]= False
                k += p
        p += 1
    return primos
def divisiveis(primos, n):
    if primos[n]:
        return 2
    max = n//2
    saida = dict()
    i = 0
    while i<=n:
        if primos[i]:
            if n%i == 0:
                saida.append(i)
                n = n/i
            else:
                i+=1
        else:
            i+=1
    return saida
def main():
    n = int(input())
    primos = crivo(n)
    fatores = divisiveis(primos, n)
    
    print()
    
main()