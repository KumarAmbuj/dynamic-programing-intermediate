def findmaxsum(arr,k):
    dp=[0 for i in range(len(arr))]

    for i in range(k+1):
        dp[i]=arr[i]

    for i in range(k+1,len(arr)):
        mx=0
        for j in range(i-k-1,-1,-1):
            mx=max(mx,dp[j])
        dp[i]=mx+arr[i]

    mx=0
    for i in range(len(arr)):
        mx=max(mx,dp[i])
    print(mx)
    print(dp)

arr=[4, 5, 8, 7, 5, 4, 3, 4, 6, 5]
findmaxsum(arr,2)

arr=[50, 70, 40, 50, 90, 70, 60, 40, 70, 50]
findmaxsum(arr,2)