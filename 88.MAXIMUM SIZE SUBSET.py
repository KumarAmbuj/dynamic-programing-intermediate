def findmaxsize(arr,sum):
    n=len(arr)

    dp=[[False for j in range(sum+1)] for i in range(n+1)]
    count=[[0 for j in range(sum+1)] for i in range(n+1)]


    for i in range(n+1):
        for j in range(sum+1):
            if i==0 and j==0:
                dp[i][j]=True
            elif i==0:
                dp[i][j]=False
            elif j==0:
                dp[i][j]=True
            else:
                if j<arr[i-1]:
                    dp[i][j]=dp[i-1][j]
                    count[i][j]=count[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]

            if dp[i][j]==True:
                if dp[i-1][j]==True and j-arr[i-1]>=0 and dp[i-1][j-arr[i-1]]==False:
                    count[i][j]=count[i-1][j]
                elif dp[i-1][j]==False and j-arr[i-1]>=0 and dp[i-1][j-arr[i-1]]==True:
                    count[i][j]=count[i-1][j-arr[i-1]]+1
                elif dp[i-1][j]==True and j-arr[i-1]>=0 and dp[i-1][j-arr[i-1]]==True:
                    count[i][j]=max(count[i-1][j],count[i-1][j-arr[i-1]]+1)


    print(dp[n][sum])
    print(count[n][sum])
arr=[2, 3, 5, 7, 10, 15]
findmaxsize(arr,10)

arr=[1, 2, 3, 4, 5]
findmaxsize(arr,4)

arr = [2, 3, 5, 10]
sum = 20
findmaxsize(arr,sum)