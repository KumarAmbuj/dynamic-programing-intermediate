def coingamewinner(x,y,n):
    dp=['' for i in range(n+1)]
    dp[1]='A'
    if x<=n:
        dp[x]='A'
    if y<=n:
        dp[y]='A'



    for i in range(2,n+1):
        if dp[i]=='':

            if dp[i-1]=='B':
                dp[i]='A'
            if i-x>0 and dp[i-x]=='B':
                dp[i]='A'
            if i-y>0 and dp[i-y]=='B':
                dp[i]='A'

            if dp[i]=='':
                if dp[i - 1] == 'A':
                    dp[i] = 'B'
                if i - x > 0 and dp[i - x] == 'A':
                    dp[i] = 'B'
                if i - y > 0 and dp[i - y] == 'A':
                    dp[i] = 'B'

    print(dp[n])
n=5
x=3
y=4
coingamewinner(x,y,n)





