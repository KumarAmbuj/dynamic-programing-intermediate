def findeulerianNumber(n,m):

    dp=[[0 for j in range(n+2)] for i in range(m+2)]

    for i in range(m+2):
        for j in range(n+2):
            if i==0 and j==0:
                dp[i][j]=0
            elif i==0:
                dp[i][j]=1
            elif j<i:
                dp[i][j]=0
            else:
                dp[i][j]=dp[i][j-1]+i*(dp[i-1][j-1])

    sum=0

    for k in range(m+1):
        sum+=(((-1)**k)*(dp[k][n+1])*(m+1-k)**n)
    print(sum)
findeulerianNumber(4,1)