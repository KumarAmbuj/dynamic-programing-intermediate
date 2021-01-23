def findpalindromicsequence(s,l,r):
    n=len(s)
    dp=[[False for j in range(len(s))] for i in range(len(s))]

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
            i+=1
    count=0

    for g in range(r-l+1):
        i=l
        j=l+g
        while(j<r+1):
            if dp[i][j]==True:
                count+=1
            i+=1
            j+=1

    #method 2
    count1=0
    for i in range(l,r+1):
        for j in range(i,r+1):
            if dp[i][j]==True:
                count1+=1
    print(count1)



    print(count)

s='abccbc'
findpalindromicsequence(s,3,5)

s = "xyaabax"
findpalindromicsequence(s,3,5)

s = "xyaabax"
findpalindromicsequence(s,2,3)



