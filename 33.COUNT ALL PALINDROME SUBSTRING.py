def countall(s):
    dp=[[False for i in range(len(s))] for j in range(len(s))]
    count=0
    for g in range(len(s)):
        i=0

        for j in range(g,len(s)):

            if g==0:
                dp[i][j]=True

            elif g==1:
                if s[i]==s[j]:
                    dp[i][j]=True
                else:
                    dp[i][j]=False

            else:
                if s[i]==s[j] and dp[i+1][j-1]==True:
                    dp[i][j]=True
                else:
                    dp[i][j]=False

            if g>0 and dp[i][j]==True:
                count+=1
            i+=1
    print(count)
s='abaab'
countall(s)

s='abbaeae'
countall(s)


