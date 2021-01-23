def finddistinctSequence(s):
    hash={}

    dp=[0 for i in range(len(s)+1)]

    dp[0]=1

    for i in range(1,len(dp)):

        dp[i]=2*dp[i-1]

        if s[i-1] in hash:
            dp[i]-=(dp[hash[s[i-1]]-1])

        hash[s[i-1]]=i

    print(dp[len(s)])
s='gfg'
finddistinctSequence(s)

s='ggg'
finddistinctSequence(s)
