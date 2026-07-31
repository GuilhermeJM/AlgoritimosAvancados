def fib():
    n = int(input())
    if n <= 0:
        print(n)
    else:
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] +dp[i-2]

        print(dp[-1])

def escadas():
    n = int(input())
    if n <= 2:
        print(n)
    else:
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]

        print(dp[-1])


def maxnum():
    lista = list(map(int,input().split()))
    n = len(lista)
    if n<=2:
        print(max(lista))
    else:
        dp = [0]*(n+1)
        dp[1] = lista[0]
        for i in range(2,n+1):
            dp[i] = max(lista[i-1]+dp[i-2],dp[i-1])
            print(dp)

        print(dp[-1])

def dice():
    n = int(input())
    if n <=2:
        print(n)
    else:
        dp = [0] *(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + (2*dp[i-2])
            print(dp)
        print(dp[-1])
dice()