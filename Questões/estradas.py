import sys
sys.setrecursionlimit(10000)

def find(x,pais):
    if pais[x]<0:
        return x
    pais[x] = find(pais[x],pais)
    return pais[x]
def union(a,b,pais):
    representanteA = find(a,pais)
    representanteB = find(b,pais)
    if representanteA == representanteB:
        return None,None
    if representanteB < representanteA:
        representanteA, representanteB = representanteB, representanteA
    pais[representanteA] += pais[representanteB]
    pais[representanteB] = representanteA
    return True
def main():
    n,m = [int(x) for x in input().split()]
    pais = [-1]*(n+1)
    
    grafo = []
    for i in range(m):
        a, b = [int(x)for x in input().split()]
        union(a,b,pais)
        grafo.append((a,b))


    representantes = []
    for cidade in range(1,n+1):
        if cidade == find(cidade,pais):
            representantes.append(cidade)
    saida = len(representantes) -1
    print(saida)

    for i in range(saida):
        print(representantes[i],representantes[i+1])
main()