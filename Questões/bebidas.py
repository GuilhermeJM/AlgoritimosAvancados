# n = n lojas que vendem a bebida
# a proxima linha vai dizer o valor dessa bebida na loja "i"
# q = o numero de dias que a mulher quer comprar as bebidas 
# as proximas linhas são os valores que a mulher pode gastar nesse dia(linha)
import sys
input = sys.stdin.readline

def busca_binaria(vetor, alvo):
    esquerda = 0
    direita = len(vetor)

    while esquerda < direita:
        meio = (esquerda + direita) // 2

        if vetor[meio] <= alvo:
            esquerda = meio + 1
        else:
            direita = meio

    return esquerda


n = int(input())
precos = list(map(int, input().split()))

precos.sort()

q = int(input())

for _ in range(q):
    dinheiro = int(input())
    print(busca_binaria(precos, dinheiro))