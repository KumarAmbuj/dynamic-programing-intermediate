def findways(n,k):
    dp=[[[0,0]for j in range(n+1)]for i in range(k+1)]
    dp[0][1][0]=1
    dp[0][1][1]=1

    for i in range(k+1):
        for j in range(2,n+1):
            dp[i][j][0]=dp[i][j-1][0]+dp[i][j-1][1]

            dp[i][j][1] = dp[i][j - 1][0]
            if i>=1:
                dp[i][j][1]+=dp[i-1][j-1][1]
    print(dp[k][n][0]+dp[k][n][1])

findways(5,2)
findways(4,1)



