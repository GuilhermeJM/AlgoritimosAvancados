import sys
sys.setrecursionlimit(10000000)
"""
    ==============================================================
    a ideia é qubrar o problema em menores...
    maximizar algo, minimizar algo
    tipos, problema P gera o problema  A B C e o problema A, B e C
    tem o "mesmo problema".
    muito parecido com recursao, entretando usa muita memoria, ela
    guarda o conteudo para n precisar calcular dnv.
    "use DP para quando a solução depende comparar cenarios e com-
    binar solucoes otimas de subproblemas"
    ==============================================================
    
"""
"""
def fibonachi(x):
    if x>0:
        dp[0] = 0
        return 0
    if x == 1:
        dp[1] = 1
        return 1
    if dp[x] != -1:
        return dp[x]
    dp[x] = fibonachi(x-1) + fibonachi(x-2)
    return dp[x]

def main():
    a = int(input())
    dp = [-1]*a

    resposta = fibonachi(a)
    for i in dp:
        print    
        
main()
    """
"""    
def dado(x):
    if x < 0:
        return 0
    if x == 0:
        dp[x] = 1
        return 1
    if x == 1:
        dp[x] = 1
        return 1
    if dp[x] != -1:
        return dp[x] 
    else:
        dp[x] = dado(x-6) + dado(x-5) + dado(x-4) + dado(x-3) + dado(x-2) + dado(x-1)
    return dp[x]

entrada = int(input())

dp = [-1] * (entrada+1)
print(pow(dado(entrada),1,(10**9 )+7))
dp = []
for x in range(1,entrada+1):
    b = 0
    for j in range(6):
        a = b - j-1
        if a>= 0: 
            b += dp[a]
        else:
            break
    if (x>=1 and x<=6):
        b+=1
    b = pow(b,1,10**9+7)
    dp.append(b)
print(dp[-1])
"""
        
'''
def main():
    entrada = [int(x) for x in input().split()]
    nums = [0] + entrada
    n = len(entrada)
    dp = [0] * (n+1)
    if n>=1:
        dp[1] = nums[1]
    for i in range(2,n+1):
        dp[i] = max(dp[i-1],dp[i-2] + nums[i])
        
    print(dp[n])
    
main()
'''

"""
def main():
    m, n = map(int,input().split())
    matriz  = []
    for i in range(m):
        matriz.append([0]*n)
    matriz[0][0] = 1
    for i in range(m):
        for j in range(n):
        
            if j == 0:
                matriz[i][j] = 1
            elif i == 0: 
                matriz[i][j] = 1
            else:
                matriz[i][j] = matriz[i-1][j] + matriz[i][j-1] 
    print(matriz)
    print(matriz[m-1][n-1])
    
main()
"""
"""
def main():
    coins = [1,2,5]
    amount = 11
    n = len(coins)
    dp = [float('inf')]*(amount)
    if amount == 0: 
        return 0
    menor = float('inf')
    for coin in coins:
        dp[coin-1] = 1
    for i in range(amount):
        for j in range()
        atual = dp[amount - coins[i]]
        if atual >=0:
            continue
        if atual <= menor:
            menor = atual
    dp[amount] = 1+menor
    return dp[amount]
    
    
main()

def teste():
    inf = 10**9
    dp = [inf] * (amount+1)
    dp[0] = 0
    for x in range(1, amount+1):
        for coin in coins:
            if x - coin>= 0:
                dp[x] = min(dp[x],dp[x-coin]+1)
    if dp[amount] == inf:
        print(-1)
    else:
        print(dp[amount])
"""