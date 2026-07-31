a,b,c = map(int,input().split())
maxi = max(a,b,c)
mini = min(a,b,c)
meio = (a+b+c) - maxi - mini
total = abs(maxi-meio) + abs(mini-meio)
print(total)