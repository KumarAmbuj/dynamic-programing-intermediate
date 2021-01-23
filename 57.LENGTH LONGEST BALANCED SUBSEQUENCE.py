def findlongestsubsequence(s):
    dp=[0 for i in range(len(s))]
    b=1
    for i in range(len(s)):
        mx=0

        if s[i]=="(":
            dp[i]=b
        elif s[i]==')':
            for j in range(i):
                if s[j]=='(':
                    mx=max(mx,dp[j])
                    b=dp[j]+2
            dp[i]=mx+1
    mx=0
    for i in range(len(s)):
        mx=max(mx,dp[i])
    print(mx)

s='()())'
findlongestsubsequence(s)

s = "()(((((()"
findlongestsubsequence(s)










