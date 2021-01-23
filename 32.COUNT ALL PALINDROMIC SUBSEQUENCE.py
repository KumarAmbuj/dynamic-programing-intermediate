def findallpalindrome(s):
    dp=[[0 for i in range(len(s))] for j in range(len(s))]

    for g in range(len(s)):
        i=0
        for j in range(g,len(s)):

            if g==0:
                dp[i][j]=1

            elif g==1:
                if s[i]==s[j]:
                    dp[i][j]=3
                else:
                    dp[i][j]=2

            else:
                if s[i]==s[j]:
                    dp[i][j]=dp[i][j-1]+dp[i+1][j]+1
                else:
                    dp[i][j]=dp[i][j-1]+dp[i+1][j]-dp[i+1][j-1]
            i+=1
    print(dp[0][len(s)-1])

s='aaaa'
findallpalindrome(s)

s='aab'
findallpalindrome(s)

s='abcd'
findallpalindrome(s)

s='abcb'
findallpalindrome(s)

