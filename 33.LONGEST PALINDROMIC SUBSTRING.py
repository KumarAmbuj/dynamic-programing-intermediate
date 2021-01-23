def findLongestPalindromicSubstring(s):
    dp=[[False for j in range(len(s))] for i in range(len(s))]
    mx=0
    si=-1
    ei=-1
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

            if dp[i][j]==True:
                mx=g+1
                si=i
                ei=j

            i+=1
    print(mx)
    ss=''
    es=''
    res=''
    while(si<ei):
        if si==ei:
            res=ss+s[si]+es
        elif ei-si==1:
            ss=ss+s[si]
            es=s[ei]+es
            res=ss+es
        else:
            ss = ss + s[si]
            es = s[ei] + es

        si+=1
        ei-=1
    print(res)


s='forgeeksskeegfor'
findLongestPalindromicSubstring(s)

s='abccbc'
findLongestPalindromicSubstring(s)
