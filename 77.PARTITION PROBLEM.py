def findpartition(n,k):
    dp=[[0 for i in range(n+1)]for j in range(k+1)]

    for i in range(1,k+1):
        for j in range(1,n+1):

            if i==1:
                dp[i][j]=1
            elif j<i:
                dp[i][j]=0
            elif i==j:
                dp[i][j]=1
            else:
                dp[i][j]=dp[i][j-1]*i+dp[i-1][j-1]

    print(dp[k][n])
findpartition(3,2)