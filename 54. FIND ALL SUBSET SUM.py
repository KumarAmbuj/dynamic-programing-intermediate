def findallsubsetsum(arr):
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    n=len(arr)


    dp=[[False for j in range(sum+1)] for i in range(n+1)]

    for i in range(len(dp)):
        for j in range(len(dp[0])):

            if i==0 and j==0:
                dp[i][j]=True
            elif i==0:
                dp[i][j]=False
            elif j==0:
                dp[i][j]=True

            else:
                if j<arr[i-1]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
    for i in range(sum+1):
        if dp[n][i]==True:
            print(i,end=' ')
arr=[2, 3, 4, 5, 6]
findallsubsetsum(arr)
print()
arr=[1,2, 3]
findallsubsetsum(arr)