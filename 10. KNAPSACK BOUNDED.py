def knapsack(w,wt,val,n):
    dp=[[0 for j in range(w+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,w+1):

            if j-wt[i-1]<0:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-wt[i-1]]+val[i-1])

    print(dp[n][w])

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
knapsack(W,wt,val,n)
