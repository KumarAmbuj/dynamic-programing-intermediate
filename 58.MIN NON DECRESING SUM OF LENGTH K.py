def findminsum(arr,k):
    dp=[[0 for i in range(len(arr))] for j in range(k)]

    for i in range(k):
        for j in range(len(arr)):

            if i==0:
                dp[i][j]=arr[j]

            elif j<i:
                dp[i][j]=0

            else:
                mn=10000

                for m in range(j):

                    if arr[m]<=arr[j] and dp[i-1][m]!=0:
                        mn=min(mn,dp[i-1][m])

                dp[i][j]=mn+arr[j]
    mn=10000
    for i in range(len(arr)):
        if dp[k-1][i]!=0:
            mn=min(mn,dp[k-1][i])
    print(mn)

arr=[58, 12, 11, 12, 82, 30, 20, 77, 16, 86]
k = 3
findminsum(arr,k)

arr=[58, 12, 11, 12, 82, 30, 20, 77, 16, 86]
k = 4
findminsum(arr,k)

arr=[58, 12, 11, 12, 82, 30, 20, 77, 16, 86]
k = 5
findminsum(arr,k)