def findpath(arr):
    m=len(arr)
    n=len(arr[0])

    dp=[[0 for j in range(n)] for i in range(m)]

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):

            if i==m-1 and j==n-1:
                dp[i][j]=1

            elif arr[i][j]!=-1:

                if i==m-1:
                    dp[i][j]=dp[i][j+1]
                elif j==n-1:
                    dp[i][j]=dp[i+1][j]
                else:
                    dp[i][j]=dp[i][j+1]+dp[i+1][j]
    print(dp[0][0])
    for i in range(len(dp)):
        print(dp[i])
maze = [[0, 0, 0, 0],
        [0, -1, 0, 0],
        [-1, 0, 0, 0],
        [0, 0, 0, 0 ]]

findpath(maze)


