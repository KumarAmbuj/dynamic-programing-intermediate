def findmincoin(arr,n):
    dp=[None for i in range(n+1)]
    dp[0]=0

    for i in range(1,n+1):

        mn=99
        for j in range(len(arr)):
            if i-arr[j]>=0 and dp[i-arr[j]]!=None:
                mn=min(mn,dp[i-arr[j]])
        if mn!=99:
            dp[i]=mn+1
        else:
            dp[i]=None


    print(dp[n])
    print(dp)

coins = [25, 10, 5]
V = 30
findmincoin(coins,V)


coins = [9, 6, 5, 1]
V = 11
findmincoin(coins,V)


