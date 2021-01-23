def findnumberpaths(arr):
    m=len(arr)
    n=len(arr[0])

    dp=[[0 for i in range(n)] for j in range(m)]

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if i==m-1 and j==n-1:
                dp[i][j]=arr[i][j]
            elif i==m-1:
                dp[i][j]=dp[i][j+1]+arr[i][j]
            elif j==n-1:
                dp[i][j]=dp[i+1][j]+arr[i][j]
            else:
                dp[i][j]=max(dp[i][j+1],dp[i+1][j])+arr[i][j]
    print(dp[0][0])

k = 12
arr = [[1, 2, 3],
       [4, 6, 5],
       [3, 2, 1]]

findnumberpaths(arr)