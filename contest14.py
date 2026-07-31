n = int(input())
for _ in range(n):
    atual = int(input())
    if atual <= 0:
        print("NO")
    else:
        if atual%11 == 0:
            print("YES")
        elif atual %111 == 0:
            print("YES")
        elif atual %1111 == 0:
            print("YES")
        elif atual %11111 == 0:
            print("YES")
        elif atual %111111 == 0:
            print("YES")
        elif atual %1111111 == 0:
            print("YES")
        elif atual %11111111 == 0:
            print("YES")
        elif atual %111111111 == 0:
            print("YES")
        elif atual %1111111111 == 0:
            print("YES")
        else:
            atual = pow(atual,1,1111111111)
            atual = pow(atual,1,111111111)
            atual = pow(atual,1,11111111)
            atual = pow(atual,1,1111111)
            atual = pow(atual,1,111111)
            atual = pow(atual,1,11111)
            atual = pow(atual,1,1111)
            atual = pow(atual,1,111)
            atual = pow(atual,1,11)
            if atual==0:
                print("YES")
            else:
                print("NO")
