def findprobability(k,n):

    dp=[[0 for j in range(n+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(n+1):
            if i==0 and j==0:
                dp[i][j]=0
            elif i==0:
                dp[i][j]=1
            elif j<i:
                dp[i][j]=0
            elif i==1:
                dp[i][j]=j
            else:
                dp[i][j]=dp[i][j-1]+dp[i-1][j-1]

    ans=0
    p=0.5
    for i in range(k,n+1):
        ans+=dp[i][n]*(((p)**i)*(1-p)**(n-i))
    print(ans)

findprobability(2,3)
findprobability(3,6)
findprobability(12,18)
findprobability(500,1000)