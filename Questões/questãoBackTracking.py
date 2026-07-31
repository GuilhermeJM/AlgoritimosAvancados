n = int(input())
lista = [int(x) for x in input().split()]
print(pow(2,len(lista)))
check = [0] * len(lista)
teste = backtrack(check)
def backtrack(estado,j=0, atual = []):
    if estado[-1] == 1:
        print(atual)
        return True
    for i in range(j,estado):
        if estado[i] == 0:
            print(atual)
            atual.append(i+1)
            if backtrack(estado,j,atual):
                return True
            else:
                continue
            
    return False