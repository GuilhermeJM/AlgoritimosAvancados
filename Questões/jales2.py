n = int(input())
for _ in range(n):
    num = input()
    a = 0
    zero = 0
    um = 0 
    for n in num:
        if n ==0:
            zero +=1
        else:
            um +=1  
    if (max(um,zero)-min(um,zero))%2==0:
        print("NET")
    else:
        print("DA")