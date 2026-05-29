"""
---GRAFOS---

São um tipo de estrutura de dados que modelam um caminho, nesse caminho existe 2 conceitos:
    - VERTICES OU NÓS: eles são o ponto de 'parada' ou seja, se pessarmos nisso como um mapa
o nó seria um ponto dentro desse mapa.
    - ARESTAS  : as arestas seriam o caminho em si, a ligação entre os pontos do mapa, o caminho
traçado. Resumindo, ele é o elo de ligação em si dos nós.

Existem 2 tipos de grafos:
    - DIRIGIDOS OU DIRECIONADOS: são grafos que seus nós se conectam com as arestas de forma 
unidirecional, ou seja, uma pessoa que estiver em um nó A, se ele estiver conectado com uma
aresta direcional para um nó B, ele pode pode ir de A para B, mas não de B para A.
*obs.: em um grafo dirigido é permitido um self-loop, ou seja, um nó, através de uma aresta,
apontar para ele mesmo.
    - NÃO DIRIGIDOS ou NÃO DIRECIONADOS: se um ponto A está ligado com um ponto B, tanto é 
    possivel ir de A para B quanto de B para A.
**obs.: nesse tipo de grafo não é permitido o self-loop.

NOMECLATURAS:
    - (U,V): essa seria um tipo de aresta, algo como uma tupla que liga de u para v, no caso
do grafo ser direcional, isso quer dizer que V é vizinho de U, entretanto, U não é vizinho de
V. pois a aresta está direcionada de U para V. Em caso de não dirigidos esse problema não existe.
    - ADJACENCIA: resumidamente diz se um nó é adjacente a outro, ou seja, se um nó está ligado
a outro. Nesse sentido, continua tendo a implicação de (U,V), se for um grafo direcional, (U,V)
não implica em (V,U), entretanto, em um não direcional, (U,V) implica em (V,U)
    - CAMINHO: caminho é um conjuto de arestas que estão interligadas pelos nós. "um caminho de
um vertice X para um vertice Y é uma sequencia de vertices em que, para cada vertice, do primeiro
até o penultimo, há uma aresta ligando esse vertice ao próximo na sequencia."
    - COMPRIMENTO: é literalmente o numero de arestas de um caminho.
    - CICLOS: acontece quando há um caminho ciclico, ou seja, um caminho em que A->B->C->A. Um 
Self-Loop também é um ciclo.

GRAU DOS VERTICES, em grafos NÃO DIRIGIDOS,Para contar o grau do vertice basta contar a quantidade 
de arestas que sái/entra nele, para os DIRIGIDOS, existem 3 tipos de grau, o grau de saída, o 
grau de entrada e o grau "geral" que é a soma das entradas e das saídas.

CONEXÃO:
    - CONEXO em não dirigido: o grafo é conexo se todos os nós do grafo estiverem conectados em
um só caminho. 
    - DESCONEXO em não dirigidos: o grafo é desconexo se algum nó do grafo não estiver conecta-
do com o restante.
    - FORTEMENTE CONEXO(apenas grafos dirigidos): um grafo dirigido será fortemente conexo se 
partindo do ponto A, é possivel chegar em qualquer vertice e depois chegar no ponto A novamente.
    - CONEXO em grafo direcional: um grafo direcional é conexo se todos os pontos estiverem conec-
tados, entretato, essa conexão não precisa ser de via dupla. "é possivel ir, mas nem sempre é pos-
sivel voltar.
    - FRACAMENTE CONEXO(apenas grados direcionados): todos os nós estão conectados, mas não é pos-
sivel acessar um nó a partir de outro nó.

Todos os grafos também podem ser PONDERADOS, ou seja, as arestas podem ter valores(peso, custo, dis-
tancia...), esses valores podem ser positivos, negativos ou qualquer numero valido, dessa forma elas
podem ser uteis para achar o menor caminho, maior caminho, ou qualquer outra utilidade que a pondera-
ção possa gerar.

"""


#após a teoria, vem em seguida as representações:

#MAPA OU DIC

grafo_01 = {

    "A": ["B","C","d"],
    "B": ["A", "C"],
    "C": ["A", "B", "D"],
    "D": ["A", "C"]

}