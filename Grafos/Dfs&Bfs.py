""" 
    - DFS: busca por profundidade, ou seja, ele vai do vertice até o final, antes de voltar e
ir para os outros filhos.
    - BFS: busca por largura, ou seja, antes de ir até o "final" do grafo, ele visita todos os
nós do mesmo layer

"""

#DFS por recursão.

def Dfs_recursivo(grafo, vertice, visitados=None):
    if visitados == None:
        visitados = set()
    
    visitados.add(vertice)
    print(vertice)

    for vizinho in grafo[vertice]:
        if vizinho not in visitados:
            Dfs_recursivo(grafo,vizinho,visitados)

#DFS por pilha
def Dfs_pilha(grafo, vertice, visitados = None):
    if visitados == None:
        visitados = set()
    
    pilha=[]
    pilha.append(vertice)

    while len(pilha)>0:
        nó = pilha[-1]
        pilha.pop() 
    
        if nó not in visitados:
            print(nó)
            visitados.add(nó)
            for vizinho in range(len(grafo[nó])-1,-1,-1):
                pilha.append(grafo[nó][vizinho])

#BFS
#temos que importar o 'deque', from collections import deque
from collections import deque

def Bfs(grafo, vertice):
    fila = deque([vertice])
    visitados = set()
    visitados.add(vertice)

    while fila:
        atual = fila.popleft()
        print(atual)
        visitados.add(atual)

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                fila.append(vizinho)

#Main
def main():
    grafo = [
        [1, 2],
        [0, 3, 4],
        [0, 5, 6],
        [1],
        [1],
        [2],
        [2]
    ]
    Bfs(grafo,0)

main()