def findways(n,m,k):

    dp=[[0 for j in range(m+1)]for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):

            if i==1:
                dp[i][j]=1
            elif (j+k)-i<=0:
                dp[i][j]=0
            else:
                for l in range(j,0,-1):

                    if j==l and k<i:
                        dp[i][j]+=dp[i-1][l]-1

                    else:
                        dp[i][j]+=dp[i-1][l]

    sum=0
    for i in range(1,m+1):
        sum+=dp[n][i]
    print(sum)

findways(3,3,2)
findways(3,3,1)
findways(2,3,2)