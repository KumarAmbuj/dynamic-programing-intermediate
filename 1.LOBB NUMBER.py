def findcoefficient(n,k):
    dp=[[0 for j in range(n+1)] for i in range(k+1)]

    for i in range(k+1):
        for j in range(n+1):
            if i==0 and j==0:
                dp[i][j]=0
            elif i==0:
                dp[i][j]=1
            elif j<i:
                dp[i][j]=0
            elif i==j:
                dp[i][j]=1
            elif j>i:
                dp[i][j]=dp[i][j-1]+dp[i-1][j-1]
    return dp[k][n]


def findlobbnumber(n,m):
    coeff=findcoefficient(2*n,m+n)

    ans=(2*m+1)*(coeff)/(m+n+1)
    print(int(ans))

findlobbnumber(3,2)


findlobbnumber(5,3)