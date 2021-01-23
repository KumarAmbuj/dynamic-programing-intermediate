def maxproduct(n):
    dp=[0 for i in range(n+1)]
    dp[0]=1
    dp[1]=1

    for i in range(2,n+1):
        mx=0

        for j in range(i):
            mx=max(mx,j*(i-j),j*dp[i-j])
        dp[i]=mx

    print(dp[n])
maxproduct(2)
maxproduct(3)
maxproduct(4)
maxproduct(5)
maxproduct(6)
maxproduct(10)
maxproduct(7)
