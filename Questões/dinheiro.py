d = int(input())
ncem = d // 100
restocem = d % 100
nvinte = restocem // 20
restovinte = restocem% 20
ndez = restovinte // 10
restodez = restovinte % 10
ncinco = restodez // 5
restocinco = restodez % 5
total = 0
for n in [ncem,nvinte,ndez,ncinco,restocinco]:
    if n >=1:
        total+=n

print(total)