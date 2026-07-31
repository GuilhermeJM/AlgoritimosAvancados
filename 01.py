def dfs(vertice, grafo, visitados = None,pilha=None):
    if visitados == None:
        visitados = set()
    if pilha == None:
        pilha = []
    pilha.append(vertice)
    grupos = 0
    while len(pilha)>0:
        nó = pilha[-1]
        pilha.pop() 
    
        if nó not in visitados:
            visitados.add(nó)
            if len(grafo[nó]) <=0:
                grupos+=1
            for vizinho in range(len(grafo[nó])):
                pilha.append(grafo[nó][vizinho])

    return grupos
