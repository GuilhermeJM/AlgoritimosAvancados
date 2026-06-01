
def main():
    n = int(input())
    lista = [0] * (n+1)
    dic = {}
    #crio uma lista
    for i in range(1,n+1):
        f = int(input())
        lista[i] = f
        dic[i] = []
    #crio um grafo
    for i in range(1, n+1):
        if lista[i] != -1:
            dic[lista[i]].append(i)
    grupos = 0
    #verifico os nós que não tem filho, se não houver, é um grupo a mais
    for j in range(1,n+1):
        if dic[j] != []:
            grupos+=1
    print(dic)
    print(grupos+1)
main()
