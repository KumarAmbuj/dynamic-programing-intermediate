def findlps(s):

    dp=[[0 for i in range(len(s))] for j in range(len(s))]

    for g in range(len(s)):
        i=0
        j=g
        while(j<len(s)):

            if g==0:
                dp[i][j]=1

            elif g==1:
                if s[i]==s[j]:
                    dp[i][j]=2
                else:
                    dp[i][j]=1

            else:
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i+1][j])

            i+=1
            j+=1

    print(dp[0][len(s)-1])
s='geeksforgeeks'
findlps(s)
