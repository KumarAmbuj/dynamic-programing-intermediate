def findSCS(s1,s2):
    dp=[[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]

    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s2)-1,-1,-1):

            if s1[i]==s2[j]:
                dp[i][j]=dp[i+1][j+1]+1
            else:
                dp[i][j]=max(dp[i][j+1],dp[i+1][j])
    common=dp[0][0]
    print(common)

    ans=len(s1)-common+len(s2)-common+common
    print(ans)

s1='geek'
s2='eke'
findSCS(s1,s2)

s1='AGGTAB'
s2='GXTXAYB'
findSCS(s1,s2)

s1='babab'
s2='babba'
findSCS(s1,s2)


