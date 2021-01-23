def findoccurence(S,T):
    m=len(S)
    n=len(T)
    dp=[[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(m,-1,-1):
        for j in range(n,-1,-1):

            if i==m and j==n:
                dp[i][j]=1
            elif i==m:
                dp[i][j]=0
            elif j==n:
                dp[i][j]=1
            else:
                if S[i] == T[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]




    print(dp[0][0])
s='BANANA'
t='BAN'
findoccurence(s,t)