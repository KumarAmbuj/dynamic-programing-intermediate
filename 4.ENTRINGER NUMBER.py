def findNumber(n,k):

    dp=[[0 for j in range(k+1)] for i in range(n+1)]
    dp[0][0]=1

    for i in range(1, n + 1):
        dp[i][0] = 0


    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = (dp[i][j - 1]
                        + dp[i - 1][i - j])
    print(dp[n][k])

findNumber(4,3)
