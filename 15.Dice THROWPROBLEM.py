def findways(m,n,x):
    dp=[[0 for j in range(x+1)]for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,x+1):

            if i == 1 and j<=m:
                dp[i][j] = 1

            elif j < i:
                dp[i][j]=0

            else:
                for k in range(1,m+1):
                    if j-k>=0:
                        dp[i][j]+=dp[i-1][j-k]

    print(dp[n][x])

findways(6,3,8)
findways(4,2,5)

