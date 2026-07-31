# n = qntd pendrive
# m = tam do arquivo
n = int(input())
m = int(input())
lista = []
for _ in range(n):
    p = int(input())
    lista.append(p)

lista.sort()
total = 0 
np = 0
for i in range(n-1,-1,-1):
    if total >= m:
        break
    total += lista[i]
    np += 1

print(np)