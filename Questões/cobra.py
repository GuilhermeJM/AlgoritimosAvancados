a, b = input().split()
linhas = int(a)
colunas = int(b)
matriz = []
linha = 0
variavel = 1
while linha<linhas:
    matriz.append([]) 
    if linha%2 == 0:
        string = '#' * colunas
    else: 
        if variavel == 1:
            string1 = '.' * (colunas-1)
            string = string1 + '#'
            variavel = 2
        else:
            string1 = '.' * (colunas-1)
            string = '#' + string1
            variavel = 1
    matriz[linha].append(string)
    linha += 1

for linha in matriz:
    print(*linha)