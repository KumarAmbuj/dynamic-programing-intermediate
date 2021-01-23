def partitionproblem(arr):
    n=len(arr)
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]

    if sum%2==1:
        print('not possible ')
        return
    else:
        sum=sum//2

    dp=[[False for j in range(sum+1)] for i in range(len(arr)+1)]

    for i in range(n+1):
        for j in range(sum+1):

            if i==0 and j==0:
                dp[i][j]=True
            elif i==0:
                dp[i][j]=False
            elif j==0:
                dp[i][j]=True
            elif j<arr[i-1]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]

    print(dp[n][sum])

arr = [1, 5, 11, 5]
partitionproblem(arr)

arr = [1, 5, 3]
partitionproblem(arr)

arr = [3, 1, 5, 9, 12]
partitionproblem(arr)
