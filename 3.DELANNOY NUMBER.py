def findDelannoyNumber(n,m):
    dp=[[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(m,-1,-1):
        for j in range(n,-1,-1):

            if i==m and j==n:
                dp[i][j]=1

            elif i==m:
                dp[i][j]=dp[i][j+1]

            elif j==n:
                dp[i][j]=dp[i+1][j]

            else:
                dp[i][j]=dp[i][j+1]+dp[i+1][j]+dp[i+1][j+1]

    print(dp[0][0])

findDelannoyNumber(3,4)