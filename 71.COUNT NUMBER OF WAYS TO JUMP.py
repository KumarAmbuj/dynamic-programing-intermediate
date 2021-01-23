def findways(arr):

    dp=[0 for i in range(len(arr))]

    n=len(arr)
    dp[n-1]=1



    for i in range(n-2,-1,-1):


        if arr[i]!=0:
            for j in range(1, arr[i] + 1):

                if (i + j) < n :
                    dp[i]+=dp[i+j]
    for i in range(n):
        if dp[i]==0:
            dp[i]=-1
    dp[n-1]=0

    for i in range(n):
        print(dp[i],end=' ')
arr=[3, 2, 0, 1]
findways(arr)
print()
arr=[1, 3, 5, 8, 9, 1, 0, 7, 6, 8, 9]
findways(arr)