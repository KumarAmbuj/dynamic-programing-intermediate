def findoccur(S,T,m,n,dp):
    if n==0:
        return 1
    if m==0:
        return 0

    if dp[m][n]!=-1:
        return dp[m][n]

    ans=0
    if S[m-1]==T[n-1]:
        ans=findoccur(S,T,m-1,n-1,dp)+findoccur(S,T,m-1,n,dp)
    else:
        ans=findoccur(S,T,m-1,n,dp)

    dp[m][n]=ans
    return dp[m][n]



def findOccurences(S,T):
    m=len(S)
    n=len(T)

    dp=[[-1 for i in range(n+1)] for j in range(m+1)]

    ans=findoccur(S,T,m,n,dp)
    print(ans)
s='BANANA'
t='BAN'
findOccurences(s,t)