"""
==============================================================
                    TEORIA DOS JOGOS
- resumidamente é so um "jogo" onde estamos considerando onde
sempre, todos participantes, fazem "a melhor jogada", ou seja
sempre o passo otimo.
- achar padrão.
- estados(é como o "jogo" está naquele momento).
- a partir do estado inicial, a gente consegue descobrir quem
ganhou.
- invariancia(coisas que n mudam independente da jogada ou do
estado).
- estado perdedor(independente do que eu fizer, o oponente
ganha).
- estado vencedor(se houver pelo menos uma jogada em que me ga
ranta a vitoria, esse é o estado vencedor.)
- teorema do xor(um numero xor outro, n ^ m).
- jogo do nim, ele usa a ideia do teorema do xor aí.
- função mex(menor inteiro negativo que não pertence ao con-
junto) 
- grandy ou nimber(usa o mex).
(o jogador 1 ganhara o jogo se o g(n1)^g(n2)^...^g(nk)>0 se não
o jogador ganhará )
cses, task 1729

==============================================================
"""
"""
def grandy(numeros, passos):
    lista = []
    for i in range(1,len(numeros)+1):
        if numeros[i] == -1:
            for n in passos
    return lista

def mex(numeros):
    atual = 0
    while atual in numeros:
        atual +=1
    return atual

def main():
    a,b = map(int,input().split())
    lista = [int(x) for x in input().split()]
    lista_grandy = [-1] * (n+1)
    saida = ""
    lista_grandy = grandy(lista_grandy,lista)
    for i in range(1,a+1):
        gn = grandy(i,lista)
        acumulado = 0
        for n in gn:
            acumulado ^= n
        if acumulado!= 0:
            saida+="W"
        else: 
            saida += "L"
            
    print(saida)
main()

"""
