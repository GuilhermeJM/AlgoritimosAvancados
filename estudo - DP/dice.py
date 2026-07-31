def dice():
    n = int(input())
    if n <=6:
        print(2**(n-1))
    else:
        dp = [0] *(n+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        dp[4] = 8
        dp[5] = 16
        dp[6] = 32
        for i in range(7,n+1):
            dp[i] = pow((dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4] + dp[i-5] + dp[i-6]),1,10**9+7)
        print(pow(dp[-1],1,10**9+7))
dice()