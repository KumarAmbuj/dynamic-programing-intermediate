def findNumber(n,arr):
    dp=[0 for i in range(n)]
    dp[0]=1

    count=[0 for i in range(len(arr))]

    for i in range(1,n):
        mn=100000
        for j in range(len(arr)):
            mn=min(mn,dp[count[j]]*arr[j])
        dp[i]=mn

        for j in range(len(arr)):
            if mn%arr[j]==0:
                count[j]=count[j]+1

    print(dp[n-1])

arr=[2,5]
findNumber(5,arr)

arr=[2,3,5]
findNumber(50,arr)

arr=[3,5,7,11,13]
findNumber(9,arr)

