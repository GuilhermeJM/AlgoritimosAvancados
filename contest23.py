import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

def teste(atual,variavel = False):
    if atual == x:
        variavel = True
        return variavel
    for i in range(n-1,-1,-1):
        num = listaA[i]
        if atual + num not in listaB and atual + num <= x:
            atual += num
            variavel = teste(atual)
            if variavel:
                break
            atual -= num
    return variavel


n = int(input())
listaA = [int(x) for x in input().split()]
m = int(input())
listaB = n*[False]
listaB = set(int(x) for x in input().split())
print(listaB)
x = int(input())
atual = 0
sera = teste(atual)
if sera:
    print("Yes")
else:
    print("No")

    



"""

==================
code forces 2107-B
==================

n = int(input())
for _ in range(n):
    m,k = map(int,input().split())
    lista = [int(x) for x in input().split()]
    jogador_atual = True
    total = sum(lista)
    
    if total%2==0:
        print("Jerry")
    else:
        lista.sort()
        lista[-1] -= 1
        if max(lista) - min(lista) > k:
            print("Jerry")
        else:
            print("Tom")
"""