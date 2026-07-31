import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def find(a):
    if pais[a]<0:
        return a
    pais[a] = find(pais[a])
    return pais[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    if b < a:
        a, b = b, a
    pais[a] += pais[b]
    pais[b] = a
    return True

def kruskal(n, arestas):
    arestas.sort()
    custo_total = 0
    count = 0
    for peso, u, v in arestas:
        if union(u,v):
            custo_total += peso
            count += 1
        if count == (n-1):
            break
    if count != n-1:
        return "IMPOSSIBLE"
    return custo_total

n, m = map(int, input().split())

pais = [-1] *(n+1)
arestas = []
for _ in range(m):
    u,v,p = map(int,input().split())
    arestas.append((p,u,v))

total = kruskal(n, arestas)
print(total)