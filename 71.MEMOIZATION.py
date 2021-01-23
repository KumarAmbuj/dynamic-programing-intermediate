def findpath(i,arr,dp,n):
    if i==n-1:
        dp[i]=1
        return 1
    if i>=n:
        return 0
    if dp[i]!=0:
        return dp[i]
    if arr[i]!=0:
        ans=0
        for k in range(1,arr[i]+1):
            ans+=findpath(i+k,arr,dp,n)
        dp[i]=ans
    return dp[i]




def findways(arr):
    n=len(arr)
    dp=[0 for i in range(n)]

    ans=findpath(0,arr,dp,n)
    print(ans)

arr=[3, 2, 0, 1]
findways(arr)

arr=[1, 3, 5, 8, 9, 1, 0, 7, 6, 8, 9]
findways(arr)