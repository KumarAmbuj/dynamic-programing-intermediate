def findLRS(s):
    dp=[[0 for j in range(len(s)+1)]for i in range(len(s)+1)]

    for i in range(len(s)-1,-1,-1):
        for j in range(len(s)-1,-1,-1):

            if s[i]==s[j] and i!=j:
                dp[i][j]=dp[i+1][j+1]+1
            else:
                dp[i][j]=max(dp[i][j+1],dp[i+1][j])

    print(dp[0][0])
s='AABEBCDD'
findLRS(s)