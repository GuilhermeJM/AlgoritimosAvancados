from heapq import heappop,heappush

def dijkstra(grafo, comeco):
    x = len(grafo)
    caminhos = []
    for _ in range(x):  
        caminhos.append([])
    caminhos[comeco] = 1
    dist = [float('inf')]*x
    dist[comeco] = 0
    heap = [(0,comeco)]
    while heap:
        distancia_atual, no = heappop(heap)
        if distancia_atual >dist[no]:
            continue
        for vizinho,peso in grafo[no]:
            nova_dist = dist[no] + peso
            caminhos[vizinho].append(no)
            if nova_dist < dist[vizinho]:
                dist[vizinho] = nova_dist
                heappush(heap,(nova_dist,vizinho))
    return caminhos,dist

n, m = map(int,input().split())
grafo = []
for _ in range(n):
    grafo.append([])
for _ in range(m):
    a,b,c = map(int,input().split())
    grafo[a-1].append((b-1,c))

caminho,dist = dijkstra(grafo, 0)
print(caminho,dist)
