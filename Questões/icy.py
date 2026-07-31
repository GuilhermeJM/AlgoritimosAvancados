def find(a,pais): 
    if pais[a] != a:
        pais[a] = find(pais[a],pais)
    return pais[a]

def union(a,b, pais):
    ra = find(a, pais)
    rb = find(b, pais)
    if ra != rb:
        pais[ra] = rb 
       

def main():
   
    n_pilha = int(input())
    pais = list(range(n_pilha))
    grafo = []
    for i in range(n_pilha):
        x,y = [int(x) for x in input().split()]
        grafo.append((x,y))
  
    for i in range(n_pilha):
        for j in range(i+1,(n_pilha)):
            x1,y1 = grafo[i]
            x2,y2 = grafo[j]
            if x1==x2 or y1==y2:
                union(i,j,pais)
    
    pilhas = set()
    for i in range(n_pilha):
        pilhas.add(find(i,pais))

    print(len(pilhas)-1)
    
main()