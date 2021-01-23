def findderangements(n):

    dp=[0 for i in range(n+1)]
    dp[2]=1

    for i in range(3,n+1):
        dp[i]=(i-1)*(dp[i-1]+dp[i-2])

    print(dp[n])
    
findderangements(3)
findderangements(4)
findderangements(5)