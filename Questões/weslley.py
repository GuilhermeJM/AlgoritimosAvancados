from heapq import heappop, heappush

def dijskra(grafo,inicio):
    x = len(grafo)
    dist = [float('inf')] * x
    dist[inicio] = 0
    heap = [(0,inicio)]
    while heap:
        distancia_atual, no = heappop(heap)
        if distancia_atual > dist[no]:
            continue
        for vizinho, peso in grafo[no]:
            nova_dist = dist[no] + peso
            if nova_dist< dist[vizinho]:
                dist[vizinho] = nova_dist
                heappush(heap,(nova_dist,vizinho))
    return dist

n, m = map(int,input().split())
grafo = []
for _ in range(n):
    grafo.append([])
for _ in range(m):
    a,b,c = map(int,input().split())
    grafo[a-1].append((b-1,c))
grafo.reverse()
dists = dijskra(grafo,0)
print(*dists)