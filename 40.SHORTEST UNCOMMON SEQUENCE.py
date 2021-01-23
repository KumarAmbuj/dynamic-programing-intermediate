def findShortestUncommon(S,T):
    dp=[[0 for j in range(len(T)+1)] for i in range(len(S)+1)]


    for i in range(len(S)-1,-1,-1):
        for j in range(len(T)-1,-1,-1):

            if S[i]==T[j]:
                dp[i][j]=dp[i+1][j+1]+1
            else:
                dp[i][j]=max(dp[i][j+1],dp[i+1][j])
    mx=dp[0][0]
    print(mx)
    ans=len(S)-mx
    if ans==0:
        print(-1)
    else:
        print(ans)

S = 'babab'
T = 'babba'
findShortestUncommon(S,T)
