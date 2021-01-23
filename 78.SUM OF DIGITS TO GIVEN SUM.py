def findCount(sum,n):
    dp=[[0 for j in range(sum+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,sum+1):

            if i==1 and j<=sum:
                dp[i][j]=1
            elif j<i:
                dp[i][j]=0
            else:
                for k in range(1,j):
                    for l in range(1,i):
                        dp[i][j]+=dp[i-l][j-k]


    sm=0
    for i in range(n+1):
        sm+=dp[i][sum]


    print(sm)

findCount(2,2)
findCount(5,2)
findCount(6,3)
findCount(5,3)