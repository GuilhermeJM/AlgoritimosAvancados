def crivo(n):
    lista = [True] *(n+1)
    if n >= 0:
        lista[0] = False
    if n>= 1:
        lista[1] = False
    p = 2
    while p*p <= n:
        if lista[p]:
            multiplo = p*p
        while multiplo<= n:
            lista[multiplo] = False
            multiplo += p
        p+=1
    return lista

def main():
    n = int(input())
    lista = crivo(n)
    for i in range(len(lista)):
        if lista[i]:
            print(i)
main()