def knapsack(wt,val,w):
    n=len(val)

    dp=[0 for i in range(w+1)]

    for i in range(1,w+1):
        mx=0

        for j in range(n):
            if i-wt[j]>=0:
                mx=max(mx,dp[i-wt[j]]+val[j])

        dp[i]=mx

    print(dp[w])

W = 100
val  = [1, 30]
wt = [1, 50]
knapsack(wt,val,W)


W = 8
val = [10, 40, 50, 70]
wt  = [1, 3, 4, 5]
knapsack(wt,val,W)