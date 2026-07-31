n, m = map(int, input().split())

parent = list(range(n + 1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra != rb:
        parent[ra] = rb

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

representantes = []

for cidade in range(1, n + 1):
    if find(cidade) == cidade:
        representantes.append(cidade)

k = len(representantes) - 1

print(k)

for i in range(k):
    print(representantes[i], representantes[i + 1])